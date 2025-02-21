import streamlit as st
import joblib

# Load the trained model
try:
    model = joblib.load("spam_model.pkl")
except FileNotFoundError:
    st.error("⚠️ Model file not found! Please upload 'spam_model.pkl' to your GitHub repository.")

# Streamlit UI
st.title("Spam Identifier")
st.write("Enter a message below to check if it's spam or not.")

user_input = st.text_area("Enter your message:")

if st.button("Check Spam"):
    if user_input:
        prediction = model.predict([user_input])
        if prediction[0] == 1:
            st.error("⚠️ This message is **Spam**.")
        else:
            st.success("✅ This message is **Not Spam**.")
    else:
        st.warning("Please enter a message to classify.")
