import streamlit as st

st.set_page_config(page_title="How to Use This App", layout="centered")

st.title("🧭 How to Use This App")

# Section 1: Voca Starter
with st.expander("🌱 1. Voca Starter"):
    st.markdown("""
- **Word List**: View and study target words with definitions.  
- **Meaning Master**: Match words with their meanings.  
- **Spelling Master**: Type and spell each word correctly to reinforce memory.
    """)

# Section 2: Grammar
with st.expander("🌿 2. Grammar"):
    st.markdown("""
- **Grammar Concept**: Read the text that explains what passive is.
- **Video Explanations**: Watch short, clear videos explaining grammar rules with text.  
- **Drawing Activity**: Use an interactive canvas to visualize grammar concepts (e.g., sentence structure, parts of speech).
    """)

# Section 3: Passage Reading
with st.expander("🌳 3. Passage Reading"):
    st.markdown("""
- **TTS(Text to Speech)**: Listen to the full passage. Students can opt to see text and translation or not.
- **Setence Reader**: Listen to native-like pronunciation, sentence by sentence.
    """)

# Section 4: Quiz
with st.expander("🌲 4. Quiz"):
    st.markdown("""
- **True or False**: Test comprehension with simple factual statements.  
- **Level 1 / 2 / 3 Quizzes**: Challenge yourself with increasing difficulty.
    """)

# Section 5: Study Alone
with st.expander("📚 5. Study Alone"):
    st.markdown("""
- **Memorization of the text**: Revisit reading texts with missing words.   
- **Active to Passive practice**: Convert active voice sentences into passive voice interactively.
    """)

st.markdown("---")
st.caption("Made for interactive English learning 🌍")
