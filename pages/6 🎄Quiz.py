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
    st.markdown("Enter the preterite form of the verb above.")

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
    st.markdown("Check the grammaticality of the sentence.")

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
    st.header("Fill in the Blank Quiz (Level 3)")
    st.markdown("Choose the right verb from among four options")

    fill_questions = [
        {
            "sentence": "The book ( ___ ) that the king was happy.",
            "options": ["Say", "Said", "is said", "Saying"],
            "answer": "is said",
            "explanation": "The phrase 'The book is said that...' is a common passive structure used to express reported speech."
        },
        {
            "sentence": "A decision ( ___ ) since Holiday.",
            "options": ["made", "makes", "was made", "has been made"],
            "answer": "has been made",
            "explanation": "'Has been made' is present perfect passive, appropriate since the time is 'since Holiday'."
        },
        {
            "sentence": "My hamburger will ( ___ ) tomorrow.",
            "options": ["deliver", "delivered", "be delivered", "be delivering"],
            "answer": "be delivered",
            "explanation": "Future passive voice: 'will be delivered'."
        },
        {
            "sentence": "He ( ___ ) the cabin with own hands.",
            "options": ["built", "build", "is built", "building"],
            "answer": "built",
            "explanation": "This is active voice, simple past. The subject 'he' performed the action."
        },
        {
            "sentence": "The hat ( ___ ) is on the chair now.",
            "options": ["washes", "washed", "washing", "is washed"],
            "answer": "washed",
            "explanation": "'The hat washed' acts as a reduced relative clause. It means 'The hat that was washed...'."
        },
        {
            "sentence": "Teams ( ___ ) the project early.",
            "options": ["completed", "are completed", "to complete", "will be completed"],
            "answer": "completed",
            "explanation": "Active voice: 'Teams completed the project' is grammatically correct and natural."
        },
        {
            "sentence": "The invitation ( ___ ) last week.",
            "options": ["sent", "is sent", "was sent", "to sending"],
            "answer": "was sent",
            "explanation": "'Was sent' is past simple passive. 'Last week' suggests a completed past action."
        },
        {
            "sentence": "Those shoes ( ___ ) in Italy.",
            "options": ["made", "were made", "are making", "have made"],
            "answer": "were made",
            "explanation": "Passive voice past tense: 'were made'. The sentence tells about origin."
        },
        {
            "sentence": "My father thought that the cookies ( ___ ) this morning.",
            "options": ["baked", "is baking", "were made", "to make"],
            "answer": "were made",
            "explanation": "'The cookies were made' is passive in the past, matching with 'this morning'."
        },
        {
            "sentence": "She ( ___ ) the car right now.",
            "options": ["washed", "is washing", "will be washing", "should be washed"],
            "answer": "is washing",
            "explanation": "'Is washing' is present continuous active voice, and matches 'right now'."
        },
    ]

    if "fill_index" not in st.session_state:
        st.session_state.fill_index = 0
        st.session_state.fill_shuffled = random.sample(fill_questions, len(fill_questions))
        st.session_state.fill_answers = [None] * len(fill_questions)

    i = st.session_state.fill_index
    current_q = st.session_state.fill_shuffled[i]

    st.subheader(f"Question {i + 1} of {len(fill_questions)}")
    st.markdown(f"### {current_q['sentence']}")

    answer = st.radio("Choose the correct answer:", current_q["options"], key=f"fill_radio_{i}")

    if st.button("Submit Answer", key=f"fill_submit_{i}"):
        st.session_state.fill_answers[i] = answer
        if answer == current_q["answer"]:
            st.success("Correct!")
        else:
            st.error(f"Incorrect. Correct answer: **{current_q['answer']}**")
        st.info(f"**Explanation:** {current_q['explanation']}")

    c1, c2, c3 = st.columns(3)
    with c1:
        if st.button("Previous", disabled=(i == 0), key="fill_prev"):
            st.session_state.fill_index -= 1
            st.rerun()
    with c2:
        if st.button("Next", disabled=(i == len(fill_questions) - 1), key="fill_next"):
            st.session_state.fill_index += 1
            st.rerun()
    with c3:
        if st.button("Show Score", key="fill_score"):
            score = sum(
                1 for j, q in enumerate(st.session_state.fill_shuffled)
                if st.session_state.fill_answers[j] == q["answer"]
            )
            st.success(f"Your score: {score} / {len(fill_questions)}")
