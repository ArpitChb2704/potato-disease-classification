import streamlit as st
import requests
from PIL import Image
import io

# Streamlit app title
st.title("🥔 Potato Leaf Disease Classifier")

# Upload image
uploaded_file = st.file_uploader("Upload a potato leaf image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Show preview
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    # Button to trigger prediction
    if st.button("Predict"):
        with st.spinner("Classifying..."):
            # Send image to FastAPI backend
            response = requests.post(
                "http://localhost:8000/predict",
                files={"file": uploaded_file.getvalue()}
            )
            
            if response.status_code == 200:
                result = response.json()
                st.success(f"🌿 Predicted Class: **{result['class']}**")
                st.info(f"📈 Confidence: **{result['confidence'] * 100:.2f}%**")
            else:
                st.error("Prediction failed. Please try again.")
