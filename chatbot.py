import streamlit as st
import google.generativeai as genai
import os

# ✅ Configure the API key (make sure GEMINI_API_KEY is set)
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# ✅ Load Gemini model
model = genai.GenerativeModel(model_name="gemini-2.0-flash")

# ✅ Setup chat session with persistent history
if "chat" not in st.session_state:
    st.session_state.chat = model.start_chat(history=[])

# ✅ Streamlit page config
st.set_page_config(page_title="⚡ JustinFlash  — Chatbot", layout="centered")
st.title("⚡ JustinFlash  — Chatbot")

# ✅ Display previous messages
for message in st.session_state.chat.history:
    role = message.role  # "user" or "model"
    with st.chat_message(role):
        st.markdown(message.parts[0].text)


# ✅ Input box for new messages
user_input = st.chat_input("Ask me anything...")

if user_input:
    # Show user's message
    st.chat_message("user").markdown(user_input)

    try:
        # Send input to Gemini
        response = st.session_state.chat.send_message(user_input)

        # Show bot's response
        st.chat_message("assistant").markdown(response.text)
    except Exception as e:
        st.error(f"⚠️ Flash 2.0 Error: {e}")
