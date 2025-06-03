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
   
    import streamlit as st

    st.title("🎬 What Is the Passive Voice?")

    # iframe을 사용해 영상 크기 조절
    st.markdown("""
    <iframe width="400" height="300" src="https://www.youtube.com/embed/JDuMljo0uik" 
frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
allowfullscreen></iframe>
""", unsafe_allow_html=True)

    st.write("Watch this if you want to learn more about the passive voice!")

with tab3:
    import streamlit as st
    from gtts import gTTS
    import tempfile

    # Grammar expression and dialogue database
    EXPRESSION_DB = {
        "be p.p": {
            "examples": [
                [
                    "A: Did you hear? Our classroom was cleaned yesterday.",
                    "B: Really? It looks so much better now.",
                    "A: Yeah, and new computers were installed this morning.",
                    "B: That’s great! I heard the old ones were broken last week.",
                    "A: Right. The whole room was redesigned by the school’s tech team."
                ],
                [
                    "A: The soccer field was repaired last weekend.",
                    "B: Yeah, I saw that! The grass was replaced too.",
                    "A: It was damaged after the heavy rain, right?",
                    "B: Exactly. Now it looks brand new!"
                ],
                [
                    "A: Did you know the art competition results were announced?",
                    "B: No way! Was my painting chosen?",
                    "A: Yes! Your artwork was selected for first prize!",
                    "B: That’s amazing! I didn’t expect that at all."
                ],
                [
                    "A: Our science project was displayed in the hallway.",
                    "B: I saw it! A lot of students were impressed.",
                    "A: It was presented really well, thanks to your design.",
                    "B: Thanks! I’m glad our effort was noticed."
                ]
            ]
        }
    }

    # Grammar explanation
    EXPRESSION_INFO = {
        "be p.p": {
            "description": (
                "**Passive voice 'be + past participle' (be p.p)** is used when the subject receives the action.\n\n"
                "Example: *The window was broken by the wind.*"
            )
        }
    }

    # Title and intro
    st.title("🎭 Roleplay Dialog App")
    st.markdown("Select a grammar expression and view dialogues with audio. Great for practice and role-play!")

    # Select grammar expression
    expression = "be p.p"  # Only one available now

    # Show grammar explanation
    st.markdown("### 📘 Grammar Explanation")
    st.markdown(EXPRESSION_INFO[expression]["description"])

    # Select dialogue index
    dialogue_list = EXPRESSION_DB[expression]["examples"]
    dialogue_options = [f"Dialogue {i+1}" for i in range(len(dialogue_list))]
    dialogue_index = st.selectbox("🎬 Choose a dialogue:", dialogue_options, index=0)
    selected_dialogue = dialogue_list[dialogue_options.index(dialogue_index)]

    # Audio playback
    if st.button("▶️ Listen to the dialogue"):
        full_text = " ".join(selected_dialogue)
        tts = gTTS(full_text)
        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as fp:
            tts.save(fp.name)
            st.audio(fp.name, format="audio/mp3")

    # Show dialogue text toggle
    if "show_text" not in st.session_state:
        st.session_state["show_text"] = False

    if st.button("👀 Show / Hide the dialogue text"):
        st.session_state["show_text"] = not st.session_state["show_text"]

    if st.session_state["show_text"]:
        col1, col2 = st.columns(2)
        with col1:
            st.subheader("👤 A")
            for line in selected_dialogue:
                if line.startswith("A:"):
                    st.write(line[3:])
                else:
                    st.write("")
        with col2:
            st.subheader("🧑 B")
            for line in selected_dialogue:
                if line.startswith("B:"):
                    st.write(line[3:])
                else:
                    st.write("")



with tab4:
    st.title("Drawing Activity")
    st.write("This section is for the second class activity. Students should aware of essential words, the concept of passives, and comprehenshion of the passage.")

    def main():
        st.header("Draw to describe the provided sentence.")

        # 사용자 입력 위젯
        stroke_width = st.slider("Thickness", min_value=1, max_value=25, value=5)
        stroke_color = st.color_picker("Color", "#000000")

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
