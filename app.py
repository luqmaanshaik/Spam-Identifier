import streamlit as st
import joblib  

# Load the trained spam detection model
@st.cache_resource
def load_model():
    return joblib.load("spam_model.pkl")  # Ensure this file is in your repository

model = load_model()

# Customizing Streamlit UI
st.set_page_config(page_title="Spam Identifier", page_icon="📩", layout="centered")

# Applying custom CSS for professional look
st.markdown(
    """
    <style>
        body { background-color: #f4f6f7; }
        .title { font-size: 40px; font-weight: bold; text-align: center; color: #2E86C1; }
        .subheader { text-align: center; font-size: 20px; color: #566573; margin-bottom: 20px; }
        .stTextArea textarea { font-size: 18px; }
        .button { background-color: #2E86C1; color: white; font-size: 18px; border-radius: 10px; padding: 10px 20px; }
        .button:hover { background-color: #1B4F72; }
        .footer { text-align: center; color: #7D3C98; margin-top: 50px; font-size: 16px; }
    </style>
    """,
    unsafe_allow_html=True,
)

# Stylish Title
st.markdown("<h1 class='title'>📧 Spam Identifier</h1>", unsafe_allow_html=True)
st.markdown("<p class='subheader'>Created by <b>Shaik Luqmaan</b></p>", unsafe_allow_html=True)

# User Input Section
st.markdown("### 🔍 Enter a message below to check if it's spam or not.")
user_input = st.text_area("✉️ Message:", "")

# Prediction Button with Empty Input Handling
if st.button("🔎 Predict", key="predict", help="Click to classify the message"):
    if user_input.strip() == "":  # Prevent empty input
        st.warning("⚠️ Please enter a message before predicting.")
    else:
        prediction = model.predict([user_input])  # Model Prediction
        if prediction[0] == 1:
            st.error("🚨 **Spam Message Detected!**")
        else:
            st.success("✅ **Not Spam Message!**")

# Footer with LinkedIn Profile
st.markdown(
    """
    <hr>
    <p class='footer'>Made with ❤️ by <b>Shaik Luqmaan</b> | <a href="https://www.linkedin.com/in/shaikluqmaan" target="_blank">LinkedIn</a></p>
    """,
    unsafe_allow_html=True,
)
