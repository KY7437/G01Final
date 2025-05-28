import streamlit as st
import pandas as pd
from gtts import gTTS
from io import BytesIO
import random

# 페이지 설정
st.set_page_config(page_title="Review Check")

st.title("Review Check")

# 탭 정의
tab1, tab2, tab3, tab4 = st.tabs(["Paragraph-TF", "Grammar-Level 1", "Grammar-Level 2", "Grammar-Level 3"])

# ------------------- TAB 1 -------------------
with tab1:
    st.header("The Midnight Library - True or False Quiz")
    st.markdown("Decide whether each statement is **True or False** based on the story.")

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

    if "shuffled_questions" not in st.session_state:
        st.session_state.shuffled_questions = random.sample(questions_data, len(questions_data))
        st.session_state.current_question = 0
        st.session_state.answers = [None] * len(questions_data)
        st.session_state.answer_submitted = [False] * len(questions_data)

    q_index = st.session_state.current_question
    question = st.session_state.shuffled_questions[q_index]

    st.subheader(f"Question {q_index + 1} of {len(questions_data)}")
    st.write(question["question"])

    selected = st.radio("Choose your answer:", ["True", "False"],
                        index=0 if st.session_state.answers[q_index] is None else (0 if st.session_state.answers[q_index] else 1))

    if st.button("Submit Answer"):
        st.session_state.answers[q_index] = (selected == "True")
        st.session_state.answer_submitted[q_index] = True

    if st.session_state.answer_submitted[q_index]:
        correct = question["answer"]
        if st.session_state.answers[q_index] == correct:
            st.success("Correct!")
        else:
            st.error("Incorrect.")
        st.info(f"Explanation: {question['explanation']}")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        if st.button("Previous", disabled=(q_index == 0)):
            st.session_state.current_question -= 1
            st.session_state.answer_submitted[q_index] = False

    with col2:
        if st.session_state.answer_submitted[q_index]:
            if st.button("Next", disabled=(q_index == len(questions_data) - 1)):
                st.session_state.current_question += 1
                st.session_state.answer_submitted[q_index] = False
                st.rerun()

    with col3:
        if st.button("Show Score"):
            correct_count = sum(
                1 for i, q in enumerate(st.session_state.shuffled_questions)
                if st.session_state.answers[i] == q["answer"]
            )
            st.success(f"You scored {correct_count} out of {len(questions_data)}")

    with col4:
        if st.button("Reset Quiz"):
            del st.session_state.shuffled_questions
            del st.session_state.current_question
            del st.session_state.answers
            del st.session_state.answer_submitted
            st.experimental_rerun()

# ------------------- TAB 2 -------------------
with tab2:
    st.header("Verb Form Quiz (Level 2)")

    verb_data = [
        {"base": "go", "past": "went", "pp": "gone"},
        {"base": "eat", "past": "ate", "pp": "eaten"},
        {"base": "write", "past": "wrote", "pp": "written"},
        {"base": "take", "past": "took", "pp": "taken"},
        {"base": "see", "past": "saw", "pp": "seen"},
        {"base": "come", "past": "came", "pp": "come"},
        {"base": "break", "past": "broke", "pp": "broken"},
        {"base": "choose", "past": "chose", "pp": "chosen"},
        {"base": "fly", "past": "flew", "pp": "flown"},
        {"base": "begin", "past": "began", "pp": "begun"}
    ]

    if "verb_quiz" not in st.session_state:
        st.session_state.verb_quiz = random.sample(verb_data, len(verb_data))
        st.session_state.verb_index = 0
        st.session_state.verb_mode = random.choices(["past", "pp"], k=len(verb_data))
        st.session_state.verb_answers = [None] * len(verb_data)
        st.session_state.verb_submitted = [False] * len(verb_data)

    index = st.session_state.verb_index
    current_verb = st.session_state.verb_quiz[index]
    mode = st.session_state.verb_mode[index]

    correct_answer = current_verb[mode]
    wrong_answers = set(v[mode] for v in verb_data if v != current_verb)
    choices = random.sample(list(wrong_answers), 3) + [correct_answer]
    random.shuffle(choices)

    mode_label = "Past" if mode == "past" else "Past Participle"
    st.markdown(f"### {current_verb['base']} ({mode_label})")

    selected = st.radio("Choose the correct form:", choices,
                        index=0 if st.session_state.verb_answers[index] is None else choices.index(st.session_state.verb_answers[index]))

    if st.button("Submit Answer"):
        st.session_state.verb_answers[index] = selected
        st.session_state.verb_submitted[index] = True

    if st.session_state.verb_submitted[index]:
        if selected == correct_answer:
            st.success("Correct!")
        else:
            st.error(f"Incorrect. The correct answer is: **{correct_answer}**")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        if st.button("Previous", disabled=(index == 0)):
            st.session_state.verb_index -= 1
            st.rerun()

    with col2:
        if st.button("Next", disabled=(index == len(verb_data) - 1)):
            st.session_state.verb_index += 1
            st.rerun()

    with col3:
        if st.button("Show Score"):
            score = sum(
                1 for i, v in enumerate(st.session_state.verb_quiz)
                if st.session_state.verb_answers[i] == v[st.session_state.verb_mode[i]]
            )
            st.success(f"Your score: {score} / {len(verb_data)}")

    with col4:
        if st.button("Reset Quiz"):
            del st.session_state.verb_quiz
            del st.session_state.verb_index
            del st.session_state.verb_mode
            del st.session_state.verb_answers
            del st.session_state.verb_submitted
            st.experimental_rerun()

# ------------------- TAB 3 -------------------
with tab3:
    st.header("Level 3 Content")
    st.write("Text-to-Speech Demo:")
    text = st.text_input("Enter text for TTS:", "Hello, Streamlit!")
    if st.button("Generate TTS"):
        tts = gTTS(text)
        tts_bytes = BytesIO()
        tts.write_to_fp(tts_bytes)
        tts_bytes.seek(0)
        st.audio(tts_bytes, format="audio/mp3")

# ------------------- TAB 4 -------------------
with tab4:
    st.header("Paragraph TF - Coming Soon")
    st.write("You can add paragraph-based True/False questions here later.")
