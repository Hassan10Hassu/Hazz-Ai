import streamlit as st
import google.generativeai as genai
import fal_client
import os

# 1. 🔑 KEYS (Same as before)
GEMINI_KEY = "AIzaSyCTrIsSO7JYwHG5pKzbtwZ_jomBnbZhu9M"
FAL_KEY = "3fc8d750-df6c-48ff-91da-ff5e4e6a99db:448b685fb163176440ba6edb57490cbe"
os.environ["FAL_KEY"] = FAL_KEY

# 2. 🚀 SPEED BOOST: Cache the Brain
# This keeps the AI "awake" so it doesn't have to restart every time.
@st.cache_resource
def init_models():
    genai.configure(api_key=GEMINI_KEY)
    # Using 'flash-lite' for 0.2s response times
    return genai.GenerativeModel('gemini-1.5-flash-8b') 

model = init_models()

# 3. 🎨 UI SETUP
st.set_page_config(page_title="Hazz Ai | Turbo", page_icon="⚡", layout="wide")
st.markdown("""
    <style>
    .stApp { background-color: #050505; color: #e0e0e0; }
    h1 { color: #00f2ff; text-shadow: 0 0 10px #00f2ff55; }
    .stButton>button { background: linear-gradient(45deg, #00f2ff, #0072ff); color: white; border-radius: 8px; }
    </style>
    """, unsafe_allow_html=True)

st.title("⚡ HAZZ AI TURBO")
tabs = st.tabs(["💬 Chat", "🖼️ Visuals", "🎬 Motion", "🎵 Audio"])

# --- CHAT TAB (The Speed King) ---
with tabs[0]:
    user_msg = st.chat_input("Command Hazz Ai...")
    if user_msg:
        with st.chat_message("user"): st.write(user_msg)
        with st.chat_message("assistant"):
            # Streaming + 8B model = Instant typing
            response = model.generate_content(user_msg, stream=True)
            def stream_cleaner(resp):
                for chunk in resp:
                    if chunk.text: yield chunk.text
            st.write_stream(stream_cleaner(response))

# --- VISUALS TAB (Lightning Fast) ---
with tabs[1]:
    p_img = st.text_input("Describe image:")
    if st.button("Generate Image"):
        with st.spinner("Rendering..."):
            try:
                # Switching to 'lightning' model for 2-second images
                res = fal_client.subscribe("fal-ai/flux-lightning", arguments={"prompt": p_img})
                st.image(res['images'][0]['url'])
            except Exception as e: st.error(f"Error: {e}")

# --- MOTION & AUDIO (Keeping your original working code) ---
with tabs[2]:
    p_vid = st.text_input("Describe video:")
    if st.button("Generate Video"):
        with st.spinner("Processing..."):
            try:
                res = fal_client.subscribe("fal-ai/luma-dream-machine", arguments={"prompt": p_vid})
                st.video(res['video']['url'])
            except: st.error("Model busy, try again.")

with tabs[3]:
    p_aud = st.text_input("Vibe:")
    if st.button("Generate Song"):
        with st.spinner("Composing..."):
            try:
                res = fal_client.subscribe("fal-ai/stable-audio", arguments={"prompt": p_aud})
                st.audio(res['audio']['url'])
            except: st.error("Audio engine busy.")

st.divider()
st.caption("Developed by Hassan Faiz In | Turbo Mode Enabled")
