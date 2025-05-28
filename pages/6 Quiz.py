import streamlit as st
import pandas as pd
from gtts import gTTS
from io import BytesIO
import random

# 페이지 설정은 반드시 코드 가장 위에 있어야 합니다.
st.set_page_config(page_title="Review Check")

st.title("Review Check")

# 탭 4개 정의
tab1, tab2, tab3, tab4 = st.tabs(["Grammar-Level 1", "Grammar-Level 2", "Grammar-Level 3", "Paragraph-TF"])

# ------------------- TAB 1 -------------------
# 퀴즈 탭
with tab1:
    st.header("The Midnight Library - True or False Quiz")
    st.markdown("Decide whether each statement is **True or False** based on the story.")

    # 퀴즈 문제 정의
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
    if "shuffled_questions" not in st.session_state:
        st.session_state.shuffled_questions = random.sample(questions_data, len(questions_data))
        st.session_state.current_question = 0
        st.session_state.answers = [None] * len(questions_data)
        st.session_state.answer_submitted = [False] * len(questions_data)

    # 현재 질문 표시
    q_index = st.session_state.current_question
    question = st.session_state.shuffled_questions[q_index]

    st.subheader(f"Question {q_index + 1} of {len(questions_data)}")
    st.write(question["question"])

    # 답변 선택
    selected = st.radio("Choose your answer:", ["True", "False"],
                        index=0 if st.session_state.answers[q_index] is None else (0 if st.session_state.answers[q_index] else 1))

    # 제출 버튼
    if st.button("Submit Answer"):
        st.session_state.answers[q_index] = (selected == "True")
        st.session_state.answer_submitted[q_index] = True

    # 결과 및 해설 표시
    if st.session_state.answer_submitted[q_index]:
        correct = question["answer"]
        if st.session_state.answers[q_index] == correct:
            st.success("Correct!")
        else:
            st.error("Incorrect.")
        st.info(f"Explanation: {question['explanation']}")

    # 네비게이션 버튼
    col1, col2, col3 = st.columns(3)

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

# ------------------- TAB 2 -------------------
# Level 2 탭
with tab2:
    st.header("Level 2 Content")
    st.write("This is where you can add Level 2 content.")
    if st.button("Generate Random Number"):
        number = random.randint(1, 100)
        st.write(f"Random Number: {number}")

# ------------------- TAB 3 -------------------
# TTS 기능 탭
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
# Paragraph-TF 탭
with tab4:
    st.header("Paragraph TF - Coming Soon")
    st.write("You can add paragraph-based True/False questions here later.")
