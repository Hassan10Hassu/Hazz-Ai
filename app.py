import streamlit as st
import google.generativeai as genai
import fal_client
import os

# ==========================================
# 🔑 THE BRAINS (Hardcoded for Hassan Faiz)
# ==========================================
GEMINI_KEY = "AIzaSyCTrIsSO7JYwHG5pKzbtwZ_jomBnbZhu9M"
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
    </style>
    """, unsafe_allow_html=True)

# Header
col1, col2 = st.columns([1, 5])
with col1:
    st.image("https://cdn-icons-png.flaticon.com/512/2103/2103633.png", width=70)
with col2:
    st.title("HAZZ AI")
    st.write("Developed by **Hassan Faiz In** | v4.0 Final")

# ==========================================
# 🚀 CORE FEATURES (Defining Tabs First!)
# ==========================================
# IMPORTANT: We define 'tabs' HERE so they exist for the code below
tabs = st.tabs(["💬 Chat", "🖼️ Visuals", "🎬 Motion", "🎵 Audio"])

# 1. Chat (CLEAN & FAST)
with tabs[0]:
    user_msg = st.chat_input("Command Hazz Ai...")
    if user_msg:
        with st.chat_message("user"):
            st.write(user_msg)
        
        with st.chat_message("assistant"):
            try:
                model = genai.GenerativeModel('gemini-3-flash-preview')
                
                # We use streaming for speed
                response = model.generate_content(user_msg, stream=True)
                
                # This helper extracts ONLY the text from the technical data
                def stream_text(response_iterator):
                    for chunk in response_iterator:
                        # Only yield the text part of the chunk
                        if chunk.text:
                            yield chunk.text

                # Display the cleaned text word-by-word
                st.write_stream(stream_text(response))
                
            except Exception as e:
                st.error(f"Neural Error: {e}")
# 2. Images
with tabs[1]:
    prompt_img = st.text_input("Describe image:")
    if st.button("Generate Image"):
        with st.spinner("Hazz Ai rendering..."):
            try:
                res = fal_client.subscribe("fal-ai/flux/schnell", arguments={"prompt": prompt_img})
                st.image(res['images'][0]['url'])
            except Exception as e:
                st.error(f"Visual Error: {e}")

# 3. Video
with tabs[2]:
    prompt_vid = st.text_input("Describe video:")
    if st.button("Generate Video"):
        with st.spinner("Hazz Ai processing..."):
            try:
                res = fal_client.subscribe("fal-ai/luma-dream-machine", arguments={"prompt": prompt_vid})
                st.video(res['video']['url'])
            except Exception as e:
                st.error(f"Motion Error: {e}")

# 4. Music
with tabs[3]:
    prompt_mus = st.text_input("Vibe:")
    if st.button("Generate Song"):
        with st.spinner("Hazz Ai composing..."):
            try:
                res = fal_client.subscribe("fal-ai/stable-audio", arguments={"prompt": prompt_mus})
                st.audio(res['audio']['url'])
            except Exception as e:
                st.error(f"Audio Error: {e}")

st.divider()
st.markdown("<p style='text-align: center; color: #00f2ff;'>Created by Hassan Faiz In</p>", unsafe_allow_html=True)
