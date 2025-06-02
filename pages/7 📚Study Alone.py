import streamlit as st
import random
from gtts import gTTS
from io import BytesIO
import re

st.set_page_config(page_title="📚Study Alone", layout="wide")

st.title("📚Study Alone")

# Define tabs
tab1, tab2, tab3 = st.tabs(["Guidelines", "Memorization of the text", "a"])

with tab1:
    st.title("Guidelines")
    st.write("This section will provide guidelines on how to use the application effectively.")

with tab2:
    import streamlit as st

st.set_page_config(page_title="Passive Practice", page_icon="📝") 
st.title("Memorization of the Text")

    # Text passage
    text = """In the small town of Willowby, there stood an old library that was rumored to be enchanted. Every night at midnight, the books inside would whisper stories to each other, bringing their characters to life. One evening, Sarah, a curious 15-year-old book lover, decided to sneak into the library to see if the rumors were true.

    As the clock struck twelve, the books began to rustle. To Sarah's amazement, characters stepped out of their pages. She met Alice from Wonderland, the White Rabbit, and even pirates from Treasure Island. They invited her to join their midnight council, where they discussed the tales of their adventures and the wisdom they contained.

    Sarah spent the whole night listening and learning from the characters, promising to keep their secret. As dawn approached, they returned to their pages. Sarah left the library, inspired and filled with stories to tell, forever changed by the magic of the Midnight Library.
    """

    # Difficulty selection
    difficulty = st.selectbox("Select Difficulty", ["Easy", "Normal", "Hard"])

    # Set blank ratio based on difficulty
    blank_ratio = {"Easy": 0.15, "Normal": 0.30, "Hard": 0.50}[difficulty]

    # Split text into words and create blanks
    words = text.split()
    num_blanks = int(len(words) * blank_ratio)
    blank_indices = sorted(random.sample(range(len(words)), num_blanks))

    # Process words to create blanks
    answer_words = []
    processed_words = []
    for i, word in enumerate(words):
        if i in blank_indices:
            stripped = word.strip(".,!?;:")
            suffix = word[len(stripped):]
            answer_words.append(stripped)
            blank = "_____" + suffix
            processed_words.append(blank)
        else:
            processed_words.append(word)

    # Display text with blanks
    st.markdown(" ".join(processed_words))

    # Collect user input
    user_input = st.text_input("Enter the words for the blanks, separated by commas (e.g., Willowby,Sarah,books,...)")

    if st.button("Submit"):
        user_answers = [w.strip() for w in user_input.split(",")]

        st.subheader("Check Your Answers")
        for idx, (correct, user) in enumerate(zip(answer_words, user_answers)):
            if correct.lower() == user.lower():
                st.markdown(f"✅ **{idx+1}. {user}** (Correct)")
            else:
                st.markdown(f"❌ **{idx+1}. {user}** → Correct answer: **{correct}**")

        if len(user_answers) < len(answer_words):
            st.warning(f"❗ You have entered fewer words. There are {len(answer_words)} blanks.")
        elif len(user_answers) > len(answer_words):
            st.warning(f"❗ You have entered too many words. There are {len(answer_words)} blanks.")
        else:
            score = sum([a.lower() == b.lower() for a, b in zip(answer_words, user_answers)])
            st.success(f"Correct Answers: {score} / {len(answer_words)}")

with tab3:
import streamlit as st

# ✅ 반드시 맨 위에 있어야 함
st.set_page_config(page_title="Passive Practice", page_icon="📝")
st.title("📝 Active to Passive Practice")

# 예문 리스트
examples = [
    "Tom eats an apple.",
    "She wrote a letter.",
    "They make cookies.",
    "He buys a car.",
    "We saw a movie.",
    "I took a picture.",
    "I did the homework.",
    "The chef made a cake.",
    "A student found the book.",
    "The teacher sent a message."
]

# 동사의 과거형 → 과거분사
past_to_pp = {
    "ate": "eaten", "wrote": "written", "saw": "seen", "made": "made",
    "took": "taken", "did": "done", "bought": "bought", "found": "found",
    "sent": "sent", "read": "read", "said": "said", "went": "gone", "gave": "given", "make": "made"
}

# 동사의 기본형 → 과거분사
base_to_pp = {
    "eat": "eaten", "write": "written", "see": "seen", "make": "made",
    "take": "taken", "do": "done", "buy": "bought", "find": "found",
    "send": "sent", "read": "read", "say": "said", "go": "gone", "give": "given"
}

# 주어를 목적격으로 바꾸는 사전
subject_to_object = {
    "I": "me", "He": "him", "She": "her", "It": "it",
    "We": "us", "They": "them", "You": "you",
    "Tom": "Tom", "John": "John", "Mary": "Mary",
    "The teacher": "the teacher", "The chef": "the chef", "A student": "a student"
}

# 상태 저장
if "index" not in st.session_state:
    st.session_state.index = 0
if "current_sentence" not in st.session_state:
    st.session_state.current_sentence = examples[0]
if "show_passive" not in st.session_state:
    st.session_state.show_passive = False

# 버튼 UI
col1, col2 = st.columns(2)
with col1:
    if st.button("🔄 Show Passive"):
        st.session_state.show_passive = True
with col2:
    if st.button("➡️ Next Sentence"):
        st.session_state.index = (st.session_state.index + 1) % len(examples)
        st.session_state.current_sentence = examples[st.session_state.index]
        st.session_state.show_passive = False

# 현재 문장
current = st.session_state.current_sentence
st.markdown(f"<h3 style='font-size:28px;'>✏️ Active Sentence: {current}</h3>", unsafe_allow_html=True)

# 수동태로 변환하는 함수
def convert_to_passive(sentence):
    sentence = sentence.strip().rstrip(".")
    words = sentence.split()

    if words[0].lower() in ["the", "a", "an"]:
        subject = f"{words[0]} {words[1]}"
        verb = words[2]
        obj_words = words[3:]
    else:
        subject = words[0]
        verb = words[1]
        obj_words = words[2:]

    obj = " ".join(obj_words)
    plural_subjects = ["they", "we", "you"]
    is_plural = any(plural in subject.lower() for plural in plural_subjects)

    if verb in past_to_pp:
        be = "were" if is_plural else "was"
        past_participle = past_to_pp[verb]
    elif verb.endswith("s"):
        base = verb[:-1]
        be = "are" if is_plural else "is"
        past_participle = base_to_pp.get(base, base + "ed")
    elif verb.endswith("ed"):
        be = "were" if is_plural else "was"
        past_participle = verb
    else:
        return None, f"❗ Unknown verb: '{verb}'"

    subject_key = subject.strip().capitalize()
    object_form = subject_to_object.get(subject_key, subject)

    passive = f"{obj.capitalize()} {be} {past_participle} by {object_form}."
    explanation = (
        f"➡ Subject = **{subject}** → **by {object_form}** (objective form)\n"
        f"➡ Verb = **{verb}** → Past participle = **{past_participle}**\n"
        f"➡ Object = **{obj}** → becomes the subject in passive\n"
        f"➡ Passive = **{passive}**"
    )
    return passive, explanation

# 수동태 표시
if st.session_state.show_passive:
    result, explanation = convert_to_passive(current)
    if result:
        st.markdown(f"<h3 style='font-size:28px;'>✅ Passive Sentence: {result}</h3>", unsafe_allow_html=True)
        st.markdown(f"### 🧠 Explanation:\n{explanation}")
    else:
        st.warning(explanation)
