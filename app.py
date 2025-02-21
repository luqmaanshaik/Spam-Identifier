import streamlit as st
import joblib  # Ensure joblib is installed

# Load the trained spam detection model
@st.cache_resource
def load_model():
    return joblib.load("spam_model.pkl")  # Ensure this file is in your repository

model = load_model()

# Customizing Streamlit UI
st.set_page_config(page_title="Spam Identifier", page_icon="📩", layout="centered")

# Stylish Title
st.markdown(
    """
    <h1 style='text-align: center; color: #2E86C1;'>📧 Spam Identifier</h1>
    <p style='text-align: center; color: #566573; font-size: 18px;'>Created by <b>Shaik Luqmaan</b></p>
    """,
    unsafe_allow_html=True,
)

st.write("🔍 **Enter a message below to check if it's spam or not.**")

# User Input
user_input = st.text_area("✉️ Message:", "")

# Prediction Button with Empty Input Handling
if st.button("🔎 Predict"):
    if user_input.strip() == "":  # Prevent empty input
        st.warning("⚠️ Please enter a message before predicting.")
    else:
        prediction = model.predict([user_input])  # Model Prediction
        if prediction[0] == 1:
            st.error("🚨 **Spam Message Detected!**")
        else:
            st.success("✅ **Not Spam**")

# Footer
st.markdown(
    """
    <br><hr>
    <p style='text-align: center; color: #7D3C98;'>Made with ❤️ by <b>Shaik Luqmaan</b></p>
    """,
    unsafe_allow_html=True,
)
