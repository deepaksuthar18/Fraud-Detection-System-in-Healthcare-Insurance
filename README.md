# Fraud-Detection-System-in-Healthcare-Insurance

This is a simple Machine Learning web application built using Streamlit to detect fraudulent healthcare insurance claims.
It allows users to input basic claim data and predicts whether the claim is Fraudulent or Not Fraudulent.

<h2>Features</h2>
Model Selection: Choose between two machine learning models:

Random Forest Classifier

Logistic Regression

User Input Form: Input Age, Claim Amount, and Gender.

Prediction: Predicts if the insurance claim is fraudulent, showing probability scores.

Interactive UI: Clean, fast, and responsive web app using Streamlit.

Algorithms Used
Random Forest Classifier: An ensemble learning method that operates by constructing multiple decision trees and outputs the mode of the classes.

Logistic Regression: A statistical model that uses a logistic function to model a binary dependent variable (fraudulent or not).

How it Works
Two ML models are trained on dummy sample data inside the app.

Based on user inputs (age, claim amount, and gender), the selected model predicts the fraud status.

Gender is encoded as: Male → 1, Female → 0.

Tech Stack
Python

Streamlit (for the Web Interface)

Scikit-learn (for Machine Learning models)
