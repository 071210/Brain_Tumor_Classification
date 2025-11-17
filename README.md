# Brain Tumor Classification for Hospital Malacca
**BAXI S1G1 - Group E**  
**Universiti Teknikal Malaysia Melaka (UTeM)**  

---

## Overview
The Brain Tumor Classification System is an AI-powered medical imaging project developed for Hospital Melaka.
The system assists healthcare professionals by automatically analyzing MRI brain scans and predicting four categories of brain tumors:
- Glioma
- Meningioma
- Pituitary Tumor
- No Tumor

The solution uses a Convolutional Neural Network (CNN) model trained in Google Colab and integrates with a Flask-based web system where hospital staff can upload MRI images to receive instant predictions.

---

## Project Objectives
1. **Develop a high-accuracy CNN model** capable of classifying MRI brain tumors into four categories. 
2. **Provide a simple and secure web interface** for hospital staff to upload MRI scans.  
3. **Ensure the system is lightweight and easy to maintain**, enabling integration into hospital workflows.

---

## Project Modules

### **Module 1 — Web Interface**
- Develop a clean, simple UI for medical staff
- Implement secure MRI upload page
- Build result display page with tumor class & confidence
- Organize templates (welcome, upload, result pages)

### **Module 2 — Model Development (CNN)**
- Use the Kaggle MRI Brain Tumor Dataset
  https://www.kaggle.com/datasets/masoudnickparvar/brain-tumor-mri-dataset
- Build CNN architecture 
- Train model 
- Save model as .h5
- Validate accuracy using confusion matrix & classification report

### **Module 3 — Deployment & Integration**
- Connect Flask backend for prediction API
- Containerize app with Docker
- Configure Fly.io
- Test prediction performance with real MRI samples

---

## Team (Group E)

| Name | Matric No. | Role |
|------|-------------|------|
| **Aevan Cheong Wei Ren** | B032310355 | Project Manager |
| **Yew Zhi Yu** | B032310595 | Technical Support |
| **Soon Ching Mei** | B032310451 | Marketing |
| **Wong Jing Wen** | B032310517 | Treasurer |
| **Hoo Jin Yi** | B032310356 | Secretary | 

---
## Website link
https://ai-project-management-project.fly.dev/

