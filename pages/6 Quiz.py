import streamlit as st
import random
from gtts import gTTS
from io import BytesIO

# 페이지 설정
st.set_page_config(page_title="Review Check")

st.title("Review Check")

# 탭 구성
tab1, tab2, tab3, tab4 = st.tabs(["Paragraph-TF", "Grammar-Level 1", "Grammar-Level 2", "Grammar-Level 3"])

# ---------------- TAB 1: Paragraph TF ----------------
with tab1:
    st.header("The Midnight Library - True or False Quiz")
    st.markdown("Decide whether each statement is **True or False** based on the story.")

    # 퀴즈 데이터
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

    # 세션 상태 초기화
    if "tf_current_q" not in st.session_state:
        st.session_state.tf_current_q = 0
        st.session_state.tf_answers = [None] * len(questions_data)
        st.session_state.tf_submitted = [False] * len(questions_data)

    q_idx = st.session_state.tf_current_q
    question = questions_data[q_idx]

    st.subheader(f"Question {q_idx + 1} of {len(questions_data)}")
    st.write(question["question"])

    selected = st.radio(
        f"Select your answer for Q{q_idx}",
        ["True", "False"],
        key=f"tf_radio_{q_idx}",
        index=0 if st.session_state.tf_answers[q_idx] is None else (0 if st.session_state.tf_answers[q_idx] else 1)
    )

    if st.button(f"Submit Answer TF {q_idx}"):
        st.session_state.tf_answers[q_idx] = (selected == "True")
        st.session_state.tf_submitted[q_idx] = True

    if st.session_state.tf_submitted[q_idx]:
        if st.session_state.tf_answers[q_idx] == question["answer"]:
            st.success("Correct!")
        else:
            st.error("Incorrect.")
        st.info(f"Explanation: {question['explanation']}")

    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("Previous TF", disabled=(q_idx == 0)):
            st.session_state.tf_current_q -= 1

    with col2:
        if st.button("Next TF", disabled=(q_idx == len(questions_data) - 1)):
            st.session_state.tf_current_q += 1

    with col3:
        if st.button("Show Score TF"):
            score = sum(
                1 for i, q in enumerate(questions_data)
                if st.session_state.tf_answers[i] == q["answer"]
            )
            st.success(f"You scored {score} out of {len(questions_data)}")

# ---------------- TAB 2: Grammar-Level 1 (단답형 불규칙 동사) ----------------
with tab2:
    st.header("Verb Form Quiz (Level 1 - Fill in the blank)")

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
        st.session_state.verb_mode = random.choices(["past", "pp"], k=len(verb_data))
        st.session_state.verb_index = 0
        st.session_state.verb_answers = [""] * len(verb_data)
        st.session_state.verb_submitted = [False] * len(verb_data)

    vi = st.session_state.verb_index
    current = st.session_state.verb_quiz[vi]
    mode = st.session_state.verb_mode[vi]
    mode_label = "Past" if mode == "past" else "Past Participle"
    correct = current[mode]

    st.markdown(f"### {current['base']} ({mode_label})")
    answer = st.text_input("Your answer:", value=st.session_state.verb_answers[vi], key=f"verb_input_{vi}")

    if st.button(f"Submit Verb Answer {vi}"):
        st.session_state.verb_answers[vi] = answer.strip().lower()
        st.session_state.verb_submitted[vi] = True

    if st.session_state.verb_submitted[vi]:
        if st.session_state.verb_answers[vi] == correct.lower():
            st.success("Correct!")
        else:
            st.error(f"Incorrect. The correct answer is: **{correct}**")

    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("Previous Verb", disabled=(vi == 0)):
            st.session_state.verb_index -= 1
            st.rerun()

    with col2:
        if st.button("Next Verb", disabled=(vi == len(verb_data) - 1)):
            st.session_state.verb_index += 1
            st.rerun()

    with col3:
        if st.button("Show Score Verb"):
            score = sum(
                1 for i, v in enumerate(st.session_state.verb_quiz)
                if st.session_state.verb_answers[i] == v[st.session_state.verb_mode[i]].lower()
            )
            st.success(f"Your score: {score} / {len(verb_data)}")

# ---------------- TAB 3: Grammar-Level 2 ----------------
with tab3:
    st.header("Level 2 - Text to Speech")
    text = st.text_input("Enter text for TTS:", "Hello, Streamlit!")
    if st.button("Generate TTS"):
        tts = gTTS(text)
        tts_bytes = BytesIO()
        tts.write_to_fp(tts_bytes)
        tts_bytes.seek(0)
        st.audio(tts_bytes, format="audio/mp3")

# ---------------- TAB 4: Grammar-Level 3 ----------------
with tab4:
    st.header("Grammar Level 3 - Coming Soon")
    st.write("More advanced grammar exercises will be added here.")
