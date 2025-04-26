import numpy as np
import streamlit as st
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression


# Simulated models
def load_models():
    # Example RandomForestClassifier
    rf_model = RandomForestClassifier()
    rf_model.fit([[30, 50000, 1], [45, 70000, 0], [60, 100000, 1]], [0, 1, 0])  # Dummy data

    # Example LogisticRegression
    lr_model = LogisticRegression()
    lr_model.fit([[30, 50000, 1], [45, 70000, 0], [60, 100000, 1]], [0, 1, 0])  # Dummy data

    return {"Random Forest": rf_model, "Logistic Regression": lr_model}


# Load pre-trained models
models = load_models()

# Streamlit app
st.title("Healthcare Fraud Detection")

# Sidebar for model selection
st.sidebar.header("Model Selection")
selected_model_name = st.sidebar.selectbox("Select a model:", list(models.keys()))
selected_model = models[selected_model_name]

st.write(f"### Current Model: {selected_model_name}")

# Input form for claim data
st.write("#### Input Claim Data")
age = st.number_input("Age", min_value=18, max_value=120, value=30, step=1)
claim_amount = st.number_input("Claim Amount", min_value=1000, max_value=500000, value=50000, step=1000)
gender = st.selectbox("Gender", options=["Male", "Female"])

# Process inputs
gender_encoded = 1 if gender == "Male" else 0  # Encode gender (Male = 1, Female = 0)
input_data = np.array([[age, claim_amount, gender_encoded]])

# Prediction button
if st.button("Predict"):
    try:
        # Make prediction
        prediction = selected_model.predict(input_data)
        prediction_prob = selected_model.predict_proba(input_data)

        # Display result
        if prediction[0] == 1:
            st.success(f"The claim is predicted as **Fraudulent** with a probability of {prediction_prob[0][1]:.2f}.")
        else:
            st.info(f"The claim is predicted as **Not Fraudulent** with a probability of {prediction_prob[0][0]:.2f}.")
    except Exception as e:
        st.error(f"Error: {e}")
