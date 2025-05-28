import streamlit as st
import random
from gtts import gTTS
from io import BytesIO

st.set_page_config(page_title="Review Check")

st.title("Review Check")

# Define tabs
tab1, tab2, tab3, tab4 = st.tabs(["Paragraph-TF", "Verb Form Quiz", "Text-to-Speech", "Coming Soon"])

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

    if "tf_current" not in st.session_state:
        st.session_state.tf_questions = random.sample(questions_data, len(questions_data))
        st.session_state.tf_current = 0
        st.session_state.tf_answers = [None] * len(questions_data)
        st.session_state.tf_submitted = [False] * len(questions_data)

    idx = st.session_state.tf_current
    q = st.session_state.tf_questions[idx]

    st.subheader(f"Question {idx + 1} of {len(questions_data)}")
    st.write(q["question"])

    selected = st.radio("Choose your answer:", ["True", "False"],
                        index=0 if st.session_state.tf_answers[idx] is None else (0 if st.session_state.tf_answers[idx] else 1),
                        key=f"tf_radio_{idx}")

    if st.button("Submit Answer", key=f"submit_tf_{idx}"):
        st.session_state.tf_answers[idx] = (selected == "True")
        st.session_state.tf_submitted[idx] = True

    if st.session_state.tf_submitted[idx]:
        correct = q["answer"]
        if st.session_state.tf_answers[idx] == correct:
            st.success("Correct!")
        else:
            st.error("Incorrect.")
        st.info(f"Explanation: {q['explanation']}")

    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("Previous", key=f"tf_prev_{idx}", disabled=(idx == 0)):
            st.session_state.tf_current -= 1
    with col2:
        if st.button("Next", key=f"tf_next_{idx}", disabled=(idx == len(questions_data) - 1)):
            st.session_state.tf_current += 1
    with col3:
        if st.button("Show Score", key="tf_score"):
            score = sum(
                1 for i, q in enumerate(st.session_state.tf_questions)
                if st.session_state.tf_answers[i] == q["answer"]
            )
            st.success(f"Your score: {score} / {len(questions_data)}")

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
        st.session_state.verb_mode = random.choices(["past", "pp"], k=len(verb_data))
        st.session_state.verb_answers = [None] * len(verb_data)
        st.session_state.verb_submitted = [False] * len(verb_data)

    vi = st.session_state.verb_index
    verb = st.session_state.verb_quiz[vi]
    mode = st.session_state.verb_mode[vi]
    label = "Past" if mode == "past" else "Past Participle"

    st.markdown(f"### {verb['base']} ({label})")

    input_key = f"verb_input_{vi}"
    answer = st.text_input("Your answer:", key=input_key)

    if st.button("Submit Answer", key=f"submit_verb_{vi}"):
        st.session_state.verb_answers[vi] = answer.strip().lower()
        st.session_state.verb_submitted[vi] = True

    if st.session_state.verb_submitted[vi]:
        correct = verb[mode]
        if st.session_state.verb_answers[vi] == correct:
            st.success("Correct!")
        else:
            st.error(f"Incorrect. The correct answer is: **{correct}**")

    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("Previous", key=f"verb_prev_{vi}", disabled=(vi == 0)):
            st.session_state.verb_index -= 1
    with col2:
        if st.button("Next", key=f"verb_next_{vi}", disabled=(vi == len(verb_data) - 1)):
            st.session_state.verb_index += 1
    with col3:
        if st.button("Show Score", key="verb_score"):
            score = sum(
                1 for i in range(len(verb_data))
                if st.session_state.verb_answers[i] == st.session_state.verb_quiz[i][st.session_state.verb_mode[i]]
            )
            st.success(f"Your score: {score} / {len(verb_data)}")

# ------------------- TAB 3 -------------------
with tab3:
    st.header("Text-to-Speech (TTS)")
    text = st.text_input("Enter text for TTS:", "Hello, Streamlit!", key="tts_input")
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
