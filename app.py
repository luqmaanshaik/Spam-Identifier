
import streamlit as st
import pandas as pd
import joblib
from sklearn.feature_extraction.text import CountVectorizer

# Load the trained model and vectorizer
model = joblib.load("spam_model.pkl")  # Replace with your actual model file name
vectorizer = joblib.load("vectorizer.pkl")  # Replace with your actual vectorizer file name

# Streamlit App UI
st.title("Spam Identifier")
st.write("Enter a message below to check if it's spam or not.")

user_input = st.text_area("Enter your message:")

if st.button("Check Spam"):
    if user_input:
        # Transform input using the saved vectorizer
        input_vectorized = vectorizer.transform([user_input])
        
        # Predict using the trained model
        prediction = model.predict(input_vectorized)
        
        # Display Result
        if prediction[0] == 1:
            st.error("⚠️ This message is **Spam**.")
        else:
            st.success("✅ This message is **Not Spam**.")
    else:
        st.warning("Please enter a message to classify.")
