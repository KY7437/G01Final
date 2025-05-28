import streamlit as st
import random
from gtts import gTTS
from io import BytesIO

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

    if "tf_quiz" not in st.session_state:
        st.session_state.tf_quiz = random.sample(questions_data, len(questions_data))
        st.session_state.tf_index = 0
        st.session_state.tf_answers = [None] * len(questions_data)
        st.session_state.tf_submitted = [False] * len(questions_data)

    index = st.session_state.tf_index
    q = st.session_state.tf_quiz[index]

    st.subheader(f"Question {index + 1} of {len(questions_data)}")
    st.write(q["question"])

    selected = st.radio("Choose your answer:", ["True", "False"],
                        index=0 if st.session_state.tf_answers[index] is None else (0 if st.session_state.tf_answers[index] else 1),
                        key=f"tf_radio_{index}")

    if st.button("Submit Answer", key=f"tf_submit_{index}"):
        st.session_state.tf_answers[index] = (selected == "True")
        st.session_state.tf_submitted[index] = True

    if st.session_state.tf_submitted[index]:
        if st.session_state.tf_answers[index] == q["answer"]:
            st.success("Correct!")
        else:
            st.error("Incorrect.")
        st.info(f"Explanation: {q['explanation']}")

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        if st.button("Previous", disabled=(index == 0), key="tf_prev"):
            st.session_state.tf_index -= 1
            st.rerun()
    with col2:
        if st.button("Next", disabled=(index == len(questions_data) - 1), key="tf_next"):
            st.session_state.tf_index += 1
            st.rerun()
    with col3:
        if st.button("Show Score", key="tf_score"):
            score = sum(
                1 for i, q in enumerate(st.session_state.tf_quiz)
                if st.session_state.tf_answers[i] == q["answer"]
            )
            st.success(f"You scored {score} / {len(questions_data)}")
    with col4:
        if st.button("Reset Quiz", key="tf_reset"):
            for k in ["tf_quiz", "tf_index", "tf_answers", "tf_submitted"]:
                st.session_state.pop(k, None)
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

    v_index = st.session_state.verb_index
    current = st.session_state.verb_quiz[v_index]
    mode = st.session_state.verb_mode[v_index]
    correct = current[mode]

    mode_label = "Past" if mode == "past" else "Past Participle"
    st.markdown(f"### {current['base']} ({mode_label})")

    user_input = st.text_input("Enter the correct form:",
                               value="" if st.session_state.verb_answers[v_index] is None else st.session_state.verb_answers[v_index],
                               key=f"verb_input_{v_index}")

    if st.button("Submit Answer", key=f"verb_submit_{v_index}"):
        st.session_state.verb_answers[v_index] = user_input.strip()
        st.session_state.verb_submitted[v_index] = True

    if st.session_state.verb_submitted[v_index]:
        if user_input.strip().lower() == correct.lower():
            st.success("Correct!")
        else:
            st.error(f"Incorrect. The correct answer is: **{correct}**")

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        if st.button("Previous", disabled=(v_index == 0), key="verb_prev"):
            st.session_state.verb_index -= 1
            st.rerun()
    with col2:
        if st.button("Next", disabled=(v_index == len(verb_data) - 1), key="verb_next"):
            st.session_state.verb_index += 1
            st.rerun()
    with col3:
        if st.button("Show Score", key="verb_score"):
            score = sum(
                1 for i, v in enumerate(st.session_state.verb_quiz)
                if st.session_state.verb_answers[i]
                and st.session_state.verb_answers[i].strip().lower() == v[st.session_state.verb_mode[i]].lower()
            )
            st.success(f"Your score: {score} / {len(verb_data)}")
    with col4:
        if st.button("Reset Quiz", key="verb_reset"):
            for k in ["verb_quiz", "verb_index", "verb_mode", "verb_answers", "verb_submitted"]:
                st.session_state.pop(k, None)
            st.experimental_rerun()

# ------------------- TAB 3 -------------------
with tab3:
    st.header("Text-to-Speech Demo")
    text = st.text_input("Enter text for TTS:", "Hello, Streamlit!")
    if st.button("Generate TTS", key="tts_button"):
        tts = gTTS(text)
        tts_bytes = BytesIO()
        tts.write_to_fp(tts_bytes)
        tts_bytes.seek(0)
        st.audio(tts_bytes, format="audio/mp3")

# ------------------- TAB 4 -------------------
with tab4:
    st.header("Paragraph TF - Coming Soon")
    st.write("You can add paragraph-based True/False questions here later.")
