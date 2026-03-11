import streamlit as st
import google.generativeai as genai
import fal_client
import os

# ==========================================
# 🔑 SECURE KEY LOADING (Safe for Public Use)
# ==========================================
try:
    # This looks for keys in your Streamlit Settings -> Secrets
    GEMINI_KEY = st.secrets["GEMINI_API_KEY"]
    FAL_KEY = st.secrets["FAL_API_KEY"]
    
    os.environ["FAL_KEY"] = FAL_KEY
    genai.configure(api_key=GEMINI_KEY)
    app_status = "🟢 ONLINE"
except Exception:
    app_status = "🔴 OFFLINE (Check Secrets)"
    st.error("Credential Error: Please add your API keys to Streamlit Secrets.")
    st.stop()

# ==========================================
# 🎨 FUTURISTIC UI/UX SETUP
# ==========================================
st.set_page_config(page_title="Hazz Ai | Pro Suite", page_icon="⚡", layout="wide")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&display=swap');
    .stApp { background-color: #050505; color: #e0e0e0; }
    h1, h2, h3 { font-family: 'Orbitron', sans-serif; color: #00f2ff; text-shadow: 0 0 10px #00f2ff22; }
    .stButton>button { 
        background: linear-gradient(45deg, #00f2ff, #0072ff); 
        color: white; border: none; width: 100%; font-weight: bold; border-radius: 8px; transition: 0.3s;
    }
    .stButton>button:hover { transform: scale(1.02); box-shadow: 0 0 15px #00f2ff; }
    </style>
    """, unsafe_allow_html=True)

# Header with Status
col1, col2 = st.columns([4, 1])
with col1:
    st.title("HAZZ AI")
    st.markdown(f"**Creative Director:** Hassan Faiz In")
with col2:
    st.markdown(f"<p style='text-align: right; color: #00f2ff;'>{app_status}</p>", unsafe_allow_html=True)

st.divider()

# ==========================================
# 🛰️ MULTIMODAL TABS
# ==========================================
tabs = st.tabs(["💬 Chat", "🖼️ Visuals", "🎬 Motion", "🎵 Audio"])

# 1. Chat
with tabs[0]:
    user_msg = st.chat_input("Command Hazz Ai...")
    if user_msg:
        with st.chat_message("user"): st.write(user_msg)
        with st.chat_message("assistant"):
            try:
                # Using the 2026 stable identifier
               # Updated for March 2026 stable endpoints
model = genai.GenerativeModel('gemini-3-flash-preview')
                response = model.generate_content(user_msg)
                st.write(response.text)
            except Exception as e:
                st.error(f"Neural Error: {e}")

# 2. Visuals (Image Generation)
with tabs[1]:
    p_img = st.text_input("Describe the image you want:")
    if st.button("RENDER IMAGE"):
        with st.spinner("Processing..."):
            try:
                res = fal_client.subscribe("fal-ai/flux/schnell", arguments={"prompt": p_img})
                st.image(res['images'][0]['url'])
            except Exception as e: st.error(f"Error: {e}")

# 3. Motion (Video Generation)
with tabs[2]:
    p_vid = st.text_input("Describe the video scene:")
    if st.button("GENERATE VIDEO"):
        with st.spinner("Processing motion..."):
            try:
                res = fal_client.subscribe("fal-ai/luma-dream-machine", arguments={"prompt": p_vid})
                st.video(res['video']['url'])
            except Exception as e: st.error(f"Error: {e}")

# 4. Audio (Music Generation)
with tabs[3]:
    p_aud = st.text_input("Vibe (e.g. Cinematic cinematic trailer):")
    if st.button("COMPOSE MUSIC"):
        with st.spinner("Orchestrating..."):
            try:
                res = fal_client.subscribe("fal-ai/stable-audio", arguments={"prompt": p_aud})
                st.audio(res['audio']['url'])
            except Exception as e: st.error(f"Error: {e}")

# Footer
st.divider()
st.markdown("<p style='text-align: center; color: #888;'>Hazz Ai Pro Suite © 2026</p>", unsafe_allow_html=True)
