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
    import tkinter as tk

# 🔤 단어 리스트 (단어, 뜻)
word_list = [
    ("apple", "사과"),
    ("run", "달리다"),
    ("book", "책"),
    ("happy", "행복한"),
    ("teacher", "선생님"),
    ("water", "물"),
]

class FlashcardApp:
    def __init__(self, root):
        self.root = root
        self.root.title("🃏 영어 단어 카드 뒤집기 게임")
        self.cards = []

        # 🧱 카드 프레임
        self.frame = tk.Frame(root, bg="white")
        self.frame.pack(padx=20, pady=20)

        self.create_cards()

        # 🔁 리셋 버튼
        reset_btn = tk.Button(root, text="🔄 전체 리셋", command=self.reset_cards, font=("Arial", 12))
        reset_btn.pack(pady=10)

    def create_cards(self):
        for idx, (word, meaning) in enumerate(word_list):
            card = tk.Button(
                self.frame,
                text=word,
                width=20,
                height=3,
                font=("Arial", 14),
                relief="raised",
                bg="#f2f2f2",
                command=lambda i=idx: self.flip_card(i)
            )
            row = idx // 3
            col = idx % 3
            card.grid(row=row, column=col, padx=10, pady=10)
            self.cards.append({"button": card, "word": word, "meaning": meaning, "flipped": False})

    def flip_card(self, index):
        card = self.cards[index]
        if card["flipped"]:
            card["button"]["text"] = card["word"]
            card["flipped"] = False
        else:
            card["button"]["text"] = card["meaning"]
            card["flipped"] = True

    def reset_cards(self):
        for card in self.cards:
            card["button"]["text"] = card["word"]
            card["flipped"] = False

# 🎬 실행
if __name__ == "__main__":
    root = tk.Tk()
    app = FlashcardApp(root)
    root.mainloop()

with tab3:
    vocabulary_quiz("Meaning Master", "meaning")

with tab4:
    vocabulary_quiz("Spelling Master", "spelling")
