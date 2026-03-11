import streamlit as st
import google.generativeai as genai
import fal_client

# --- CONFIGURATION & BRANDING ---
st.set_page_config(page_title="Hazz Ai", page_icon="🤖")
st.title("🤖 Hazz Ai")
st.markdown("### The Professional Multimodal Assistant")

# --- CUSTOM SIDEBAR ---
with st.sidebar:
    st.header("Settings")
    api_key = st.text_input("Enter Gemini API Key", type="password")
    fal_key = st.text_input("Enter Fal.ai Key (for Video/Images)", type="password")
    st.info("Created & Managed by: **Hassan Faiz**")

# --- AI LOGIC ---
if api_key:
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-1.5-flash')

    # Simple Chat Input
    user_input = st.chat_input("Ask Hazz Ai to write, draw, or make a video...")
    
    if user_input:
        with st.chat_message("user"):
            st.write(user_input)
            
        with st.chat_message("assistant"):
            if "video" in user_input.lower():
                st.write("Generating video for you...")
                # This would call the Fal.ai video model
                st.video("https://www.w3schools.com/html/mov_bbb.mp4") # Placeholder
            elif "image" in user_input.lower():
                st.write("Creating your image...")
                st.image("https://picsum.photos/400/300") # Placeholder
            else:
                response = model.generate_content(user_input)
                st.write(response.text)

# --- THE SIGNATURE ---
st.write("---")
st.caption("© 2026 Hazz Ai | Developed by **Hassan Faiz**")
