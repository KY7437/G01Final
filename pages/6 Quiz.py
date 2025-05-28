import streamlit as st
import pandas as pd
from gtts import gTTS
from io import BytesIO
import random
import tempfile

st.write("Review Check")

# Define tabs
tab1, tab2, tab3 = st.tabs(["❄️ Level 1", "❄️ Level 2", "❄️ Level 3"])

with tab1:
    st.header("Level 1 Content")
    st.write("This is where you can put content for Level 1.")
    # Example: Add a simple interactive element
    if st.button("Say Hello"):
        st.write("Hello from Level 1!")

with tab2:
    st.header("Level 2 Content")
    st.write("This is where you can put content for Level 2.")
    # Example: Display a random number
    if st.button("Generate Random Number"):
        number = random.randint(1, 100)
        st.write(f"Random Number: {number}")

with tab3:
    st.header("Level 3 Content")
    st.write("This is where you can put content for Level 3.")
    # Example: Text-to-Speech functionality
    text = st.text_input("Enter text for TTS:", "Hello, Streamlit!")
    if st.button("Generate TTS"):
        tts = gTTS(text)
        tts_bytes = BytesIO()
        tts.write_to_fp(tts_bytes)
        tts_bytes.seek(0)
        st.audio(tts_bytes, format="audio/mp3")
