import streamlit as st
import google.generativeai as genai
import fal_client
import os

# ==========================================
# 🔑 THE BRAINS (Hardcoded for Hassan Faiz)
# ==========================================
GEMINI_KEY = "AIzaSyC7K1AkCW14bvgl5HPV4lPznnzEN1_qfSQ"
FAL_KEY = "3fc8d750-df6c-48ff-91da-ff5e4e6a99db:448b685fb163176440ba6edb57490cbe"

os.environ["FAL_KEY"] = FAL_KEY
genai.configure(api_key=GEMINI_KEY)

# ==========================================
# 🎨 FUTURISTIC UI/UX SETUP
# ==========================================
st.set_page_config(page_title="Hazz Ai | Pro Suite", page_icon="⚡", layout="wide")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&display=swap');
    .stApp { background-color: #050505; color: #e0e0e0; }
    h1, h2, h3 { font-family: 'Orbitron', sans-serif; color: #00f2ff; text-shadow: 0 0 10px #00f2ff55; }
    .stButton>button { 
        background: linear-gradient(45deg, #00f2ff, #0072ff); 
        color: white; border: none; width: 100%; font-weight: bold; border-radius: 8px;
    }
    .stTextInput>div>div>input { background-color: #111; color: white; border: 1px solid #333; }
    </style>
    """, unsafe_allow_html=True)

# Header
col1, col2 = st.columns([1, 5])
with col1:
    st.image("https://cdn-icons-png.flaticon.com/512/2103/2103633.png", width=70)
with col2:
    st.title("HAZZ AI")
    st.write("Developed by **Hassan Faiz In** | v2.0 Stable")

# ==========================================
# 🚀 CORE FEATURES
# ==========================================
tabs = st.tabs(["💬 Chat", "🖼️ Visuals", "🎬 Motion", "🎵 Audio"])

# 1. Chat
with tabs[0]:
    user_msg = st.chat_input("Command Hazz Ai...")
    if user_msg:
        with st.chat_message("user"):
            st.write(user_msg)
        with st.chat_message("assistant"):
            try:
                # Use 'gemini-1.5-flash' for maximum compatibility
                model = genai.GenerativeModel('gemini-1.5-flash')
                response = model.generate_content(user_msg)
                st.write(response.text)
            except Exception as e:
                st.error(f"Brain Error: {e}")

# 2. Images
with tabs[1]:
    prompt_img = st.text_input("Describe the image you want:")
    if st.button("Generate Image"):
        with st.spinner("Hazz Ai is rendering..."):
            try:
                res = fal_client.subscribe("fal-ai/flux/schnell", arguments={"prompt": prompt_img})
                st.image(res['images'][0]['url'])
            except Exception as e:
                st.error(f"Visual Error: {e}")

# 3. Video
with tabs[2]:
    prompt_vid = st.text_input("Describe the video scene (e.g., A drone shot of a futuristic city):")
    if st.button("Generate Video"):
        with st.spinner("Hazz Ai is processing motion..."):
            try:
                res = fal_client.subscribe("fal-ai/luma-dream-machine", arguments={"prompt": prompt_vid})
                st.video(res['video']['url'])
            except Exception as e:
                st.error(f"Motion Error: {e}")

# 4. Music
with tabs[3]:
    prompt_mus = st.text_input("Vibe (e.g., Dark cinematic techno, 120 BPM):")
    if st.button("Generate Song"):
        with st.spinner("Hazz Ai is composing..."):
            try:
                res = fal_client.subscribe("fal-ai/stable-audio", arguments={"prompt": prompt_mus})
                st.audio(res['audio']['url'])
            except Exception as e:
                st.error(f"Audio Error: {e}")

# Footer Tag
st.divider()
st.markdown("<p style='text-align: center; color: #00f2ff;'>Created by Hassan Faiz In</p>", unsafe_allow_html=True)
