import streamlit as st
import google.generativeai as genai
import fal_client
import os

# ==========================================
# 🔑 THE BRAINS
# ==========================================
GEMINI_KEY = "AIzaSyAMwUMCWiRA0PMwUGcBBTL23srBgVtEgTg"
FAL_KEY = "3fc8d750-df6c-48ff-91da-ff5e4e6a99db:448b685fb163176440ba6edb57490cbe"

os.environ["FAL_KEY"] = FAL_KEY

@st.cache_resource
def load_model():
    genai.configure(api_key=GEMINI_KEY)
    # Use the 2026 workhorse model
    return genai.GenerativeModel('gemini-3-flash-preview')

model = load_model()

# ==========================================
# 🎨 PROFESSIONAL UI/UX INJECTION
# ==========================================
st.set_page_config(
    page_title="Hazz AI | Pro Suite", 
    page_icon="https://img.sanishtech.com/u/86b88fbb3abf4ebc53d5e5c1ad3f4b03.png", 
    layout="wide"
)

# Custom CSS for Professional Dark Mode & Branding
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800&display=swap');
    
    /* Main Background */
    .stApp {
        background: radial-gradient(circle at 20% 10%, #111827 0%, #000000 100%);
        color: #f3f4f6;
        font-family: 'Inter', sans-serif;
    }

    /* Sidebar / Glassmorphism Tabs */
    .stTabs [data-baseweb="tab-list"] {
        gap: 10px;
        background-color: transparent;
    }

    .stTabs [data-baseweb="tab"] {
        height: 50px;
        white-space: pre-wrap;
        background-color: rgba(255, 255, 255, 0.05);
        border-radius: 12px;
        color: white;
        border: 1px solid rgba(255, 255, 255, 0.1);
        padding: 10px 20px;
        transition: all 0.3s;
    }

    .stTabs [aria-selected="true"] {
        background: linear-gradient(135deg, #6366f1 0%, #a855f7 100%) !important;
        border: none !important;
    }

    /* Professional Buttons */
    .stButton>button {
        background: linear-gradient(90deg, #6366f1, #a855f7);
        color: white;
        border: none;
        border-radius: 12px;
        padding: 12px 24px;
        font-weight: 600;
        letter-spacing: 0.5px;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        width: 100%;
    }

    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 10px 20px -10px rgba(99, 102, 241, 0.5);
    }

    /* Logo Glow */
    .brand-logo {
        filter: drop-shadow(0 0 10px rgba(99, 102, 241, 0.4));
        border-radius: 15px;
    }
    
    /* Header Text */
    .hazz-title {
        font-weight: 800;
        background: linear-gradient(to right, #fff, #94a3b8);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        letter-spacing: -1px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- Header Section ---
col1, col2 = st.columns([1, 8])
with col1:
    st.image("https://img.sanishtech.com/u/86b88fbb3abf4ebc53d5e5c1ad3f4b03.png", width=80)
with col2:
    st.markdown('<h1 class="hazz-title">HAZZ AI</h1>', unsafe_allow_html=True)
    st.write("Professional Creative Suite | Powering Digital Innovation")

st.divider()

# ==========================================
# 🚀 CORE FEATURES
# ==========================================
tabs = st.tabs(["💬 Assistant", "🎨 Image Studio", "🎥 Motion Pro", "🎵 Audio Lab"])

# 1. Chat (CLEAN & FAST)
with tabs[0]:
    user_msg = st.chat_input("Command Hazz AI...")
    if user_msg:
        with st.chat_message("user"):
            st.write(user_msg)
        
        with st.chat_message("assistant", avatar="https://img.sanishtech.com/u/86b88fbb3abf4ebc53d5e5c1ad3f4b03.png"):
            try:
                response = model.generate_content(user_msg, stream=True)
                
                def stream_text(response_iterator):
                    for chunk in response_iterator:
                        if chunk.text:
                            yield chunk.text

                st.write_stream(stream_text(response))
                
            except Exception as e:
                st.error(f"Neural Error: {e}")

# 2. Images (Visual Studio)
with tabs[1]:
    st.subheader("Visual Engine")
    prompt_img = st.text_input("Describe your visual concept:", placeholder="Cinematic portrait, 8k, highly detailed...")
    if st.button("Generate Masterpiece"):
        with st.spinner("Hazz AI is rendering..."):
            try:
                res = fal_client.subscribe("fal-ai/flux/schnell", arguments={"prompt": prompt_img})
                st.image(res['images'][0]['url'], use_container_width=True)
            except Exception as e:
                st.error(f"Visual Error: {e}")

# 3. Video (Motion Pro)
with tabs[2]:
    st.subheader("Motion Engine")
    prompt_vid = st.text_input("Describe the motion:", placeholder="Slow pan of a futuristic city...")
    if st.button("Render Motion"):
        with st.spinner("Processing cinematic frames..."):
            try:
                res = fal_client.subscribe("fal-ai/luma-dream-machine", arguments={"prompt": prompt_vid})
                st.video(res['video']['url'])
            except Exception as e:
                st.error(f"Motion Error: {e}")

# 4. Music (Audio Lab)
with tabs[3]:
    st.subheader("Audio Synthesis")
    prompt_mus = st.text_input("Vibe or Genre:", placeholder="Cyberpunk synthwave, 120bpm...")
    if st.button("Synthesize Audio"):
        with st.spinner("Composing original score..."):
            try:
                res = fal_client.subscribe("fal-ai/stable-audio", arguments={"prompt": prompt_mus})
                st.audio(res['audio']['url'])
            except Exception as e:
                st.error(f"Audio Error: {e}")

# Footer
st.markdown("<br><hr><p style='text-align: center; color: #4b5563; font-size: 0.8rem;'>© 2026 Hazz AI | Developed by Hassan Faiz</p>", unsafe_allow_html=True)
