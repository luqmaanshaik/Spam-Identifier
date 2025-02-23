import streamlit as st
import joblib  

# Load the trained spam detection model
@st.cache_resource
def load_model():
    return joblib.load("spam_model.pkl")  # Ensure this file is in your repository

model = load_model()

# Streamlit Page Configuration
st.set_page_config(page_title="Spam Detector", page_icon="🚨", layout="centered")

# Custom CSS for Spam-Themed UI
st.markdown(
    """
    <style>
        body { background-color: #121212; color: white; }
        .title { font-size: 42px; font-weight: bold; text-align: center; color: #ff4b5c; text-shadow: 2px 2px 10px red; }
        .subheader { text-align: center; font-size: 18px; color: #d1d1d1; margin-bottom: 20px; }
        .stTextArea textarea { font-size: 16px; border-radius: 8px; padding: 10px; background-color: #1e1e1e; color: white; border: 1px solid #ff4b5c; }
        .button-container { display: flex; justify-content: center; }
        .button { background-color: #ff4b5c; color: white; font-size: 18px; border-radius: 8px; padding: 12px 24px; font-weight: bold; border: none; cursor: pointer; text-shadow: 1px 1px 5px black; }
        .button:hover { background-color: #d63031; box-shadow: 0px 0px 10px red; }
        .spam-message { color: white; background-color: #ff4b5c; padding: 15px; border-radius: 8px; text-align: center; font-size: 18px; box-shadow: 0px 0px 10px red; }
        .not-spam-message { color: white; background-color: #2ecc71; padding: 15px; border-radius: 8px; text-align: center; font-size: 18px; box-shadow: 0px 0px 10px green; }
        .footer { text-align: center; color: #888; margin-top: 50px; font-size: 16px; }
        .links { text-align: center; margin-top: 10px; }
        .links a { text-decoration: none; font-size: 18px; margin: 0 15px; font-weight: bold; color: white; }
        .links img { width: 30px; height: 30px; vertical-align: middle; margin-right: 5px; }
        hr { border: none; height: 1px; background-color: #333; margin-top: 40px; }
    </style>
    """,
    unsafe_allow_html=True,
)

# App Title
st.markdown("<h1 class='title'>🚨 Spam Detector</h1>", unsafe_allow_html=True)
st.markdown("<p class='subheader'>Created by <b>Shaik Luqmaan</b> - AI & Cybersecurity Enthusiast</p>", unsafe_allow_html=True)

# User Input Section
st.markdown("### 🔍 Enter a message below to check if it's spam or not.")
user_input = st.text_area("✉️ Message:", "", placeholder="Type your message here...")

# Centered Prediction Button
st.markdown("<div class='button-container'>", unsafe_allow_html=True)
if st.button("🔎 Detect Spam"):
    if user_input.strip() == "":
        st.warning("⚠️ Please enter a message before detecting spam.")
    else:
        probability = model.predict_proba([user_input])[0][1]  
        spam_percentage = round(probability * 100, 2) 
        
        if probability > 0.5:
            st.markdown(f"<p class='spam-message'>🚨 <b>Spam Detected! ({spam_percentage}% Spam Probability)</b></p>", unsafe_allow_html=True)
        else:
            st.markdown(f"<p class='not-spam-message'>✅ <b>Not Spam! ({100 - spam_percentage}% Safe Probability)</b></p>", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

# Footer with GitHub and LinkedIn
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
