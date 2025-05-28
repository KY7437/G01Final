import streamlit as st
import pandas as pd
from gtts import gTTS
from io import BytesIO
import random
import tempfile

st.write("🌱 Vocabulary learning")

# Define tabs
tab1, tab2, tab3 = st.tabs(["❄️ Word List", "❄️ 2. Wordle", "❄️ 3. Role Playing"])

with tab1:
    st.markdown("### 📋 Word List")

    # Load CSV from GitHub
    url = "https://raw.githubusercontent.com/KY7437/G01Final/refs/heads/main/wordlist.csv"
    df = pd.read_csv(url)

    # Show table only when button is clicked
    if st.button("Show Word List"):
        st.dataframe(df, use_container_width=True)

with tab2:

    npm install vis-network

 <!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <title>Knowledge Map</title>
  <script src="https://unpkg.com/vis-network/standalone/umd/vis-network.min.js"></script>
  <style>
    #network { width: 100%; height: 600px; border: 1px solid lightgray; }
  </style>
</head>
<body>

<h2>🧠 지식 연결 지도 (Knowledge Map)</h2>
<input type="text" id="keyword" placeholder="Enter a word (e.g., evolution)" />
<button onclick="generateMap()">Generate Map</button>

<div id="network"></div>

<script>
const OPENAI_API_KEY = "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"; // 여기에 본인 API 키 넣기

async function getRelatedConcepts(word) {
  const prompt = `Give me 8 related concepts to the English word "${word}" in JSON array format. Example: ["biology", "Darwin", "natural selection"]`;

  const res = await fetch("https://api.openai.com/v1/chat/completions", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "Authorization": `Bearer ${OPENAI_API_KEY}`
    },
    body: JSON.stringify({
      model: "gpt-4",
      messages: [{ role: "user", content: prompt }],
      temperature: 0.7
    })
  });

  const data = await res.json();
  try {
    return JSON.parse(data.choices[0].message.content);
  } catch (e) {
    console.error("GPT 응답 파싱 오류:", data);
    return [];
  }
}

async function generateMap() {
  const word = document.getElementById("keyword").value.trim();
  if (!word) return alert("Please enter a word!");

  const related = await getRelatedConcepts(word);
  const nodes = [{ id: 0, label: word, color: '#ffcc00' }];
  const edges = [];

  related.forEach((item, i) => {
    nodes.push({ id: i + 1, label: item });
    edges.push({ from: 0, to: i + 1 });
  });

  const container = document.getElementById("network");
  const data = { nodes: new vis.DataSet(nodes), edges: new vis.DataSet(edges) };
  const options = { nodes: { shape: "dot", size: 20 }, physics: { stabilization: false } };
  new vis.Network(container, data, options);
}
</script>

</body>
</html>



with tab3:
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
        st.session_state["show_text"] = True

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
