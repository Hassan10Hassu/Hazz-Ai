# 1. Chat (Updated for 2026 Models)
with tabs[0]:
    user_msg = st.chat_input("Command Hazz Ai...")
    if user_msg:
        with st.chat_message("user"):
            st.write(user_msg)
        with st.chat_message("assistant"):
            # Try the newest 2026 models
            models_to_try = [
                'gemini-3-flash-preview', 
                'gemini-2.5-flash', 
                'gemini-2.0-flash'
            ]
            success = False
            
            for model_name in models_to_try:
                try:
                    model = genai.GenerativeModel(model_name)
                    response = model.generate_content(user_msg)
                    st.write(response.text)
                    success = True
                    break 
                except Exception:
                    continue 
            
            if not success:
                st.error("Neural path blocked. Please verify your API Key has 'Generative Language API' enabled in Google AI Studio.")
