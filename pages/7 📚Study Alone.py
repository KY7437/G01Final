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
    st.title("a")
    st.write("This section is under development.")
