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
    # Grammar example sentence dictionary
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

    # Input expression
    expression = st.text_input("📝 Enter expressions (ex. that, be p.p): ").strip().lower()

    # Output results
    if expression in EXPRESSION_DB:
        data = EXPRESSION_DB[expression]
        st.write("🗣️ Sample sentences:")
        for ex in data["examples"]:
            st.write(f"- {ex}")
    else:
        st.write("⚠️ Please use expressions we used in class!!")

# Example TTS function (place where you might integrate TTS)
def text_to_speech(text):
    tts = gTTS(text, lang='en')
    audio_bytes = BytesIO()
    tts.write_to_fp(audio_bytes)
    audio_bytes.seek(0)
    return audio_bytes
