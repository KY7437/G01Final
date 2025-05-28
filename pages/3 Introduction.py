import streamlit as st
import pandas as pd
from gtts import gTTS
from io import BytesIO
import tempfile

st.write("🌱 Vocabulary Learning")

# Define tabs
tab1, tab2, tab3 = st.tabs(["❄️ Word List", "❄️ Knowledge Map", "❄️ Role Playing"])

with tab1:
    st.markdown("### 📋 Word List")

    # Load CSV from GitHub
    url = "https://raw.githubusercontent.com/KY7437/G01Final/refs/heads/main/wordlist.csv"
    try:
        df = pd.read_csv(url)
        if st.button("Show Word List"):
            st.dataframe(df, use_container_width=True)
    except Exception as e:
        st.error(f"Error loading word list: {e}")

with tab2:
    st.markdown("### 🧠 Knowledge Map")
    st.write("Knowledge Map functionality is under development.")
import streamlit as st
import openai
from pyvis.network import Network
import networkx as nx
import os
import tempfile

# 🔑 OpenAI API Key 설정
openai.api_key = st.secrets["OPENAI_API_KEY"] if "OPENAI_API_KEY" in st.secrets else "sk-여기에_키_붙여넣기"

# 🌐 GPT로 관련 개념 받아오기
def get_related_words(word):
    prompt = f'Give me 8 conceptually related English words to "{word}" as a JSON list.'
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7
    )
    content = response['choices'][0]['message']['content']
    try:
        return eval(content)
    except:
        return []

# 🕸️ 지식 연결 지도 만들기
def create_knowledge_map(center_word, related_words):
    G = nx.Graph()
    G.add_node(center_word)
    for w in related_words:
        G.add_node(w)
        G.add_edge(center_word, w)

    net = Network(height="600px", width="100%", bgcolor="#ffffff", font_color="black")
    net.from_nx(G)
    return net

# 🖼️ HTML로 시각화
def show_map_in_streamlit(net):
    with tempfile.NamedTemporaryFile(delete=False, suffix=".html") as f:
        path = f.name
        net.save_graph(path)
        with open(path, 'r', encoding='utf-8') as file:
            html = file.read()
        st.components.v1.html(html, height=620, scrolling=True)

# 🎯 Streamlit UI 구성
st.title("🧠 지식 연결 지도 앱")
keyword = st.text_input("Enter a keyword (English):", "")

if st.button("Generate Knowledge Map") and keyword:
    with st.spinner("GPT로 관련 개념을 불러오는 중..."):
        related = get_related_words(keyword)
        if related:
            st.success(f"'{keyword}'와 관련된 개념: {', '.join(related)}")
            net = create_knowledge_map(keyword, related)
            show_map_in_streamlit(net)
        else:
            st.error("관련 단어를 불러오는 데 실패했습니다.")
