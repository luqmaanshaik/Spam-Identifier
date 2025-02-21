import streamlit as st
import joblib  # Ensure joblib is installed

# Load the trained spam detection model
@st.cache_resource
def load_model():
    return joblib.load("spam_model.pkl")  # Ensure this file is in your repository

model = load_model()

# Streamlit App Title
st.title("📧 Spam Identifier")
st.write("Enter a message below to check if it's spam or not.")

# User Input
user_input = st.text_area("Message:", "")

# Prediction Button with Empty Input Handling
if st.button("Predict"):
    if user_input.strip() == "":  # Prevent empty input
        st.warning("⚠️ Please enter a message before predicting.")
    else:
        prediction = model.predict([user_input])  # Model Prediction
        result = "**Spam** 🚨" if prediction[0] == 1 else "**Not Spam** ✅"
        st.success(f"Prediction: {result}")
