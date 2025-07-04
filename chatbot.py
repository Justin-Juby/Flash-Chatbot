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
# --- Centered Logo ---
st.markdown("<div style='text-align:center; margin-top: 20px;'>", unsafe_allow_html=True)
st.image("logo.png", width=220)
st.markdown("</div>", unsafe_allow_html=True)

# --- Fully Purple Themed Title & Subtitle ---
st.markdown(
    """
    <div style='text-align: center; font-family: "Segoe UI", Tahoma, Geneva, Verdana, sans-serif;'>
        <h1 style='font-size: 3.2em; font-weight: 800; color: #7C3AED; margin: 10px 0 5px 0;'>⚡ Justin-AI</h1>
        <p style='color: #A855F7; font-size: 1.25em; margin-top: 0; font-weight: 500; letter-spacing: 0.03em;'>
            Coffee-powered AI — for your daily tasks
        </p>
    </div>
    <hr style='border-top: 1px solid #C4B5FD; margin-top: 30px;' />
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

