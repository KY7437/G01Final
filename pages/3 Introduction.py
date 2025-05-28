import streamlit as st
import pandas as pd
from gtts import gTTS
from io import BytesIO
import random

st.write("🌱 Vocabulary learning")

# Define tabs
tab1, tab2, tab3 = st.tabs(["❄️ Word List", "❄️ 2. Wordle", "❄️ 3. Role Playing"])

with tab1:
    st.markdown("### 📋 Word List")

    # Load CSV from GitHub
    url = "https://raw.githubusercontent.com/KY7437/G01Final/refs/heads/main/wordlist.csv"
    df = pd.read_csv(url)

    # Show table only when button is clicked
    if st.button("Show Word List"):
        st.dataframe(df, use_container_width=True)

with tab2:
    # Core words dictionary
    core_words = {
        "magic": "a special power that makes impossible things happen",
        "library": "a place where you can read or borrow books",
        "adventure": "an exciting or unusual experience",
        "secret": "something that you do not tell other people",
        "listen": "to pay attention to sounds or words",
        "sneak": "to go somewhere quietly and secretly"
    }

    word_list = [
        "magic", "library", "adventure", "secret", "listen", "sneak",
        "midnight", "character", "change", "inspire", "pirate",
        "council", "tale", "wisdom", "leave", "story", "approach",
        "curious", "dawn", "keep", "promise", "change", "return",
        "learn", "whole", "spend", "contain", "wisdom", "discuss", "join", "invite",
        "island", "treasure", "decide", "bring", "curious", "enchant", "stand", "rumor"
    ]

    # Set up session state for the Wordle game
    if 'answer' not in st.session_state:
        st.session_state.answer = random.choice(list(core_words.keys()))
        st.session_state.definition = core_words[st.session_state.answer]
        st.session_state.attempts = 0
        st.session_state.max_attempts = 6
        st.session_state.guessed = False

    def compare_words(guess, answer):
        result = []
        for i in range(len(guess)):
            if i < len(answer) and guess[i] == answer[i]:
                result.append("🟩")
            elif guess[i] in answer:
                result.append("🟨")
            else:
                result.append("⬛")
        return "".join(result)

    st.title("Wordle Game")
    st.write(f"Hint: Definition - {st.session_state.definition}")
    st.write(f"The word has {len(st.session_state.answer)} letters.")
    st.write(f"You have {st.session_state.max_attempts - st.session_state.attempts} attempts left.")

    guess = st.text_input("Enter your guess:")

    if st.button("Submit") and guess:
        guess = guess.lower()
        if guess not in word_list:
            st.warning("Please guess a valid word from the list.")
        elif st.session_state.guessed:
            st.info("You already guessed the word! Please restart the app to play again.")
        else:
            st.session_state.attempts += 1
            feedback = compare_words(guess, st.session_state.answer)
            st.write(f"Result: {feedback}")
            if guess == st.session_state.answer:
                st.success(f"Correct! The word is '{st.session_state.answer.upper()}'.")
                st.write(f"Meaning: {st.session_state.definition}")
                st.session_state.guessed = True
            elif st.session_state.attempts >= st.session_state.max_attempts:
                st.error(f"Sorry, you used all attempts. The word was '{st.session_state.answer.upper()}'.")
                st.write(f"Meaning: {st.session_state.definition}")
                st.session_state.guessed = True

with tab3:
   import streamlit as st
from gtts import gTTS
import tempfile
import os

# 문법 예문 및 설명 데이터베이스
EXPRESSION_DB = {
    "that": {
        "examples": [
            "A: Did you watch the movie that I recommended yesterday?",
            "B: Yes, I did! I loved the part that shows the main character’s childhood.",
            "A: Me too! The scene that made me cry was at the end.",
            "B: Same here. I think it’s a movie that everyone should watch."
        ]
    },
    "be p.p": {
        "examples": [
            "A: Did you hear? Our classroom was cleaned yesterday.",
            "B: Really? It looks so much better now.",
            "A: Yeah, and new computers were installed this morning.",
            "B: That’s great! I heard the old ones were broken last week.",
            "A: Right. The whole room was redesigned by the school’s tech team."
        ]
    }
}

# 문법 설명
EXPRESSION_INFO = {
    "that": {
        "description": (
            "**Relative pronoun 'that'** is used to connect a noun to a clause that gives more information about it.\n\n"
            "Example: *The book that I read was very interesting.*"
        )
    },
    "be p.p": {
        "description": (
            "**Passive voice 'be + past participle' (be p.p)** is used when the subject receives the action.\n\n"
            "Example: *The window was broken by the wind.*"
        )
    }
}

# 제목
st.title("🎭 Middle School Roleplay Dialog App")
st.markdown("Select a grammar expression to hear a conversation. You can reveal the text if needed!")

# 문법 선택
expression = st.selectbox("🔤 Choose a grammar expression:", list(EXPRESSION_DB.keys()))

# 문법 설명 표시
st.markdown("### 📘 Grammar Explanation")
st.markdown(EXPRESSION_INFO[expression]["description"])

# TTS 재생
if st.button("▶️ Listen to the dialogue"):
    examples = EXPRESSION_DB[expression]["examples"]
    full_text = " ".join(examples)
    tts = gTTS(full_text)
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as fp:
        tts.save(fp.name)
        st.audio(fp.name, format="audio/mp3")

    st.session_state["show_text"] = False

# 대화문 보기
if "show_text" not in st.session_state:
    st.session_state["show_text"] = False

if st.button("👀 Show the dialogue text"):
    st.session_state["show_text"] = True

if st.session_state["show_text"]:
    examples = EXPRESSION_DB[expression]["examples"]
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("👤 A")
        for line in examples:
            if line.startswith("A:"):
                st.write(line[3:])
            else:
                st.write("")
    with col2:
        st.subheader("🧑 B")
        for line in examples:
            if line.startswith("B:"):
                st.write(line[3:])
            else:
                st.write("")

