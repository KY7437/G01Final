import streamlit as st
from gtts import gTTS
import tempfile
from streamlit_drawable_canvas import st_canvas
import numpy as np

# Define tabs
tab1, tab2, tab3, tab4 = st.tabs(["🔍 Guidelines", "🍃 Grammar Concept", "🍃 Role Play", "🍃 Drawing Activity"])

with tab1:
    st.title("Guidelines")

with tab2:
    st.title("Passives")
    st.markdown("Raymond Murphy, (2019). English Grammar in Use, Cambridge, p. 84")
    
    # Font size scaler
    font_size = st.slider("Select Font Size", min_value=12, max_value=40, value=20, step=2)

    # Apply the selected font size
    st.markdown(f"""
        <style>
        .passive-text {{
            font-size: {font_size}px !important;
        }}
        </style>
        """, unsafe_allow_html=True)

    st.markdown("""
        <div class="passive-text">
        Be verb plus participle<br>
        In this section, we will take a look about the passives.<br><br>
        When we use an <strong>active verb</strong>, we say <strong>what the subject does</strong>: <br>
        - My grandfather was a builder. He built this house in 1981.<br>
        - It’s a big company. It employs two hundred people.<br><br>
        When we use a <strong>passive verb</strong>, we say <strong>what happens to the subject</strong>:<br>
        - ‘How old is this house?’ ‘It was built in 1981.’<br>
        - Two hundred people are employed by the company.<br><br>
        When we use the passive, who or what causes the action is often unknown or unimportant:<br>
        - A lot of money was stolen in the robbery. (somebody stole it, but we don’t know who)<br>
        - Is this room cleaned every day? (does somebody clean it? – it’s not important who)<br><br>
        If we want to say who does or what causes the action, we use <strong>by</strong>:<br>
        - This house was built <strong>by my grandfather</strong>.<br>
        - Two hundred people are employed <strong>by the company</strong>.<br><br>
        The passive is be (is/was etc.) + past participle (done/cleaned/seen etc.):<br>
        (be) done (be) cleaned (be) damaged (be) built (be) seen etc.<br><br>
        The past participle often ends in -ed (cleaned/damaged etc.), but many important verbs are irregular (built/done/stolen etc.). To practice irregular forms more, go to Voca Starter and use the app deployed on tab 3.
        </div>
    """, unsafe_allow_html=True)

with tab3:
    st.title("Role Play")
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
    st.title("🎭 Roleplay Dialog App")
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

with tab4:
    st.title("Drawing Activity")

    def main():
        st.title("Drawing")

        # 사용자 입력 위젯
        stroke_width = st.slider("선 굵기", min_value=1, max_value=25, value=5)
        stroke_color = st.color_picker("선 색깔", "#000000")

        canvas_result = st_canvas(
            fill_color="rgba(255, 165, 0, 0.3)",  # 투명 오렌지색 배경
            stroke_width=stroke_width,
            stroke_color=stroke_color,
            background_color="#eeeeee",
            height=400,
            width=600,
            drawing_mode="freedraw",
            key="canvas",
        )

        if canvas_result.image_data is not None:
            img = canvas_result.image_data.astype(np.uint8)
            st.image(img)

    if __name__ == "__main__":
        main()
