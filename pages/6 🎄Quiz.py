import streamlit as st
import random
from gtts import gTTS
from io import BytesIO

st.set_page_config(page_title="Review Check", layout="centered")

tab1, tab2, tab3, tab4 = st.tabs(["🍃Paragraph-TF", "🍃Grammar-Level 1", "🍃Grammar-Level 2", "🍃Grammar-Level 3"])

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

    answer = st.radio("Select your answer:", ["True", "False"], key=f"tf_radio_{idx}")
    if st.button("Submit Answer", key=f"tf_submit_btn_{idx}"):
        user_answer = (answer == "True")
        st.session_state.tf_answers[idx] = user_answer
        if user_answer == question["answer"]:
            st.success("Correct!")
        else:
            st.error("Incorrect.")
        st.info(f"Explanation: {question['explanation']}")

    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("Previous", disabled=(idx == 0), key=f"tf_prev_{idx}"):
            st.session_state.tf_index -= 1
            st.rerun()
    with col2:
        if st.button("Next", disabled=(idx == len(tf_questions) - 1), key=f"tf_next_{idx}"):
            st.session_state.tf_index += 1
            st.rerun()
    with col3:
        if st.button("Show Score", key="tf_show_score"):
            score = sum(
                1 for i, q in enumerate(st.session_state.tf_shuffled)
                if st.session_state.tf_answers[i] == q["answer"]
            )
            st.success(f"Your score: {score} / {len(tf_questions)}")

# ------------------- TAB 2 -------------------
with tab2:
    st.header("Verb Form Quiz (Level 1)")

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
    correct = current[mode]

    label = "Past" if mode == "past" else "Past Participle"
    st.markdown(f"### {current['base']} ({label})")

    user_input = st.text_input("Type your answer:", key=f"verb_input_{i}")
    if st.button("Submit Answer", key=f"verb_submit_btn_{i}"):
        st.session_state.verb_answers[i] = user_input.strip().lower()
        if user_input.strip().lower() == correct:
            st.success("Correct!")
        else:
            st.error(f"Incorrect. Correct answer: **{correct}**")

    c1, c2, c3 = st.columns(3)
    with c1:
        if st.button("Previous", disabled=(i == 0), key=f"verb_prev_{i}"):
            st.session_state.verb_index -= 1
            st.rerun()
    with c2:
        if st.button("Next", disabled=(i == len(verb_data) - 1), key=f"verb_next_{i}"):
            st.session_state.verb_index += 1
            st.rerun()
    with c3:
        if st.button("Show Score-Q2", key="verb_score_show"):
            score = sum(
                1 for j, v in enumerate(st.session_state.verb_quiz)
                if st.session_state.verb_answers[j] == v[st.session_state.verb_modes[j]]
            )
            st.success(f"Your score: {score} / {len(verb_data)}")

# ------------------- TAB 3 -------------------
with tab3:
    st.header("Idenfying Sentence Quiz (Level 2)")

    passive_questions = [
        {"sentence": "The cake was baked by my mom.", "correct": True},
        {"sentence": "A new library is being build near the park.", "correct": False},  # 오류 intentional
        {"sentence": "This photo was taken in Paris.", "correct": True},
        {"sentence": "The homework have been completed by all the students.", "correct": False},  # 오류 intentional
        {"sentence": "English is spoken in many countries.", "correct": True},
        {"sentence": "The car was repair yesterday.", "correct": False},  # 오류 intentional
        {"sentence": "These apples will be picked tomorrow.", "correct": True},
        {"sentence": "The movie is directing by a famous filmmaker.", "correct": False},  # 오류 intentional
        {"sentence": "The package had been delivered before noon.", "correct": True},
        {"sentence": "The rules must followed at all times.", "correct": False}  # 오류 intentional
    ]

    if "pv_index" not in st.session_state:
        st.session_state.pv_index = 0
        st.session_state.pv_shuffled = random.sample(passive_questions, len(passive_questions))
        st.session_state.pv_answers = [None] * len(passive_questions)

    i = st.session_state.pv_index
    current_q = st.session_state.pv_shuffled[i]

    st.subheader(f"Question {i + 1} of {len(passive_questions)}")
    st.write(f"**{current_q['sentence']}**")
    answer = st.radio("Is this sentence grammatically correct?", ["Correct", "Incorrect"], key=f"pv_radio_{i}")

    if st.button("Submit Answer", key=f"pv_submit_{i}"):
        user_answer = (answer == "Correct")
        st.session_state.pv_answers[i] = user_answer
        if user_answer == current_q["correct"]:
            st.success("Correct!")
        else:
            st.error("Incorrect.")
            st.info(f"Explanation: This sentence is {'correct' if current_q['correct'] else 'incorrect'}.")

    c1, c2, c3 = st.columns(3)
    with c1:
        if st.button("Previous", disabled=(i == 0), key="pv_prev"):
            st.session_state.pv_index -= 1
            st.rerun()
    with c2:
        if st.button("Next", disabled=(i == len(passive_questions) - 1), key="pv_next"):
            st.session_state.pv_index += 1
            st.rerun()
    with c3:
        if st.button("Show Score", key="pv_score"):
            score = sum(
                1 for j, q in enumerate(st.session_state.pv_shuffled)
                if st.session_state.pv_answers[j] == q["correct"]
            )
            st.success(f"Your score: {score} / {len(passive_questions)}")
    
# ------------------- TAB 4 -------------------
with tab4:
    st.header("Paragraph TF - Coming Soon")
    st.write("You can add paragraph-based True/False questions here later.")
