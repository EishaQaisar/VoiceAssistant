import streamlit as st
import speech_recognition as sr
from main import execute_command

# Streamlit UI Configuration
st.set_page_config(page_title="AI Voice Assistant", page_icon="🎙️", layout="wide")

# Custom Styles
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Poppins', sans-serif;
    }
    .stApp {
        background: linear-gradient(135deg, #1e1e2e, #2a2a40);
    }
    .main-container {
        background: rgba(255, 255, 255, 0.1);
        padding: 2rem;
        border-radius: 15px;
        box-shadow: 0 10px 20px rgba(0, 0, 0, 0.2);
    }
    .title {
        color: #f8f9fa;
        font-size: 3rem;
        font-weight: 600;
        text-align: center;
        text-shadow: 2px 2px 5px rgba(0,0,0,0.3);
    }
    .subtitle {
        color: #b3b3b3;
        font-size: 1.2rem;
        text-align: center;
    }
    .stButton>button {
        background: linear-gradient(45deg, #ff6b6b, #ffcc5c);
        color: white;
        font-size: 1.2rem;
        font-weight: 600;
        padding: 0.8rem 2rem;
        border-radius: 50px;
        box-shadow: 0 4px 10px rgba(0,0,0,0.3);
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        transform: scale(1.05);
        box-shadow: 0 6px 15px rgba(0,0,0,0.4);
        background: linear-gradient(45deg, #ffcc5c, #ff6b6b);
    }
    .status {
        font-size: 1.2rem;
        text-align: center;
        margin: 1rem 0;
        color: #ffffff;
        font-weight: 600;
    }
    .output-container {
        background-color: rgba(255, 255, 255, 0.15);
        padding: 1.5rem;
        border-radius: 10px;
        margin-top: 1.5rem;
        color: #ffffff;
        text-align: center;
    }
    .footer {
        text-align: center;
        margin-top: 3rem;
        color: #808080;
        font-size: 0.9rem;
    }
    .sidebar-content {
        background: linear-gradient(135deg, #ff914d, #ffcc5c);
        padding: 1.5rem;
        border-radius: 15px;
        color: white;
        text-align: center;
        font-weight: 600;
        font-size: 1.2rem;
        box-shadow: 0 4px 10px rgba(0,0,0,0.3);
    }
    .sidebar-instructions {
        background: rgba(255, 255, 255, 0.1);
        padding: 1rem;
        border-radius: 10px;
        color: #fff;
        text-align: left;
        font-size: 1rem;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Sidebar Menu
st.sidebar.markdown('<div class="sidebar-content">📌 Instructions</div>', unsafe_allow_html=True)
st.sidebar.markdown('<div class="sidebar-instructions">', unsafe_allow_html=True)
st.sidebar.write("✔ Click the 'Start Listening' button to begin.")
st.sidebar.write("✔ Speak clearly into your microphone.")
st.sidebar.write("✔ Wait for the assistant to process and respond.")
st.sidebar.write("✔ If there's an issue, check your internet connection.")
st.sidebar.markdown('</div>', unsafe_allow_html=True)

# Main Content
st.markdown('<h1 style="color: #e0e0e0; text-align: center;">🎙️ AI Voice Assistant</h1>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Your intelligent voice-powered companion</p>', unsafe_allow_html=True)

col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    if st.button("🎤 Start Listening", use_container_width=True):
        st.markdown('<div class="status">🎙️ Listening...</div>', unsafe_allow_html=True)
        
        recognizer = sr.Recognizer()
        with sr.Microphone() as source:
            recognizer.adjust_for_ambient_noise(source)
            try:
                audio = recognizer.listen(source)
                command = recognizer.recognize_google(audio)
                
                st.markdown(f'<div class="output-container">🗣️ You said: <strong>{command}</strong></div>', unsafe_allow_html=True)
                response = execute_command(command)
                st.markdown(f'<div class="output-container">🤖 Assistant: <strong>{response}</strong></div>', unsafe_allow_html=True)
                
            except sr.UnknownValueError:
                st.warning("🤔 Sorry, I couldn't understand.")
            except sr.RequestError:
                st.error("⚠️ Could not request results. Check your internet connection.")

# Footer
st.markdown("""
    <div class="footer">
        <p>Powered by AI | Created with ❤️</p>
    </div>
""", unsafe_allow_html=True)
