import streamlit as st

st.set_page_config(page_title="Font Size Scaler", layout="centered")

st.title("🧭 How to Use This App")

# Font size scaler using a slider
font_size = st.slider("Select Font Size", min_value=12, max_value=40, value=20, step=2)

# Injecting custom CSS into the app
st.markdown(f"""
    <style>
    .custom-font-size {{
        font-size: {font_size}px !important;
    }}
    </style>
    """, unsafe_allow_html=True)

# Section 1: Voca Starter
with st.expander("🌱 1. Voca Starter"):
    st.markdown("""
    <div class="custom-font-size">
    - **Word List**: View and study target words with definitions.  
    - **Meaning Master**: Match words with their meanings.  
    - **Spelling Master**: Type and spell each word correctly to reinforce memory.
    </div>
    """, unsafe_allow_html=True)

# Section 2: Grammar
with st.expander("🌿 2. Grammar"):
    st.markdown("""
    <div class="custom-font-size">
    - **Grammar Concept**: Read the text that explains what passive is.
    - **Video Explanations**: Watch short, clear videos explaining grammar rules with text.  
    - **Drawing Activity**: Use an interactive canvas to visualize grammar concepts (e.g., sentence structure, parts of speech).
    </div>
    """, unsafe_allow_html=True)

# Section 3: Passage Reading
with st.expander("🌳 3. Passage Reading"):
    st.markdown("""
    <div class="custom-font-size">
    - **TTS(Text to Speech)**: Listen to the full passage. Students can opt to see text and translation or not.
    - **Sentence Reader**: Listen to native-like pronunciation, sentence by sentence.
    </div>
    """, unsafe_allow_html=True)

# Section 4: Quiz
with st.expander("🌲 4. Quiz"):
    st.markdown("""
    <div class="custom-font-size">
    - **True or False**: Test comprehension with simple factual statements.  
    - **Level 1 / 2 / 3 Quizzes**: Challenge yourself with increasing difficulty.
    </div>
    """, unsafe_allow_html=True)

# Section 5: Study Alone
with st.expander("📚 5. Study Alone"):
    st.markdown("""
    <div class="custom-font-size">
    - **Memorization of the text**: Revisit reading texts with missing words.   
    - **Active to Passive practice**: Convert active voice sentences into passive voice interactively.
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")
st.caption("Made for interactive English learning 🌍")
