import streamlit as st
import google.generativeai as genai
import fal_client
import os

# 🔑 Setup
GEMINI_KEY = "AIzaSyCTrIsSO7JYwHG5pKzbtwZ_jomBnbZhu9M"
FAL_KEY = "3fc8d750-df6c-48ff-91da-ff5e4e6a99db:448b685fb163176440ba6edb57490cbe"
os.environ["FAL_KEY"] = FAL_KEY

# 🚀 SPEED BOOST 1: Cache the Model Connection
@st.cache_resource
def get_model():
    genai.configure(api_key=GEMINI_KEY)
    return genai.GenerativeModel('gemini-3-flash-preview')

model = get_model() # This is now instant after the first run

# 🎨 UI Setup
st.set_page_config(page_title="Hazz Ai | Pro Suite", page_icon="⚡", layout="wide")
st.title("HAZZ AI")

tabs = st.tabs(["💬 Chat", "🖼️ Visuals", "🎬 Motion", "🎵 Audio"])

# 1. Chat (Streaming + Clean Filter)
with tabs[0]:
    user_msg = st.chat_input("Command Hazz Ai...")
    if user_msg:
        with st.chat_message("user"): st.write(user_msg)
        with st.chat_message("assistant"):
            try:
                # Streaming makes the response FEEL instant
                response = model.generate_content(user_msg, stream=True)
                def stream_cleaner(resp):
                    for chunk in resp:
                        if chunk.text: yield chunk.text
                st.write_stream(stream_cleaner(response))
            except Exception as e: st.error(f"Error: {e}")

# 2. Visuals (SPEED BOOST 2: Using Lightning Model)
with tabs[1]:
    p_img = st.text_input("Quick Render Prompt:")
    if st.button("RENDER (2s)"):
        with st.spinner("Lighting fast render..."):
            try:
                # Flux Lightning is 5x faster than Flux Schnell
                res = fal_client.subscribe("fal-ai/flux-lightning", arguments={"prompt": p_img})
                st.image(res['images'][0]['url'])
            except Exception as e: st.error(f"Error: {e}")

# 3. Motion & 4. Audio stay the same (Luma and Stable Audio take time by nature)
