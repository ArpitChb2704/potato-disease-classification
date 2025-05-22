# 🥔 Potato Disease Classification Web App

This is a full-stack machine learning project that classifies potato leaf diseases using image input. The model predicts whether a potato leaf is **healthy**, infected with **early blight**, or **late blight**.

The project consists of:
- 🧠 A Convolutional Neural Network (CNN) model trained on a dataset of potato leaf images
- ⚙️ A FastAPI backend for serving model predictions as an API
- 🎨 A Streamlit frontend for user interaction
- ☁️ Both backend and frontend deployed on [Render](https://render.com)

---

## 📂 Project Structure

├── backend- ─ main.py/ # FastAPI app for model inference
├── frontend- app.py/ # Streamlit app for frontend UI
├── model/ # Saved trained model
│ └── potato_model.h5
├── requirements.txt # Combined dependencies
├── PlantVillage # Leaf Images Folder
│ └── Healthy
    - Early Blight
    - Late Blight
└── README.md # This file

**[👉 Dataset Link – _https://www.kaggle.com/datasets/arjuntejaswi/plant-village]**

## 🧠 Model Details

- A **CNN (Convolutional Neural Network)** was built using TensorFlow/Keras.
- The model was trained on the potato leaf image dataset.
- After training, the model was saved and served using FastAPI.

---

## ⚙️ Backend (FastAPI)

The backend is built using **FastAPI** and exposes a `/predict` endpoint that accepts image files and returns the predicted class.

🛰️ **Deployed Backend API:**  
**[👉 API URL – https://potato-disease-classification-ltgh.onrender.com/ping]**

---

## 🎨 Frontend (Streamlit)

The frontend is a user-friendly Streamlit app where users can upload leaf images and get real-time disease predictions.

🌐 **Live Frontend App:**  
**[👉 Streamlit App URL – https://potato-disease-classification-1-hbm5.onrender.com_]**

---
## 📌 Inspired By

This project is inspired by the YouTube tutorial from the amazing channel Codebasics. Be sure to check it out for a step-by-step breakdown of similar projects!
