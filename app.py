import streamlit as st
import joblib
import numpy as np

# Load the trained model
try:
    model = joblib.load("spam_model.pkl")
except FileNotFoundError:
    st.error("⚠️ Model file not found! Please upload 'spam_model.pkl' to your GitHub repository.")
    st.stop()

# Streamlit UI Design
st.set_page_config(page_title="Spam Identifier", page_icon="📩")
st.title("📩 Spam Identifier")
st.markdown("### 🚀 Enter a message to check if it's spam or not!")

# Text Input Box
user_input = st.text_area("✍️ Type your message here:", height=150)

# Check Spam Button
check_spam = st.button("🔍 Check Spam")

# Spam Prediction Logic
if check_spam:
    if user_input.strip():
        prediction_prob = model.predict_proba([user_input])[0]  # Get probability scores
        spam_prob = prediction_prob[1] * 100  # Spam percentage

        # Display results with confidence score
        if spam_prob > 50:
            st.markdown(
                f'<div style="background-color:#FF4B4B;padding:15px;border-radius:10px;color:white;font-size:18px;">⚠️ This message is <b>Spam</b> ({spam_prob:.2f}% confidence).</div>',
                unsafe_allow_html=True
            )
        else:
            st.markdown(
                f'<div style="background-color:#4CAF50;padding:15px;border-radius:10px;color:white;font-size:18px;">✅ This message is <b>Not Spam</b> ({100 - spam_prob:.2f}% confidence).</div>',
                unsafe_allow_html=True
            )
    else:
        st.warning("⚠️ Please enter a message before checking.")

# Footer with Your Name
st.markdown("---")
st.markdown("🔹 Built with ❤️ by **Shaik Luqmaan** using **Streamlit & Machine Learning**")
