import streamlit as st
import google.generativeai as genai
import fal_client
import os

# ==========================================
# 🔑 SECURE KEY LOADING (The "Secret" Way)
# ==========================================
try:
    # This pulls keys from Streamlit's private settings, NOT the code
    GEMINI_KEY = st.secrets["AIzaSyA5r1VapEiAMDSqyqroazpRMOwNr7g-TOE"]
    FAL_KEY = st.secrets["3fc8d750-df6c-48ff-91da-ff5e4e6a99db:448b685fb163176440ba6edb57490cbe"]
    
    os.environ["FAL_KEY"] = FAL_KEY
    genai.configure(api_key=GEMINI_KEY)
except Exception:
    st.error("Credential Error: Please add your API keys to Streamlit Secrets.")
    st.stop()

# 🚀 SPEED BOOST: Cache the brain so it's 0.5s fast
@st.cache_resource
def load_brain():
    return genai.GenerativeModel('gemini-3-flash-preview')

model = load_brain()

# 🎨 UI SETUP
st.set_page_config(page_title="Hazz Ai | Pro", page_icon="⚡", layout="wide")
st.title("HAZZ AI")

tabs = st.tabs(["💬 Chat", "🖼️ Visuals", "🎬 Motion", "🎵 Audio"])

# 1. Chat
with tabs[0]:
    user_msg = st.chat_input("Command Hazz Ai...")
    if user_msg:
        with st.chat_message("user"): st.write(user_msg)
        with st.chat_message("assistant"):
            # Use streaming for instant response
            response = model.generate_content(user_msg, stream=True)
            def stream_cleaner(resp):
                for chunk in resp:
                    if chunk.text: yield chunk.text
            st.write_stream(stream_cleaner(response))

# 2. Visuals
with tabs[1]:
    p_img = st.text_input("Describe image:")
    if st.button("Generate Image"):
        with st.spinner("Rendering..."):
            res = fal_client.subscribe("fal-ai/flux/schnell", arguments={"prompt": p_img})
            st.image(res['images'][0]['url'])

# 3. Motion & 4. Audio (Simplified for stability)
with tabs[2]:
    p_vid = st.text_input("Describe video:")
    if st.button("Generate Video"):
        res = fal_client.subscribe("fal-ai/luma-dream-machine", arguments={"prompt": p_vid})
        st.video(res['video']['url'])

with tabs[3]:
    p_aud = st.text_input("Vibe:")
    if st.button("Generate Song"):
        res = fal_client.subscribe("fal-ai/stable-audio", arguments={"prompt": p_aud})
        st.audio(res['audio']['url'])

st.divider()
st.caption("Developed by Hassan Faiz In | v5.0 Secure")
