import streamlit as st
import joblib  

# Load the trained spam detection model
@st.cache_resource
def load_model():
    return joblib.load("spam_model.pkl")  # Ensure this file is in your repository

model = load_model()

# Streamlit Page Configuration
st.set_page_config(page_title="Spam Identifier", page_icon="📩", layout="centered")

# Custom CSS for a Professional Look
st.markdown(
    """
    <style>
        body { background-color: #f8f9fa; }
        .title { font-size: 42px; font-weight: bold; text-align: center; color: #2C3E50; }
        .subheader { text-align: center; font-size: 20px; color: #7B7D7D; margin-bottom: 20px; }
        .stTextArea textarea { font-size: 18px; border-radius: 10px; padding: 10px; }
        .button-container { display: flex; justify-content: center; }
        .button { background-color: #3498DB; color: white; font-size: 18px; border-radius: 10px; padding: 12px 24px; font-weight: bold; border: none; cursor: pointer; }
        .button:hover { background-color: #1B4F72; }
        .spam-message { color: white; background-color: #E74C3C; padding: 15px; border-radius: 10px; text-align: center; font-size: 18px; }
        .not-spam-message { color: white; background-color: #2ECC71; padding: 15px; border-radius: 10px; text-align: center; font-size: 18px; }
        .footer { text-align: center; color: #566573; margin-top: 50px; font-size: 16px; }
        .links { text-align: center; margin-top: 10px; }
        .links a { color: #2980B9; text-decoration: none; font-size: 18px; margin: 0 15px; font-weight: bold; }
        .links a:hover { text-decoration: underline; }
        hr { border: none; height: 1px; background-color: #D5D8DC; margin-top: 40px; }
    </style>
    """,
    unsafe_allow_html=True,
)

# App Title
st.markdown("<h1 class='title'>📩 Spam Identifier</h1>", unsafe_allow_html=True)
st.markdown("<p class='subheader'>Created by <b>Shaik Luqmaan</b></p>", unsafe_allow_html=True)

# User Input Section
st.markdown("### 🔍 Enter a message below to check if it's spam or not.")
user_input = st.text_area("✉️ Message:", "", placeholder="Type your message here...")

# Centered Prediction Button
st.markdown("<div class='button-container'>", unsafe_allow_html=True)
if st.button("🔎 Predict"):
    if user_input.strip() == "":  # Prevent empty input
        st.warning("⚠️ Please enter a message before predicting.")
    else:
        prediction = model.predict([user_input])  # Model Prediction
        if prediction[0] == 1:
            st.markdown("<p class='spam-message'>🚨 <b>Spam Message Detected! Be cautious.</b></p>", unsafe_allow_html=True)
        else:
            st.markdown("<p class='not-spam-message'>✅ <b>This message is safe!</b></p>", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

# Footer with LinkedIn & GitHub Links
st.markdown(
    """
    <hr>
    <p class='footer'>Made with ❤️ by <b>Shaik Luqmaan</b></p>
    <div class='links'>
        <a href="https://www.linkedin.com/in/luqmaan-shaik-2166502a8/" target="_blank">🔗 LinkedIn</a>
        <a href="https://github.com/luqmaanshaik" target="_blank">🔗 GitHub</a>
    </div>
    """,
    unsafe_allow_html=True,
)
