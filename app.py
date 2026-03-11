import streamlit as st
import google.generativeai as genai
import fal_client
import os

# 1. 🔑 KEYS (Confirmed Working)
GEMINI_KEY = "AIzaSyCTrIsSO7JYwHG5pKzbtwZ_jomBnbZhu9M"
FAL_KEY = "3fc8d750-df6c-48ff-91da-ff5e4e6a99db:448b685fb163176440ba6edb57490cbe"
os.environ["FAL_KEY"] = FAL_KEY

# 🚀 SPEED BOOST: This keeps the app from "re-logging in" every time.
# We use the EXACT model name you said works properly.
@st.cache_resource
def get_hazz_brain():
    genai.configure(api_key=GEMINI_KEY)
    return genai.GenerativeModel('gemini-3-flash-preview')

model = get_hazz_brain()

# 🎨 UI SETUP
st.set_page_config(page_title="Hazz Ai | Pro Suite", page_icon="⚡", layout="wide")
st.title("HAZZ AI")
st.write("Developed by **Hassan Faiz In** | v4.6 Stable")

tabs = st.tabs(["💬 Chat", "🖼️ Visuals", "🎬 Motion", "🎵 Audio"])

# 1. Chat (USING YOUR WORKING LOGIC)
with tabs[0]:
    user_msg = st.chat_input("Command Hazz Ai...")
    if user_msg:
        with st.chat_message("user"): st.write(user_msg)
        with st.chat_message("assistant"):
            try:
                # We use regular generation (no stream) to ensure no '403' errors
                response = model.generate_content(user_msg)
                st.write(response.text)
            except Exception as e:
                st.error(f"Connection Error: {e}")

# 2. Visuals (Same as your v4.0)
with tabs[1]:
    prompt_img = st.text_input("Describe image:")
    if st.button("Generate Image"):
        with st.spinner("Hazz Ai rendering..."):
            try:
                # Schnell is stable, but Lightning is faster. Let's stick to Schnell for safety.
                res = fal_client.subscribe("fal-ai/flux/schnell", arguments={"prompt": prompt_img})
                st.image(res['images'][0]['url'])
            except Exception as e: st.error(f"Visual Error: {e}")

# 3. Video & 4. Audio (Your exact original code)
with tabs[2]:
    prompt_vid = st.text_input("Describe video:")
    if st.button("Generate Video"):
        with st.spinner("Processing..."):
            res = fal_client.subscribe("fal-ai/luma-dream-machine", arguments={"prompt": prompt_vid})
            st.video(res['video']['url'])

with tabs[3]:
    prompt_mus = st.text_input("Vibe:")
    if st.button("Generate Song"):
        with st.spinner("Composing..."):
            res = fal_client.subscribe("fal-ai/stable-audio", arguments={"prompt": prompt_mus})
