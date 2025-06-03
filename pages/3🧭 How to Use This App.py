import streamlit as st

st.set_page_config(page_title="Font Size Scaler", layout="centered")

st.title("🧭 How to Use This App")

# Section 1: Voca Starter
with st.expander("🌱 1. Voca Starter"):
    ("- **Word List**: View and study target words with definitions.", font_size)
    ("- **Meaning Master**: Match words with their meanings.", font_size)
    ("- **Spelling Master**: Type and spell each word correctly to reinforce memory.", font_size)

# Section 2: Grammar
with st.expander("🌿 2. Grammar"):
    ("- **Grammar Concept**: Read the text that explains what passive is.", font_size)
    ("- **Video Explanations**: Watch short, clear videos explaining grammar rules with text.", font_size)
    ("- **Drawing Activity**: Use an interactive canvas to visualize grammar concepts (e.g., sentence structure, parts of speech).", font_size)

# Section 3: Passage Reading
with st.expander("🌳 3. Passage Reading"):
    ("- **TTS(Text to Speech)**: Listen to the full passage. Students can opt to see text and translation or not.", font_size)
    ("- **Sentence Reader**: Listen to native-like pronunciation, sentence by sentence.", font_size)

# Section 4: Quiz
with st.expander("🌲 4. Quiz"):
    ("- **True or False**: Test comprehension with simple factual statements.", font_size)
    ("- **Level 1 / 2 / 3 Quizzes**: Challenge yourself with increasing difficulty.", font_size)

# Section 5: Study Alone
with st.expander("📚 5. Study Alone"):
    ("- **Memorization of the text**: Revisit reading texts with missing words.", font_size)
    ("- **Active to Passive practice**: Convert active voice sentences into passive voice interactively.", font_size)

st.markdown("---")
st.caption("Made for interactive English learning 🌍")
