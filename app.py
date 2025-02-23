import streamlit as st
import joblib  

# Load the trained spam detection model
@st.cache_resource
def load_model():
    return joblib.load("spam_model.pkl")  # Ensure this file is in your repository

model = load_model()

# Streamlit Page Configuration
st.set_page_config(page_title="Spam Identifier", page_icon="📩", layout="centered")

# Custom CSS for Dark Themed Spam Identifier UI
st.markdown(
    """
    <style>
        body { background-color: #121212; }
        .title { font-size: 42px; font-weight: bold; text-align: center; color: #ffffff; }
        .subheader { text-align: center; font-size: 18px; color: #cccccc; margin-bottom: 20px; }
        .stTextArea textarea { font-size: 16px; border-radius: 10px; padding: 10px; background-color: #222; color: white; border: 1px solid #444; }
        .button-container { display: flex; justify-content: center; margin-top: 10px; }
        .spam-message { color: white; background-color: #E74C3C; padding: 15px; border-radius: 10px; text-align: center; font-size: 18px; font-weight: bold; }
        .not-spam-message { color: white; background-color: #2ECC71; padding: 15px; border-radius: 10px; text-align: center; font-size: 18px; font-weight: bold; }
        .footer { text-align: center; color: #bbbbbb; margin-top: 50px; font-size: 14px; }
        .links { text-align: center; margin-top: 10px; }
        .links a { text-decoration: none; font-size: 16px; margin: 0 15px; font-weight: bold; color: #cccccc; }
        .links img { width: 30px; height: 30px; vertical-align: middle; margin-right: 5px; }
        hr { border: none; height: 1px; background-color: #555; margin-top: 40px; }
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
col1, col2, col3 = st.columns([2, 1, 2])  # Centers the button
with col2:
    if st.button("🔎 Predict"):
        if user_input.strip() == "":
            st.warning("⚠️ Please enter a message before predicting.")
        else:
            probability = model.predict_proba([user_input])[0][1]  # Get spam probability
            spam_percentage = round(probability * 100, 2)

            if probability > 0.5:
                st.markdown(
                    f"<p class='spam-message'>🚨 <b>Spam Message Detected! ({spam_percentage}% Spam Probability)</b></p>",
                    unsafe_allow_html=True,
                )
            else:
                st.markdown(
                    f"<p class='not-spam-message'>✅ <b>This message is safe! ({100 - spam_percentage}% Not Spam Probability)</b></p>",
                    unsafe_allow_html=True,
                )

# Footer with GitHub and LinkedIn Links
st.markdown(
    """
    <hr>
    <p class='footer'>Made with ❤️ by <b>Shaik Luqmaan</b></p>
    <div class='links'>
        <a href="https://github.com/luqmaanshaik" target="_blank">
            <img src="https://cdn-icons-png.flaticon.com/512/25/25231.png"> GitHub
        </a>
        <a href="https://www.linkedin.com/in/luqmaan-shaik-2166502a8/" target="_blank">
            <img src="https://cdn-icons-png.flaticon.com/512/174/174857.png"> LinkedIn
        </a>
    </div>
    """,
    unsafe_allow_html=True,
)
