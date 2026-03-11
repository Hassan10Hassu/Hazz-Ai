import streamlit as st
import google.generativeai as genai
import fal_client
import os

# 1. 🔑 KEYS (Your Working Keys)
GEMINI_KEY = "AIzaSyCTrIsSO7JYwHG5pKzbtwZ_jomBnbZhu9M"
FAL_KEY = "3fc8d750-df6c-48ff-91da-ff5e4e6a99db:448b685fb163176440ba6edb57490cbe"
os.environ["FAL_KEY"] = FAL_KEY

# 🚀 THE SPEED FIX: This function runs ONCE and stays in memory.
@st.cache_resource
def load_brain():
    genai.configure(api_key=GEMINI_KEY)
    # Using the name you confirmed works:
    return genai.GenerativeModel('gemini-3-flash-preview')

model = load_brain()

# 🎨 UI SETUP (Your Professional Theme)
st.set_page_config(page_title="Hazz Ai | Pro", page_icon="⚡", layout="wide")
st.markdown("""
    <style>
    .stApp { background-color: #050505; color: #e0e0e0; }
    h1 { color: #00f2ff; text-shadow: 0 0 10px #00f2ff55; }
    .stButton>button { background: linear-gradient(45deg, #00f2ff, #0072ff); color: white; border-radius: 8px; }
    </style>
    """, unsafe_allow_html=True)

st.title("HAZZ AI")
tabs = st.tabs(["💬 Chat", "🖼️ Visuals", "🎬 Motion", "🎵 Audio"])

# 1. Chat (Streaming for speed, but using your working model)
with tabs[0]:
    user_msg = st.chat_input("Command Hazz Ai...")
    if user_msg:
        with st.chat_message("user"): st.write(user_msg)
        with st.chat_message("assistant"):
            try:
                # stream=True makes it feel much faster
                response = model.generate_content(user_msg, stream=True)
                def clean_stream(stream):
                    for chunk in stream:
                        if chunk.text: yield chunk.text
                st.write_stream(clean_stream(response))
            except Exception as e:
                # If streaming fails, we do a normal fast response
                res = model.generate_content(user_msg)
                st.write(res.text)

# 2. Visuals (Switching back to your original working model but faster version)
with tabs[1]:
    p_img = st.text_input("Describe image:")
    if st.button("Generate Image"):
        with st.spinner("Rendering..."):
            try:
                # 'flux-lightning' is the fast version of 'flux-schnell'
                res = fal_client.subscribe("fal-ai/flux-lightning", arguments={"prompt": p_img})
                st.image(res['images'][0]['url'])
            except:
                # Fallback to your old one if lightning fails
                res = fal_client.subscribe("fal-ai/flux/schnell", arguments={"prompt": p_img})
                st.image(res['images'][0]['url'])

# 3. Video & 4. Audio (Keeping your exact working code)
with tabs[2]:
    p_vid = st.text_input("Describe video:")
    if st.button("Generate Video"):
        with st.spinner("Processing..."):
            res = fal_client.subscribe("fal-ai/luma-dream-machine", arguments={"prompt": p_vid})
            st.video(res['video']['url'])

with tabs[3]:
    p_aud = st.text_input("Vibe:")
    if st.button("Generate Song"):
        with st.spinner("Composing..."):
            res = fal_client.subscribe("fal-ai/stable-audio", arguments={"prompt": p_aud})
            st.audio(res['audio']['url'])

st.divider()
st.caption("Developed by Hassan Faiz In | v4.5 Optimized")
