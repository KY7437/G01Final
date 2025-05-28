import streamlit as st
import random
from gtts import gTTS
from io import BytesIO

# 페이지 설정
st.set_page_config(page_title="Review Check", layout="centered")

# 탭 설정
tab1, tab2, tab3, tab4 = st.tabs(["Paragraph-TF", "Grammar-Level 1", "Grammar-Level 2", "Grammar-Level 3"])

# ------------------- TAB 1 -------------------
with tab1:
    st.header("The Midnight Library - True or False Quiz")
    st.markdown("Decide whether each statement is **True or False** based on the story.")

    tf_questions = [
        {"question": "Sarah is a 15-year-old girl who sneaks into the library during the day.", "answer": False, "explanation": "She sneaks in at night."},
        {"question": "The library in Willowby is said to be enchanted.", "answer": True, "explanation": "It is described as enchanted."},
        {"question": "At midnight, the characters in the books come to life and talk.", "answer": True, "explanation": "They whisper and come out of the pages."},
        {"question": "Sarah met Harry Potter in the Midnight Library.", "answer": False, "explanation": "She met characters like Alice and pirates, not Harry Potter."},
        {"question": "The characters return to their pages as dawn approaches.", "answer": True, "explanation": "They return as dawn nears."}
    ]

    if "tf_index" not in st.session_state:
        st.session_state.tf_index = 0
        st.session_state.tf_shuffled = random.sample(tf_questions, len(tf_questions))
        st.session_state.tf_answers = [None] * len(tf_questions)

    idx = st.session_state.tf_index
    question = st.session_state.tf_shuffled[idx]

    st.subheader(f"Question {idx + 1} of {len(tf_questions)}")
    st.write(question["question"])

    answer = st.radio("Select your answer:", ["True", "False"], key=f"tf_q_{idx}")
    submitted = st.button("Submit Answer", key=f"tf_submit_{idx}")

    if submitted:
        user_answer = (answer == "True")
        st.session_state.tf_answers[idx] = user_answer
        if user_answer == question["answer"]:
            st.success("Correct!")
        else:
            st.error("Incorrect.")
        st.info(f"Explanation: {question['explanation']}")

    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button("Previous", disabled=(idx == 0), key="tf_prev"):
            st.session_state.tf_index -= 1
            st.experimental_rerun()

    with col2:
        if st.button("Next", disabled=(idx == len(tf_questions) - 1), key="tf_next"):
            st.session_state.tf_index += 1
            st.experimental_rerun()

    with col3:
        if st.button("Show Score", key="tf_score"):
            correct_count = sum(
                1 for i, q in enumerate(st.session_state.tf_shuffled)
                if st.session_state.tf_answers[i] == q["answer"]
            )
            st.success(f"Your score: {correct_count} / {len(tf_questions)}")

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

    if "verb_index" not in st.session_state:
        st.session_state.verb_quiz = random.sample(verb_data, len(verb_data))
        st.session_state.verb_index = 0
        st.session_state.verb_modes = random.choices(["past", "pp"], k=len(verb_data))
        st.session_state.verb_answers = [None] * len(verb_data)

    i = st.session_state.verb_index
    current = st.session_state.verb_quiz[i]
    mode = st.session_state.verb_modes[i]
    answer_key = f"verb_answer_{i}"
    correct = current[mode]

    label = "Past" if mode == "past" else "Past Participle"
    st.markdown(f"### {current['base']} ({label})")

    user_input = st.text_input("Type your answer:", key=answer_key)
    if st.button("Submit Answer", key=f"verb_submit_{i}"):
        st.session_state.verb_answers[i] = user_input.strip().lower()
        if user_input.strip().lower() == correct:
            st.success("Correct!")
        else:
            st.error(f"Incorrect. Correct answer: **{correct}**")

    c1, c2, c3 = st.columns(3)
    with c1:
        if st.button("Previous", disabled=(i == 0), key="verb_prev"):
            st.session_state.verb_index -= 1
            st.experimental_rerun()
    with c2:
        if st.button("Next", disabled=(i == len(verb_data) - 1), key="verb_next"):
            st.session_state.verb_index += 1
            st.experimental_rerun()
    with c3:
        if st.button("Show Score-Q2", key="verb_score"):
            score = sum(
                1 for j, v in enumerate(st.session_state.verb_quiz)
                if st.session_state.verb_answers[j] == v[st.session_state.verb_modes[j]]
            )
            st.success(f"Your score: {score} / {len(verb_data)}")

# ------------------- TAB 3 -------------------
with tab3:
    st.header("Level 3 Content")
    st.write("Text-to-Speech Demo")

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
