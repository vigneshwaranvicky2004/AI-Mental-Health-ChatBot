import streamlit as st
from chain_definition import chain

st.set_page_config(page_title="🧠 Mental Health Chatbot", page_icon="💬")
st.title("🧠 Mental Health Support Chatbot")

user_input = st.text_input("💬 How are you feeling today?")

if user_input:
    with st.spinner("Thinking..."):
        try:
            response = chain.run(user_input=user_input)
            st.success(response)
        except Exception as e:
            st.error(f"❌ Error: {e}")
