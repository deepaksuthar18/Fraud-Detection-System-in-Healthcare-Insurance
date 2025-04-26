import streamlit as st
import pickle
import pandas as pd

# Title of the app
st.title("Fraud Detection System in Healthcare Insurance")

# Sidebar for model selection
st.sidebar.header("Model Selection")
st.sidebar.write("Note: Currently using the best trained model.")
model_option = "Best Model"

# Load the best model
try:
    with open('Notebook and dataset/best_model.pkl', 'rb') as f:
        selected_model = pickle.load(f)
except FileNotFoundError:
    st.error("Error: 'best_model.pkl' file not found. Please ensure the file is in the correct folder.")
    st.stop()

# Input claim data
st.header("Input Claim Data")
age = st.number_input("Age", min_value=18, max_value=100, value=30)
claim_amount = st.number_input("Claim Amount", min_value=0, value=1000)
gender = st.selectbox("Gender", ["Male", "Female"])

# Convert inputs to a DataFrame
input_data = pd.DataFrame({
    "Age": [age],
    "Claim Amount": [claim_amount],
    "Gender": [0 if gender == "Male" else 1]
})

# Make prediction
if st.button("Predict"):
    prediction = selected_model.predict(input_data)
    fraud_types = {0: "No Fraud", 1: "Ghost Enrolled", 2: "Phantom Billing", 3: "Fake Treatment"}
    st.success(f"Prediction: {fraud_types.get(prediction[0], 'Unknown')}")

