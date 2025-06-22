import streamlit as st
import pandas as pd
import random

st.title("Voca Starter")
st.write("these apps are for vocabulary study")

# Load vocabulary list from CSV
@st.cache_data
def load_vocab():
    url = "https://raw.githubusercontent.com/KY7437/G01Final/main/wordlist.csv"
    df = pd.read_csv(url)
    vocab_dict = dict(zip(df["Word"], df["Meaning"])) 
    return vocab_dict

vocab = load_vocab()

# Initialize session state
if "meaning_quiz_items" not in st.session_state:
    st.session_state.meaning_quiz_items = random.sample(list(vocab.items()), 5)
    st.session_state.spelling_quiz_items = random.sample(list(vocab.items()), 5)
    st.session_state.current_q_meaning = 0
    st.session_state.current_q_spelling = 0
    st.session_state.score_meaning = 0
    st.session_state.score_spelling = 0
    st.session_state.show_result_meaning = False
    st.session_state.show_result_spelling = False

# Define tabs
tab1, tab2, tab3 = st.tabs(["🍃 Word List", "🍃 Meaning Master", "🍃 Spelling Master"])

with tab1:
    st.markdown("### 📋 Word List")
    st.header("Instruction")
    st.write("Learners should know the words’ meanings and spellings before the class begins.
This app is designed to help you review key vocabulary through fun and interactive activities, such as matching word meanings and spelling practice.")

    # Load CSV from GitHub
    url = "https://raw.githubusercontent.com/KY7437/G01Final/main/wordlist.csv"
    try:
        df = pd.read_csv(url)
        if st.button("Show Word List"):
            st.dataframe(df, use_container_width=True)
    except Exception as e:
        st.error(f"Error loading word list: {e}")

def display_quiz(quiz_type):
    if quiz_type.lower() == "meaning":
        st.title("📖 Vocabulary Meaning Quiz")
        quiz_items = st.session_state.meaning_quiz_items
        current_q = st.session_state.current_q_meaning
        score = st.session_state.score_meaning
        key_suffix = "meaning"
    else:
        st.title("📚 Spelling Master")
        quiz_items = st.session_state.spelling_quiz_items
        current_q = st.session_state.current_q_spelling
        score = st.session_state.score_spelling
        key_suffix = "spelling"

    if current_q < len(quiz_items):
        word, meaning = quiz_items[current_q]

        st.subheader(f"Question {current_q + 1} of {len(quiz_items)}")
        st.write(f"**Word:** {word}" if quiz_type.lower() == "meaning" else f"**Meaning:** {meaning}")

        user_input = st.text_input(
            "Enter the Korean meaning:" if quiz_type.lower() == "meaning" else "Enter the English word:",
            key=f"input_{current_q}_{key_suffix}"
        )

        if st.button("Submit", key=f"submit_{current_q}_{key_suffix}") and not st.session_state[f"show_result_{key_suffix}"]:
            st.session_state[f"user_input_{key_suffix}"] = user_input.strip().lower()
            st.session_state[f"show_result_{key_suffix}"] = True

        if st.session_state[f"show_result_{key_suffix}"]:
            correct_answer = meaning if quiz_type.lower() == "meaning" else word
            if st.session_state[f"user_input_{key_suffix}"] == correct_answer.strip().lower():
                st.success("✅ Correct!")
                st.session_state[f"score_{key_suffix}"] += 1
            else:
                st.error(f"❌ Incorrect! The correct answer was **{correct_answer}**.")

            if st.button("Next", key=f"next_{key_suffix}"):
                st.session_state[f"current_q_{key_suffix}"] += 1
                st.session_state[f"show_result_{key_suffix}"] = False
                st.rerun()
    else:
        st.subheader("🎉 Quiz Finished!")
        st.write(f"Your total score is: **{st.session_state[f'score_{key_suffix}']} / {len(quiz_items)}**")

        if st.button("Play Again", key=f"play_again_{key_suffix}"):
            st.session_state[f"{quiz_type.lower()}_quiz_items"] = random.sample(list(vocab.items()), 5)
            st.session_state[f"current_q_{key_suffix}"] = 0
            st.session_state[f"score_{key_suffix}"] = 0
            st.session_state[f"show_result_{key_suffix}"] = False
            st.rerun()

with tab2:
    display_quiz("meaning")

with tab3:
    display_quiz("spelling")
