import streamlit as st

st.set_page_config(page_title="Font Size Scaler", layout="centered")

st.title("🧭 How to Use This App")

# Font size scaler using a slider
font_size = st.slider("Select Font Size", min_value=12, max_value=40, value=20, step=2)

# Function to display text with different sizes
def display_text_with_size(text, size):
    if size >= 24:
        st.write(f"### {text}")
    else:
        st.write(text)

# Section 1: Voca Starter
with st.expander("🌱 1. Voca Starter"):
    display_text_with_size("- **Word List**: View and study target words with definitions.", font_size)
    display_text_with_size("- **Meaning Master**: Match words with their meanings.", font_size)
    display_text_with_size("- **Spelling Master**: Type and spell each word correctly to reinforce memory.", font_size)

# Section 2: Grammar
with st.expander("🌿 2. Grammar"):
    display_text_with_size("- **Grammar Concept**: Read the text that explains what passive is.", font_size)
    display_text_with_size("- **Video Explanations**: Watch short, clear videos explaining grammar rules with text.", font_size)
    display_text_with_size("- **Drawing Activity**: Use an interactive canvas to visualize grammar concepts (e.g., sentence structure, parts of speech).", font_size)

# Section 3: Passage Reading
with st.expander("🌳 3. Passage Reading"):
    display_text_with_size("- **TTS(Text to Speech)**: Listen to the full passage. Students can opt to see text and translation or not.", font_size)
    display_text_with_size("- **Sentence Reader**: Listen to native-like pronunciation, sentence by sentence.", font_size)

# Section 4: Quiz
with st.expander("🌲 4. Quiz"):
    display_text_with_size("- **True or False**: Test comprehension with simple factual statements.", font_size)
    display_text_with_size("- **Level 1 / 2 / 3 Quizzes**: Challenge yourself with increasing difficulty.", font_size)

# Section 5: Study Alone
with st.expander("📚 5. Study Alone"):
    display_text_with_size("- **Memorization of the text**: Revisit reading texts with missing words.", font_size)
    display_text_with_size("- **Active to Passive practice**: Convert active voice sentences into passive voice interactively.", font_size)

st.markdown("---")
st.caption("Made for interactive English learning 🌍")
