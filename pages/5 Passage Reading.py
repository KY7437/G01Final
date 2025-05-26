import streamlit as st
from gtts import gTTS
import os

# Function to convert text to speech and return audio file path
def text_to_speech(text, filename="output.mp3"):
    tts = gTTS(text, lang='en')
    tts.save(filename)
    return filename

# Set up Streamlit app
st.title("Text-to-Speech App")

# Predefined text
predefined_text = """
In the small town of Willowby, there stood an old library that was rumored to be enchanted. Every night at midnight, the books inside would whisper stories to each other, bringing their characters to life. One evening, Sarah, a curious 15-year-old book lover, decided to sneak into the library to see if the rumors were true. As the clock struck twelve, the books began to rustle. To Sarah's amazement, characters stepped out of their pages. She met Alice from Wonderland, the White Rabbit, and even pirates from Treasure Island. They invited her to join their midnight council, where they discussed the tales of their adventures and the wisdom they contained. Sarah spent the whole night listening and learning from the characters, promising to keep their secret. As dawn approached, they returned to their pages. Sarah left the library, inspired and filled with stories to tell, forever changed by the magic of the Midnight Library.
"""

# Convert predefined text to speech and save to file
audio_file = text_to_speech(predefined_text)

# Button to play the audio
if st.button("Play TTS"):
    # Use Streamlit's audio component to play the audio file
    audio_bytes = open(audio_file, "rb").read()
    st.audio(audio_bytes, format="audio/mp3")

# Clean up by removing the audio file
os.remove(audio_file)
