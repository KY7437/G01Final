import streamlit as st
from gtts import gTTS
from io import BytesIO

st.title("Passage Reading")

# Define tabs
tab1, tab2, tab3 = st.tabs(["🍃 TTS", "🍃 2. gg", "🍃 3. gg"])

with tab1:
    url = "https://github.com/KY7437/G01Final/raw/main/data/story01.png"
    st.image(url, caption="Lesson 1", width=500)  # width in pixels

    # Function to convert text to speech
    def text_to_speech(text):
        tts = gTTS(text, lang='en')
        audio_bytes = BytesIO()
        tts.write_to_fp(audio_bytes)
        audio_bytes.seek(0)
        return audio_bytes

    # Predefined text
    predefined_text = """
    In the small town of Willowby, there stood an old library that was rumored to be enchanted. Every night at midnight, the books inside would whisper stories to each other, bringing their characters to life. One evening, Sarah, a curious 15-year-old book lover, decided to sneak into the library to see if the rumors were true. As the clock struck twelve, the books began to rustle. To Sarah's amazement, characters stepped out of their pages. She met Alice from Wonderland, the White Rabbit, and even pirates from Treasure Island. They invited her to join their midnight council, where they discussed the tales of their adventures and the wisdom they contained. Sarah spent the whole night listening and learning from the characters, promising to keep their secret. As dawn approached, they returned to their pages. Sarah left the library, inspired and filled with stories to tell, forever changed by the magic of the Midnight Library.
    """

    # Initialize session state for buttons
    if 'play_audio' not in st.session_state:
        st.session_state.play_audio = False
    if 'show_text' not in st.session_state:
        st.session_state.show_text = False

    # Button to play the audio for the predefined text
    if st.button("Play TTS"):
        st.session_state.play_audio = True

    # Button to show the text
    if st.button("Show Text"):
        st.session_state.show_text = not st.session_state.show_text  # Toggle text visibility

    # Play audio if the button has been pressed
    if st.session_state.play_audio:
        audio_bytes = text_to_speech(predefined_text)
        st.audio(audio_bytes, format="audio/mp3")
        # Reset audio state to prevent replay on refresh
        st.session_state.play_audio = False

    # Display text if the button has been pressed
    if st.session_state.show_text:
        st.write(predefined_text)

with tab2:
    import streamlit as st
from gtts import gTTS
import os
import re
import tempfile

# Function to split text into sentences
def split_text_into_sentences(text):
    return re.split(r'(?<=[.!?]) +', text)

# Sample passage
passage = """
In the small town of Willowby, there stood an old library that was rumored to be enchanted. 
Every night at midnight, the books inside would whisper stories to each other, bringing their characters to life. 
One evening, Sarah, a curious 15-year-old book lover, decided to sneak into the library to see if the rumors were true.

As the clock struck twelve, the books began to rustle. 
To Sarah's amazement, characters stepped out of their pages. 
She met Alice from Wonderland, the White Rabbit, and even pirates from Treasure Island. 
They invited her to join their midnight council, where they discussed the tales of their adventures and the wisdom they contained.

Sarah spent the whole night listening and learning from the characters, promising to keep their secret. 
As dawn approached, they returned to their pages. 
Sarah left the library, inspired and filled with stories to tell, forever changed by the magic of the Midnight Library.
"""

# Split passage into sentences
sentences = split_text_into_sentences(passage)

# Initialize session state for index
if 'index' not in st.session_state:
    st.session_state.index = 0

# Function to generate TTS for the current sentence
def get_tts():
    sentence = sentences[st.session_state.index]
    tts = gTTS(text=sentence, lang='en')
    tts.save("output.mp3")
    return sentence

# Main function for the Streamlit app
def main():
    st.title("Grammar")

    # Define tabs
    tab1, tab2, tab3, tab4 = st.tabs(["🍃 Read after TTS", "🍃 Role Play", "🍃 Tab 3", "🍃 Tab 4"])

    # Content for the first tab
    with tab2:
        st.header("Sentence by Sentence TTS Reader")

        # Display current sentence
        sentence = get_tts()
        st.text_area("Current Sentence", value=sentence, height=100)

        # Play audio
        audio_file = open("output.mp3", "rb")
        audio_bytes = audio_file.read()
        st.audio(audio_bytes, format="audio/mp3")

        # Navigation buttons
        col1, col2 = st.columns(2)
        with col1:
            if st.button("◀ Previous") and st.session_state.index > 0:
                st.session_state.index -= 1
        with col2:
            if st.button("Next ▶") and st.session_state.index < len(sentences) - 1:
                st.session_state.index += 1
with tab3:
    st.write("R")
