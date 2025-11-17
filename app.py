from flask import Flask, render_template, request, jsonify, session, redirect, url_for
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import load_img, img_to_array
from werkzeug.utils import secure_filename
import numpy as np
import os
import json

# Initialize Flask
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads'
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg'}
app.config['SECRET_KEY'] = 'super-secret-key'  # Needed for sessions

# Load your trained model
model = load_model("model/brain-tumor-model.h5")


# Load class indices saved from Colab
with open("model/class_indices.json", "r") as f:
    class_indices = json.load(f)

# Ensure the correct order
CLASS_TYPES = [k for k,v in sorted(class_indices.items(), key=lambda x: x[1])]

print("DEBUG: CLASS_TYPES order:", CLASS_TYPES)

# Allowed file check
def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in app.config["ALLOWED_EXTENSIONS"]

# Preprocess image and predict
def predict_image(image_path, target_size=(150,150)):
    img = load_img(image_path, target_size=target_size, color_mode='rgb')
    img_array = img_to_array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)
    
    predictions = model.predict(img_array)
    
    class_index = np.argmax(predictions)
    confidence = float(np.max(predictions) * 100)
    predicted_class = CLASS_TYPES[class_index]
    
    return predicted_class, f"{confidence:.2f}%"


# Routes
@app.route("/")
def welcome():
    return render_template("welcome.html")

@app.route("/uploadImage")
def upload_page():
    return render_template("uploadImage.html")

@app.route("/result")
def result_page():
    if 'prediction_result' not in session:
        return redirect(url_for('upload_page'))
    
    result = session['prediction_result']
    return render_template("result.html", 
                           tumor_type=result['tumor_type'],
                           confidence=result['confidence'],
                           image_url=result['image_url'])

@app.route("/predict", methods=["POST"])
def predict():
    if "file" not in request.files:
        return jsonify({"error": "No file uploaded"}), 400
    
    file = request.files["file"]
    if file.filename == "":
        return jsonify({"error": "No file selected"}), 400
    
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        os.makedirs(app.config["UPLOAD_FOLDER"], exist_ok=True)
        filepath = os.path.join(app.config["UPLOAD_FOLDER"], filename)
        file.save(filepath)

        # Predict
        tumor_type, confidence = predict_image(filepath)
        result = {
            "tumor_type": tumor_type,
            "confidence": confidence,
            "image_url": "/" + filepath.replace("\\", "/")
        }
        
        session['prediction_result'] = result
        return jsonify({"success": True, "redirect": url_for('result_page')})
    
    return jsonify({"error": "Invalid file type"}), 400

# Redirect HTML routes
@app.route("/welcome.html")
@app.route("/uploadImage.html")
@app.route("/result.html")
def redirect_html():
    html_to_route = {
        "welcome.html": "welcome",
        "uploadImage.html": "upload_page",
        "result.html": "result_page"
    }
    endpoint = request.path.split('/')[-1]
    route_name = html_to_route.get(endpoint, "welcome")
    return redirect(url_for(route_name))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
