import streamlit as st
import pandas as pd
from gtts import gTTS
from io import BytesIO
import random
import tempfile

st.write("Review Check")

# Define tabs
tab1, tab2, tab3, tab4 = st.tabs(["Grammar-Level 1", "Grammar-Level 2", "Grammar-Level 3", "paragraph-TF"])

with tab1:
    import streamlit as st
import random

# Quiz questions (with explanation)
questions_data = [
    {
        "question": "Sarah is a 15-year-old girl who sneaks into the library during the day.",
        "answer": False,
        "explanation": "Sarah sneaks into the library at night, not during the day."
    },
    {
        "question": "The library in Willowby is said to be enchanted.",
        "answer": True,
        "explanation": "The story clearly describes the library as rumored to be enchanted."
    },
    {
        "question": "At midnight, the characters in the books come to life and talk.",
        "answer": True,
        "explanation": "At midnight, the books whisper and characters step out of the pages."
    },
    {
        "question": "Sarah met Harry Potter in the Midnight Library.",
        "answer": False,
        "explanation": "Harry Potter is not mentioned; she met characters like Alice and pirates from Treasure Island."
    },
    {
        "question": "The characters return to their pages as dawn approaches.",
        "answer": True,
        "explanation": "As dawn approaches, the characters return to their pages."
    }
]

st.set_page_config(page_title="Midnight Library Quiz")

st.title("The Midnight Library - True or False Quiz")
st.markdown("Decide whether each statement is **True or False** based on the story.")

# Shuffle only once per session
if "shuffled_questions" not in st.session_state:
    st.session_state.shuffled_questions = random.sample(questions_data, len(questions_data))
    st.session_state.current_question = 0
    st.session_state.answers = [None] * len(questions_data)
    st.session_state.answer_submitted = [False] * len(questions_data)

# Navigation
q_index = st.session_state.current_question
question = st.session_state.shuffled_questions[q_index]

# Display question
st.subheader(f"Question {q_index + 1} of {len(questions_data)}")
st.write(question["question"])

# Answer input
selected = st.radio("Choose your answer:", ["True", "False"], index=0 if st.session_state.answers[q_index] is None else (0 if st.session_state.answers[q_index] else 1))

# Submit answer
if st.button("Submit Answer"):
    st.session_state.answers[q_index] = (selected == "True")
    st.session_state.answer_submitted[q_index] = True

# Feedback
if st.session_state.answer_submitted[q_index]:
    correct = question["answer"]
    if st.session_state.answers[q_index] == correct:
        st.success("Correct!")
    else:
        st.error("Incorrect.")
    st.info(f"Explanation: {question['explanation']}")

# Navigation buttons
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("Previous", disabled=(q_index == 0)):
        st.session_state.current_question -= 1
        st.session_state.answer_submitted[q_index] = False  # Reset the submission flag

with col2:
    # Enable "Next" button only after submitting an answer
    if st.session_state.answer_submitted[q_index]:
        if st.button("Next", disabled=(q_index == len(questions_data) - 1)):
            # Move to next question immediately after submission
            st.session_state.current_question += 1
            # Reset the submission flag for the new question
            st.session_state.answer_submitted[q_index] = False
            # Force a rerun to apply changes immediately
            st.rerun()

with col3:
    if st.button("Show Score"):
        correct_count = sum(
            1 for i, q in enumerate(st.session_state.shuffled_questions)
            if st.session_state.answers[i] == q["answer"]
        )
        st.success(f"You scored {correct_count} out of {len(questions_data)}")

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
