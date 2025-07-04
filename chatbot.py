import streamlit as st
import google.generativeai as genai
import datetime
import os

# --- Configure Gemini API key ---
api_key = st.secrets.get("GEMINI_API_KEY") or os.getenv("GEMINI_API_KEY")
if not api_key:
    st.error("❌ GEMINI_API_KEY is missing in secrets.toml or environment!")
    st.stop()

genai.configure(api_key=api_key)
model = genai.GenerativeModel(model_name="gemini-2.0-flash")

# --- Streamlit Page Config ---
st.set_page_config(
    page_title=" JustinAI",
    page_icon="⚡",
    layout="centered"
)

# --- Header with Logo and Title ---
st.markdown(
    """
    <div style='text-align: center; padding-top: 10px;'>
        <img src='logo.png' width='180' style='margin-bottom: 10px;' />
        <h1 style='margin: 0; font-size: 3em;'>⚡ JustinAI</h1>
        <p style='color: gray; font-size: 1.1em;'>Coffee powered AI - yapping assistant</p>
    </div>
    <hr style='border-top: 1px solid #444;' />
    """,
    unsafe_allow_html=True
)

# --- Initialize chat session ---
if "chat" not in st.session_state:
    st.session_state.chat = model.start_chat(history=[])

# --- Display chat history ---
for message in st.session_state.chat.history:
    role = message.role  # "user" or "model"
    with st.chat_message(role):
        st.markdown(message.parts[0].text)

# --- Chat input ---
user_input = st.chat_input("Type your message...")

if user_input:
    with st.chat_message("user"):
        st.markdown(user_input)

    try:
        response = st.session_state.chat.send_message(user_input)
        with st.chat_message("assistant"):
            st.markdown(response.text)
    except Exception as e:
        st.error(f"⚠️ Flash 2.0 Error: {e}")

# --- Footer with date/time ---
now = datetime.datetime.now().strftime("%B %d, %Y at %I:%M %p")
st.markdown("---")
st.markdown(
    f"""
    <div style='text-align: center; color: gray; font-size: 0.9em; margin-bottom: 20px;'>
        Made with ❤️ by Justin<br>
        <span style='font-size: 0.8em;'>Last updated {now}</span>
    </div>
    """,
    unsafe_allow_html=True
)
