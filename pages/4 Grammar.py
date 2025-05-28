import streamlit as st
import pyttsx3
import re

# Function to convert text to speech
def text_to_speech(sentence):
    engine = pyttsx3.init()
    engine.say(sentence)
    engine.runAndWait()

# Function to split text into sentences
def split_text_into_sentences(text):
    return re.split(r'(?<=[.!?]) +', text)

# Main function for the Streamlit app
def main():
    st.title("🌱 Vocabulary Learning")

    # Define tabs
    tab1, tab2, tab3, tab4 = st.tabs(["❄️ Read after TTS", "❄️ Tab 2", "❄️ Tab 3", "❄️ Tab 4"])

    # Content for the first tab
    with tab1:
        st.header("Sentence-by-Sentence Text-to-Speech")

        # Input text area
        text = st.text_area("Enter the text you want to study", height=200)

        if text:
            # Split the text into sentences
            sentences = split_text_into_sentences(text)
            
            # Display the sentences with a selectbox
            sentence_index = st.selectbox("Select a sentence to listen to", range(len(sentences)), format_func=lambda x: sentences[x])
            
            # Button to play selected sentence
            if st.button("Play Selected Sentence"):
                text_to_speech(sentences[sentence_index])
                st.write(f"Playing: {sentences[sentence_index]}")

if __name__ == "__main__":
    main()

streamlit run app.py

with tab2:
  st.header("dd")

with tab3:
  st.header("dd")
