import streamlit as st
from PIL import Image
import pytesseract
import re
import joblib
import numpy as np

# Load trained ML model
model = joblib.load("insurance_model.pkl")  # Ensure this .pkl exists in the same folder

# Function to extract text from uploaded image
def extract_text_from_image(image_file):
    image = Image.open(image_file)
    text = pytesseract.image_to_string(image)
    return text

# Function to extract numeric feature(s) from text
def extract_features(text):
    # You can customize this with your actual feature extraction logic
    amount_match = re.search(r'Total\s*[:\-]?\s*\₹?(\d+)', text, re.IGNORECASE)
    amount = int(amount_match.group(1)) if amount_match else 0
    return [amount]

# Prediction logic
def predict_claim(features_vector):
    prediction = model.predict([features_vector])
    return "Approved" if prediction[0] == 1 else "Rejected"

# Streamlit UI
st.title("🧾 Smart Claim Approval Bot")

uploaded_file = st.file_uploader("Upload medical bill", type=["jpg", "jpeg", "png"])

if uploaded_file:
    # OCR Text Extraction
    text = extract_text_from_image(uploaded_file)
    st.text_area("Extracted OCR Text", text, height=250)

    # Extract Features from Image
    image_features = extract_features(text)
    st.write("Extracted Features from Invoice:", image_features)

    # Collect additional user inputs
    st.subheader("➕ Additional Info Required")

    bmi = st.number_input("Enter your BMI:", min_value=10.0, max_value=50.0, value=22.5, step=0.1)
    children = st.number_input("Number of children:", min_value=0, max_value=10, step=1)
    smoker = st.selectbox("Are you a smoker?", ["No", "Yes"])
    is_smoker = 1 
    if smoker == "Yes" 
    else 0

    if st.button("Predict Claim Status"):
        full_features = image_features + [bmi, children, is_smoker]
        decision = predict_claim(full_features)
        st.success(f"✅ Claim Status: {decision}")

