import streamlit as st

st.set_page_config(page_title="Font Size Scaler", layout="centered")

st.title("🧭 How to Use This App")

# Section 1: Voca Starter
with st.expander("🌱 1. Voca Starter"):
    st.write("- **Word List**: View and study target words with definitions.")
    st.write("- **Meaning Master**: Match words with their meanings.")
    st.write("- **Spelling Master**: Type and spell each word correctly to reinforce memory.")

# Section 2: Grammar
with st.expander("🌿 2. Grammar"):
    st.write("- **Grammar Concept**: Read the text that explains what passive is.")
    st.write("- **Video Explanations**: Watch short, clear videos explaining grammar rules with text.")
    st.write("- **Drawing Activity**: Use an interactive canvas to visualize grammar concepts (e.g., sentence structure, parts of speech).")

# Section 3: Passage Reading
with st.expander("🌳 3. Passage Reading"):
    st.write("- **TTS(Text to Speech)**: Listen to the full passage. Students can opt to see text and translation or not.")
    st.write("- **Sentence Reader**: Listen to native-like pronunciation, sentence by sentence.")

# Section 4: Quiz
with st.expander("🌲 4. Quiz"):
    st.write("- **True or False**: Test comprehension with simple factual statements.")
    st.write("- **Level 1 / 2 / 3 Quizzes**: Challenge yourself with increasing difficulty.")

# Section 5: Study Alone
with st.expander("📚 5. Study Alone"):
    st.write("- **Memorization of the text**: Revisit reading texts with missing words.")
    st.write("- **Active to Passive practice**: Convert active voice sentences into passive voice interactively.")

st.markdown("---")
st.caption("Made for interactive English learning 🌍")
