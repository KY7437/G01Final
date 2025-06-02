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
    st.header("Identifying Sentence Quiz (Level 2)")

    passive_questions = [
        {"sentence": "The cake was baked by my mom.", "correct": True, "explanation": "This is a correct passive sentence. It follows the structure: was + past participle."},
        {"sentence": "A new library is being build near the park.", "correct": False, "explanation": "Incorrect. 'build' should be 'built' (past participle)."},
        {"sentence": "This photo was taken in Paris.", "correct": True, "explanation": "Correct use of the passive voice: was + taken (past participle)."},
        {"sentence": "The homework have been completed by all the students.", "correct": False, "explanation": "Incorrect. 'have' should be 'has' because 'homework' is uncountable."},
        {"sentence": "English is spoken in many countries.", "correct": True, "explanation": "This is a correct and common use of the passive voice."},
        {"sentence": "The car was repair yesterday.", "correct": False, "explanation": "Incorrect. 'repair' should be 'repaired' (past participle)."},
        {"sentence": "These apples will be picked tomorrow.", "correct": True, "explanation": "Correct future passive: will be + past participle."},
        {"sentence": "The movie is directing by a famous filmmaker.", "correct": False, "explanation": "Incorrect. 'directing' should be 'directed' (past participle)."},
        {"sentence": "The package had been delivered before noon.", "correct": True, "explanation": "Correct past perfect passive: had been + past participle."},
        {"sentence": "The rules must followed at all times.", "correct": False, "explanation": "Incorrect. Should be 'must be followed' for passive voice."}
    ]

    if "pv_index" not in st.session_state:
        st.session_state.pv_index = 0
        st.session_state.pv_shuffled = random.sample(passive_questions, len(passive_questions))
        st.session_state.pv_answers = [None] * len(passive_questions)

    i = st.session_state.pv_index
    current_q = st.session_state.pv_shuffled[i]

    st.subheader(f"Question {i + 1} of {len(passive_questions)}")
    st.markdown(f"### *{current_q['sentence']}*")  # Bigger, italicized

    answer = st.radio("Is this sentence grammatically correct?", ["Correct", "Incorrect"], key=f"pv_radio_{i}")

    if st.button("Submit Answer", key=f"pv_submit_{i}"):
        user_answer = (answer == "Correct")
        st.session_state.pv_answers[i] = user_answer
        if user_answer == current_q["correct"]:
            st.success("✅ Correct!")
        else:
            st.error("❌ Incorrect.")
        st.info(f"**Explanation:** {current_q['explanation']}")

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
            st.success(f"🏆 Your score: {score} / {len(passive_questions)}")
    
# ------------------- TAB 4 -------------------
with tab4:
    st.header("Filling in The Blank Quiz (Level 3)")

    fill_questions = [
        {
            "sentence": "1. The book (    ) that the king was happy.",
            "options": ["Say", "Said", "is said", "Saying"],
            "answer": "Said",
            "explanation": "The correct past form is 'Said' to match the tense of the sentence."
        },
        {
            "sentence": "2. A decision (   ) since Holiday.",
            "options": ["made", "makes", "was made", "has been made"],
            "answer": "has been made",
            "explanation": "'Has been made' is the correct present perfect passive form."
        },
        {
            "sentence": "3. My hamburger will (   ) tomorrow.",
            "options": ["deliver", "delivered", "be delivered", "be delivering"],
            "answer": "be delivered",
            "explanation": "'Will be delivered' is the correct future passive construction."
        },
        {
            "sentence": "4. He (   ) the cabin with own hands.",
            "options": ["built", "build", "is built", "building"],
            "answer": "built",
            "explanation": "Past simple active voice is required here: 'built'."
        },
        {
            "sentence": "5. The hat (   ) is on the chair now.",
            "options": ["washes", "washed", "washing", "is washed"],
            "answer": "washed",
            "explanation": "'The hat washed' is past participle used as adjective, not a full passive construction."
        },
        {
            "sentence": "6. Teams (   ) the project early.",
            "options": ["completed", "are completed", "to complete", "will be completed"],
            "answer": "completed",
            "explanation": "Simple past active form fits here: 'Teams completed the project.'"
        },
        {
            "sentence": "7. The invitation (   ) last week.",
            "options": ["sent", "is sent", "was sent", "to sending"],
            "answer": "was sent",
            "explanation": "Past passive form: 'was sent' is appropriate for past time marker 'last week'."
        },
        {
            "sentence": "8. Those shoes (   ) in Italy.",
            "options": ["made", "were made", "are making", "have made"],
            "answer": "were made",
            "explanation": "Past passive: 'were made'."
        },
        {
            "sentence": "9. My father thought that the cookies (   ) this morning.",
            "options": ["baked", "is baking", "were made", "to make"],
            "answer": "were made",
            "explanation": "Reported speech in past, so passive past: 'were made'."
        },
        {
            "sentence": "10. She (   ) the car right now.",
            "options": ["washed", "is washing", "will be washing", "should be washed"],
            "answer": "is washing",
            "explanation": "Present continuous active: 'is washing'."
        },
    ]

    if "fill_index" not in st.session_state:
        st.session_state.fill_index = 0
        st.session_state.fill_answers = [None] * len(fill_questions)

    idx = st.session_state.fill_index
    q = fill_questions[idx]

    st.subheader(f"Question {idx + 1} of {len(fill_questions)}")
    st.markdown(f"### {q['sentence']}")

    choice = st.radio("Choose the correct answer:", q["options"], key=f"fill_radio_{idx}")

    if st.button("Submit Answer", key=f"fill_submit_{idx}"):
        st.session_state.fill_answers[idx] = choice
        if choice == q["answer"]:
            st.success("✅ Correct!")
        else:
            st.error("❌ Incorrect.")
        st.info(f"**Explanation:** {q['explanation']}")

    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("Previous", disabled=(idx == 0), key="fill_prev"):
            st.session_state.fill_index -= 1
            st.rerun()
    with col2:
        if st.button("Next", disabled=(idx == len(fill_questions) - 1), key="fill_next"):
            st.session_state.fill_index += 1
            st.rerun()
    with col3:
        if st.button("Show Score", key="fill_score"):
            score = sum(
                1 for i, q in enumerate(fill_questions)
                if st.session_state.fill_answers[i] == q["answer"]
            )
            st.success(f"🏆 Your score: {score} / {len(fill_questions)}")
