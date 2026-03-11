import streamlit as st
import google.generativeai as genai
import fal_client
import os

# ==========================================
# 🔑 SECURE KEY LOADING
# ==========================================
try:
    GEMINI_API_KEY = st.secrets["AIzaSyC7K1AkCW14bvgl5HPV4lPznnzEN1_qfSQ"]
    FAL_API_KEY = st.secrets["a2aac75a-4a19-48d3-b173-f157e880cf4f:edca6bcd4136e01c369bbae968458600"]
    
    os.environ["a2aac75a-4a19-48d3-b173-f157e880cf4f:edca6bcd4136e01c369bbae968458600"] = FAL_API_KEY
    genai.configure(api_key=GEMINI_API_KEY)
except Exception as e:
    st.error("Credential Error: Please add your API keys to Streamlit Secrets.")
    st.stop()

# ==========================================
# 🎨 FUTURISTIC UI/UX DESIGN
# ==========================================
st.set_page_config(page_title="Hazz Ai Pro", page_icon="⚡", layout="wide")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&family=Inter:wght@300;600&display=swap');
    
    .stApp { background: linear-gradient(135deg, #050505 0%, #0a0a12 100%); color: #e0e0e0; font-family: 'Inter', sans-serif; }
    h1, h2, h3 { font-family: 'Orbitron', sans-serif; color: #00f2ff; text-shadow: 0 0 10px rgba(0, 242, 255, 0.4); }
    
    /* Futuristic Card Style */
    .css-1r6slb0 { background: rgba(255, 255, 255, 0.03); border: 1px solid rgba(0, 242, 255, 0.1); border-radius: 15px; padding: 20px; }
    
    /* Buttons */
    .stButton>button { 
        background: linear-gradient(90deg, #00f2ff 0%, #0072ff 100%); 
        color: white; border-radius: 8px; border: none; font-weight: bold; 
        padding: 10px 20px; transition: 0.3s;
    }
    .stButton>button:hover { transform: translateY(-2px); box-shadow: 0 5px 15px rgba(0, 242, 255, 0.4); }
    </style>
    """, unsafe_allow_html=True)

# Main Title Section
st.title("⚡ HAZZ AI")
st.markdown(f"**Creative Director:** Hassan Faiz | **System Status:** Optimal")
st.divider()

# ==========================================
# 🛰️ MULTIMODAL TABS
# ==========================================
tab_chat, tab_visual, tab_motion, tab_audio = st.tabs([
    "🧠 NEURAL CHAT", "🖼️ IMAGE ENGINE", "🎬 MOTION GEN", "🎵 SONIC LAB"
])

# --- 1. NEURAL CHAT ---
with tab_chat:
    if "messages" not in st.session_state:
        st.session_state.messages = []
    
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    if prompt := st.chat_input("Input command for Hazz Ai..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            try:
                model = genai.GenerativeModel('gemini-1.5-flash')
                response = model.generate_content(prompt)
                st.markdown(response.text)
                st.session_state.messages.append({"role": "assistant", "content": response.text})
            except Exception as e:
                st.error("Neural link failed. Check Gemini API credits.")

# --- 2. IMAGE ENGINE ---
with tab_visual:
    st.subheader("Generate Visual Assets")
    img_p = st.text_area("Art Prompt:", placeholder="E.g. Futuristic cinematic portrait, 8k resolution...")
    if st.button("INITIATE RENDERING"):
        with st.spinner("Synthesizing..."):
            try:
                res = fal_client.subscribe("fal-ai/flux/schnell", arguments={"prompt": img_p})
                st.image(res['images'][0]['url'], use_container_width=True)
            except:
                st.error("Visualization error. Check Fal.ai Key.")

# --- 3. MOTION GEN ---
with tab_motion:
    st.subheader("Cinematic Video Generator")
    vid_p = st.text_area("Scene Description:", placeholder="E.g. A neon-lit street in 2077, drone shot...")
    if st.button("START MOTION RENDER"):
        with st.spinner("Processing temporal frames..."):
            try:
                res = fal_client.subscribe("fal-ai/luma-dream-machine", arguments={"prompt": vid_p})
                st.video(res['video']['url'])
            except:
                st.error("Server high load. Try again.")

# --- 4. SONIC LAB ---
with tab_audio:
    st.subheader("AI Audio Composition")
    aud_p = st.text_input("Vibe:", placeholder="E.g. High-energy cinematic trailer music, 140 BPM...")
    if st.button("COMPOSE AUDIO"):
        with st.spinner("Orchestrating..."):
            try:
                res = fal_client.subscribe("fal-ai/stable-audio", arguments={"prompt": aud_p})
                st.audio(res['audio']['url'])
            except:
                st.error("Audio engine busy.")

# ==========================================
# 🏷️ FOOTER
# ==========================================
st.markdown("---")
col_l, col_r = st.columns(2)
with col_l:
    st.caption("© 2026 Hazz Ai Creative Suite")
with col_r:
    st.markdown("<p style='text-align: right; color: #00f2ff;'><b>Hassan Faiz In</b></p>", unsafe_allow_html=True)
