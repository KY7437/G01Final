import streamlit as st
from gtts import gTTS
import os
import re
import tempfile

# Function to split text into sentences
def split_text_into_sentences(text):
    return re.split(r'(?<=[.!?]) +', text)

# Sample passage
passage = """
In the small town of Willowby, there stood an old library that was rumored to be enchanted. 
Every night at midnight, the books inside would whisper stories to each other, bringing their characters to life. 
One evening, Sarah, a curious 15-year-old book lover, decided to sneak into the library to see if the rumors were true.

As the clock struck twelve, the books began to rustle. 
To Sarah's amazement, characters stepped out of their pages. 
She met Alice from Wonderland, the White Rabbit, and even pirates from Treasure Island. 
They invited her to join their midnight council, where they discussed the tales of their adventures and the wisdom they contained.

Sarah spent the whole night listening and learning from the characters, promising to keep their secret. 
As dawn approached, they returned to their pages. 
Sarah left the library, inspired and filled with stories to tell, forever changed by the magic of the Midnight Library.
"""

# Split passage into sentences
sentences = split_text_into_sentences(passage)

# Initialize session state for index
if 'index' not in st.session_state:
    st.session_state.index = 0

# Function to generate TTS for the current sentence
def get_tts():
    sentence = sentences[st.session_state.index]
    tts = gTTS(text=sentence, lang='en')
    tts.save("output.mp3")
    return sentence

# Main function for the Streamlit app
def main():
    st.title("Grammar")

    # Define tabs
    tab1, tab2, tab3, tab4 = st.tabs(["🍃 Grammar Concept", "🍃 Role Play"])

    # Content for the first tab
    with tab1:
        st.header("Passives")
        st.write("Be verb plus participle")

    with tab2:
        st.header("Role Play")
         # Grammar expression and dialogue database
        EXPRESSION_DB = {
            "that": {
                "examples": [
                    "A: Did you watch the movie that I recommended yesterday?",
                    "B: Yes, I did! I loved the part that shows the main character’s childhood.",
                    "A: Me too! The scene that made me cry was at the end.",
                    "B: Same here. I think it’s a movie that everyone should watch."
                ]
            },
            "be p.p": {
                "examples": [
                    "A: Did you hear? Our classroom was cleaned yesterday.",
                    "B: Really? It looks so much better now.",
                    "A: Yeah, and new computers were installed this morning.",
                    "B: That’s great! I heard the old ones were broken last week.",
                    "A: Right. The whole room was redesigned by the school’s tech team."
                ]
            }
        }

        # Grammar explanation
        EXPRESSION_INFO = {
            "that": {
                "description": (
                    "**Relative pronoun 'that'** is used to connect a noun to a clause that gives more information about it.\n\n"
                    "Example: *The book that I read was very interesting.*"
                )
            },
            "be p.p": {
                "description": (
                    "**Passive voice 'be + past participle' (be p.p)** is used when the subject receives the action.\n\n"
                    "Example: *The window was broken by the wind.*"
                )
            }
        }

        # Title
        st.title("🎭Roleplay Dialog App")
        st.markdown("Select a grammar expression to hear a conversation. You can reveal the text if needed!")

        # Select grammar expression
        expression = st.selectbox("🔤 Choose a grammar expression:", list(EXPRESSION_DB.keys()))

        # Display grammar explanation
        st.markdown("### 📘 Grammar Explanation")
        st.markdown(EXPRESSION_INFO[expression]["description"])

        # TTS playback
        if st.button("▶️ Listen to the dialogue"):
            examples = EXPRESSION_DB[expression]["examples"]
            full_text = " ".join(examples)
            tts = gTTS(full_text)
            with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as fp:
                tts.save(fp.name)
                st.audio(fp.name, format="audio/mp3")

            st.session_state["show_text"] = False

        # Show dialogue text
        if "show_text" not in st.session_state:
            st.session_state["show_text"] = False

        if st.button("👀 Show the dialogue text"):
            st.session_state["show_text"] = not st.session_state["show_text"]

        if st.session_state["show_text"]:
            examples = EXPRESSION_DB[expression]["examples"]
            col1, col2 = st.columns(2)
            with col1:
                st.subheader("👤 A")
                for line in examples:
                    if line.startswith("A:"):
                        st.write(line[3:])
                    else:
                        st.write("")
            with col2:
                st.subheader("🧑 B")
                for line in examples:
                    if line.startswith("B:"):
                        st.write(line[3:])
                    else:
                        st.write("")

if __name__ == "__main__":
    main()
