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

# Initialize session state for text input and result
if "text_input" not in st.session_state:
    st.session_state["text_input"] = ""
if "result" not in st.session_state:
    st.session_state["result"] = ""

# Text Input Box (Controlled by session state)
user_input = st.text_area("✍️ Type your message here:", value=st.session_state["text_input"], height=150)

# Buttons
col1, col2 = st.columns([1, 1])
with col1:
    check_spam = st.button("🔍 Check Spam")
with col2:
    clear_text = st.button("❌ Clear")

# Clear button functionality (Now clears both text & result)
if clear_text:
    st.session_state["text_input"] = ""  # Reset text input
    st.session_state["result"] = ""  # Reset result
    st.rerun()  # Refresh the app to clear everything

# Spam Prediction Logic
if check_spam:
    if user_input.strip():
        prediction_prob = model.predict_proba([user_input])[0]  # Get probability scores
        spam_prob = prediction_prob[1] * 100  # Spam percentage

        # Display results with confidence score
        if spam_prob > 50:
            st.session_state["result"] = f"⚠️ This message is **Spam** ({spam_prob:.2f}% confidence)."
        else:
            st.session_state["result"] = f"✅ This message is **Not Spam** ({100 - spam_prob:.2f}% confidence)."

    else:
        st.session_state["result"] = "⚠️ Please enter a message before checking."

# Display the result
if st.session_state["result"]:
    if "Spam" in st.session_state["result"]:
        st.error(st.session_state["result"])
    elif "Not Spam" in st.session_state["result"]:
        st.success(st.session_state["result"])
    else:
        st.warning(st.session_state["result"])

# Footer with Your Name
st.markdown("---")
st.markdown("🔹 Built with ❤️ by **Shaik Luqmaan** using **Streamlit & Machine Learning**")
