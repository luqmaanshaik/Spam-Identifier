import streamlit as st

st.title("Spam Identifier")
st.write("Enter a message below to check if it's spam or not.")

user_input = st.text_area("Message:")
if st.button("Check"):
    st.write("Spam detection model output will be displayed here.")
