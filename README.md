**Brain Tumor Classification System for Hospital Malacca**
AI-Powered MRI Brain Tumor Classification (Flask + TensorFlow)
The system allows medical staff to upload MRI images and receive instant predictions for:
    Glioma
    Meningioma
    Pituitary
    No Tumor
Built using TensorFlow, Flask, and deployed on Fly.io.

**🏥 Project Overview**
This project is developed for Hospital Melaka as part of a medical innovation initiative.
The goal is to assist doctors by providing fast, offline-capable, and lightweight tumor classification using CNN models trained in Google Colab.

**🧠 Model Details**
Image size: 150×150 
Optimizer: Adam
Loss: categorical crossentropy
Training dataset: brain MRI images 
https://www.kaggle.com/datasets/masoudnickparvar/brain-tumor-mri-dataset
Model saved as model.h5

**⭐ Features  **
✔ Upload MRI image via a secure web interface
✔ Deep learning CNN model generates prediction
✔ Real-time probability output
✔ Lightweight architecture suitable for deployment on Fly.io

**📁 Project Structure**
├── app.py                   
├── model/
│   └── brain_tumor_model.h5 
├── templates/
│   ├── welcome.html           
│   ├── uploadImage.html          
│   └── result.html
├── static/
│   └── uploads/
├── Dockerfile             
├── fly.toml                 
├── requirements.txt
└── README.md

**👨‍💻 Developers**
Project Manager    - Aevan Cheong Wei Ren
Technical Support  - Yew Zhi Yu
Marketing          - Soon Ching Mei
Treasurer          - Wong Jing Wen
Secretary          - Hoo Jin Yi
