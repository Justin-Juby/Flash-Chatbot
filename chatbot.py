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
# chatbot.py

import streamlit as st
import google.generativeai as genai
import datetime
import os

# --- Setup Gemini API ---
api_key = st.secrets.get("GEMINI_API_KEY") or os.getenv("GEMINI_API_KEY")
if not api_key:
    st.error("❌ GEMINI_API_KEY is missing in secrets.toml or environment!")
    st.stop()

genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-2.0-flash")



# --- Streamlit Page Setup ---
st.set_page_config(
    page_title="⚡ JFlash 2.0 Chatbot",
    page_icon="⚡",
    layout="centered"
)

# --- Title & Branding ---
# --- Centered Large Logo and Title ---
st.markdown(
    """
    <div style='text-align: center; padding-top: 10px;'>
        <img src='logo.png' width='160' style='margin-bottom: 10px;' />
        <h1 style='margin: 0; font-size: 2.8em;'>⚡ Flash 2.0</h1>
        <p style='color: gray; font-size: 1.1em;'>Justin powered AI - yapping assistant</p>
    </div>
    <hr style='border-top: 1px solid #444;' />
    """,
    unsafe_allow_html=True
)



# --- Session State Chat History ---
if "chat" not in st.session_state:
    st.session_state.chat = model.start_chat(history=[])

# --- Chat Input Box ---
prompt = st.chat_input("Type your message...")

if prompt:
    # Show user message
    with st.chat_message("user"):
        st.markdown(prompt)

    try:
        # Get model response
        response = st.session_state.chat.send_message(prompt)

        # Show model response
        with st.chat_message("assistant"):
            st.markdown(response.text)

    except Exception as e:
        st.error(f"⚠️ Flash 2.0 Error: {str(e)}")

# --- Footer ---
now = datetime.datetime.now().strftime("%B %d, %Y at %I:%M %p")
st.markdown("---")
st.markdown(
    f"""
    <div style='text-align: center; color: gray; font-size: 0.9em;'>
        Made with ⚡ by Justin<br>
        <span style='font-size: 0.8em;'>Last updated {now}</span>
    </div>
    """,
    unsafe_allow_html=True
)
