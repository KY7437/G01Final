import streamlit as st
from gtts import gTTS
from io import BytesIO
import re

st.title("Passage Reading")

# Define tabs
tab1, tab2 = st.tabs(["🍃 TTS", "🍃 Sentence Reader"])

with tab1:
    url = "https://github.com/KY7437/G01Final/raw/main/data/story01.png"
    st.image(url, caption="Lesson 1", width=500)

    # Function to convert text to speech
    def text_to_speech(text):
        tts = gTTS(text, lang='en')
        audio_bytes = BytesIO()
        tts.write_to_fp(audio_bytes)
        audio_bytes.seek(0)
        return audio_bytes

    # Predefined text
    predefined_text = """
    In the small town of Willowby, there stood an old library that was rumored to be enchanted. Every night at midnight, the books inside would whisper stories to each other, bringing their characters to life. One evening, Sarah, a curious 15-year-old book lover, decided to sneak into the library to see if the rumors were true.

    As the clock struck twelve, the books began to rustle. To Sarah's amazement, characters stepped out of their pages. She met Alice from Wonderland, the White Rabbit, and even pirates from Treasure Island. They invited her to join their midnight council, where they discussed the tales of their adventures and the wisdom they contained.

    Sarah spent the whole night listening and learning from the characters, promising to keep their secret. As dawn approached, they returned to their pages. Sarah left the library, inspired and filled with stories to tell, forever changed by the magic of the Midnight Library.
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
        st.session_state.show_text = not st.session_state.show_text

    # Button to show the Korean translation
    if st.button("Korean"):
        st.write("""
        작은 마을 윌로비에는 마법에 걸린 것으로 소문난 오래된 도서관이 있었다. 매일 밤 자정이 되면 그 안의 책들이 서로 이야기를 속삭이며 캐릭터들을 생명으로 불러내곤 했다. 어느 날 저녁, 호기심 많은 15세의 책 애호가 사라는 그 소문이 사실인지 확인하기 위해 도서관에 몰래 들어가기로 결심했다.

        시계가 열두 시를 알리자 책들이 소리 내며 움직이기 시작했다. 사라의 놀라움 속에서, 페이지에서 캐릭터들이 걸어나왔다. 그녀는 이상한 나라의 앨리스, 하얀 토끼, 심지어 보물섬의 해적들까지 만났다. 그들은 그녀를 자정 회의에 초대하여 그들의 모험 이야기와 그 속에 담긴 지혜를 논의했다.

        사라는 밤새 캐릭터들의 이야기를 듣고 배우며 그들의 비밀을 지키겠다고 약속했다. 새벽이 다가오자, 그들은 다시 그들의 페이지로 돌아갔다. 사라는 도서관을 떠나며 영감을 받고 이야기로 가득 차서, 자정 도서관의 마법에 의해 영원히 변화된 채로 돌아갔다.
        """)

    # Play audio if the button has been pressed
    if st.session_state.play_audio:
        audio_bytes = text_to_speech(predefined_text)
        st.audio(audio_bytes, format="audio/mp3")
        st.session_state.play_audio = False

    # Display text if the button has been pressed
    if st.session_state.show_text:
        st.write(predefined_text)

with tab2:
    # Function to split text into sentences
    def split_text_into_sentences(text):
        return re.split(r'(?<=[.!?]) +', text)

    # Sample passage
    passage = """
    In the small town of Willowby, there stood an old library that was rumored to be enchanted. Every night at midnight, the books inside would whisper stories to each other, bringing their characters to life. One evening, Sarah, a curious 15-year-old book lover, decided to sneak into the library to see if the rumors were true.

    As the clock struck twelve, the books began to rustle. To Sarah's amazement, characters stepped out of their pages. She met Alice from Wonderland, the White Rabbit, and even pirates from Treasure Island. They invited her to join their midnight council, where they discussed the tales of their adventures and the wisdom they contained.

    Sarah spent the whole night listening and learning from the characters, promising to keep their secret. As dawn approached, they returned to their pages. Sarah left the library, inspired and filled with stories to tell, forever changed by the magic of the Midnight Library.
    """
    sentences = split_text_into_sentences(passage)

    def get_tts():
        sentence = sentences[st.session_state.index]
        tts = gTTS(text=sentence, lang='en')
        audio_bytes = BytesIO()
        tts.write_to_fp(audio_bytes)
        audio_bytes.seek(0)
        return sentence, audio_bytes

    st.header("Sentence by Sentence TTS Reader")
    sentence, audio_bytes = get_tts()
    st.text_area("Current Sentence", value=sentence, height=100, key="current_sentence")
    st.audio(audio_bytes, format="audio/mp3")

    col1, col2 = st.columns(2)
    with col1:
        if st.button("◀ Previous") and st.session_state.index > 0:
            st.session_state.index -= 1
    with col2:
        if st.button("Next ▶") and st.session_state.index < len(sentences) - 1:
            st.session_state.index += 1

    # Apply the custom font size to the text
    st.markdown(f'<div class="sentence-text">{sentence}</div>', unsafe_allow_html=True)
