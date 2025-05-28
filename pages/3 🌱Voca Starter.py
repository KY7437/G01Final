import streamlit as st
import pandas as pd
from gtts import gTTS
from io import BytesIO
import random
import tempfile
import openai
from pyvis.network import Network
import networkx as nx

# 🔑 Set OpenAI API Key
openai.api_key = st.secrets["OPENAI_API_KEY"]

# Define tabs
tab1, tab2, tab3, tab4 = st.tabs(["❄️ Word List", "❄️ Knowledge Map", "❄️ Meaning Master", "❄️ Spelling Master"])

with tab1:
    st.markdown("### 📋 Word List")

    # Load CSV from GitHub
    url = "https://raw.githubusercontent.com/KY7437/G01Final/main/wordlist.csv"
    try:
        df = pd.read_csv(url)
        if st.button("Show Word List"):
            st.dataframe(df, use_container_width=True)
    except Exception as e:
        st.error(f"Error loading word list: {e}")

with tab2:
    st.markdown("### 🧠 Knowledge Map")
    
    # 🌐 Fetch related concepts with GPT
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

    # 🕸️ Create knowledge map
    def create_knowledge_map(center_word, related_words):
        G = nx.Graph()
        G.add_node(center_word)
        for w in related_words:
            G.add_node(w)
            G.add_edge(center_word, w)

        net = Network(height="600px", width="100%", bgcolor="#ffffff", font_color="black")
        net.from_nx(G)
        return net

    # 🖼️ Display map in Streamlit
    def show_map_in_streamlit(net):
        with tempfile.NamedTemporaryFile(delete=False, suffix=".html") as f:
            path = f.name
            net.save_graph(path)
            with open(path, 'r', encoding='utf-8') as file:
                html = file.read()
            st.components.v1.html(html, height=620, scrolling=True)

    st.title("🧠 Knowledge Map App")
    keyword = st.text_input("Enter a keyword (English):", "")

    if st.button("Generate Knowledge Map") and keyword:
        with st.spinner("Fetching related concepts..."):
            related = get_related_words(keyword)
            if related:
                st.success(f"Concepts related to '{keyword}': {', '.join(related)}")
                net = create_knowledge_map(keyword, related)
                show_map_in_streamlit(net)
            else:
                st.error("Failed to fetch related words.")

def load_vocab():
    url = "https://raw.githubusercontent.com/KY7437/G01Final/main/wordlist.csv"
    df = pd.read_csv(url)
    vocab_dict = dict(zip(df["Word"], df["Meaning"])) 
    return vocab_dict

vocab = load_vocab()

def vocabulary_quiz(tab_name, question_type):
    st.header(tab_name)

    # Initialize session state
    if "quiz_items" not in st.session_state:
        st.session_state.quiz_items = random.sample(list(vocab.items()), 5)
        st.session_state.current_q = 0
        st.session_state.score = 0
        st.session_state.show_result = False
        st.session_state.user_input = ""

    st.title(f"📖 {tab_name} Quiz")

    # Display current question
    if st.session_state.current_q < len(st.session_state.quiz_items):
        if question_type == "meaning":
            word, correct_answer = st.session_state.quiz_items[st.session_state.current_q]
            st.write(f"**Word:** {word}")
            prompt = "Enter the Korean meaning:"
        else:
            correct_answer, meaning = st.session_state.quiz_items[st.session_state.current_q]
            st.write(f"**Meaning:** {meaning}")
            prompt = "Enter the English word:"

        user_input = st.text_input(prompt, key=f"input_{st.session_state.current_q}")

        if st.button("Submit", key=f"submit_{st.session_state.current_q}") and not st.session_state.show_result:
            st.session_state.user_input = user_input.strip().lower()
            st.session_state.show_result = True

        if st.session_state.show_result:
            if st.session_state.user_input == correct_answer.strip().lower():
                st.success("✅ Correct!")
                st.session_state.score += 1
            else:
                st.error(f"❌ Incorrect! The correct answer was **{correct_answer}**.")

            if st.button("Next"):
                st.session_state.current_q += 1
                st.session_state.show_result = False
                st.rerun()

    # Final score
    else:
        st.subheader("🎉 Quiz Finished!")
        st.write(f"Your total score is: **{st.session_state.score} / {len(st.session_state.quiz_items)}**")

        if st.button("Play Again"):
            st.session_state.quiz_items = random.sample(list(vocab.items()), 5)
            st.session_state.current_q = 0
            st.session_state.score = 0
            st.session_state.show_result = False
            st.session_state.user_input = ""
            st.rerun()

with tab3:
    vocabulary_quiz("Meaning Master", "meaning")

with tab4:
    vocabulary_quiz("Spelling Master", "spelling")
