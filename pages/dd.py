import streamlit as st
import random

st.set_page_config(page_title="빈칸 영어 본문 학습", layout="wide")

# 본문 텍스트
text = """In the small town of *Willowby*, there stood an old library that was rumored to be enchanted. Every night at midnight, the books inside would whisper stories to each other, bringing their characters to life. One evening, **Sarah**, a curious 15-year-old book lover, decided to sneak into the library to see if the rumors were true.

As the clock struck twelve, the books began to rustle. To Sarah's amazement, characters stepped out of their pages. She met **Alice** from Wonderland, **the White Rabbit**, and even **pirates** from Treasure Island. They invited her to join their midnight council, where they discussed the tales of their adventures and the wisdom they contained.

Sarah spent the whole night listening and learning from the characters, promising to keep their secret. As dawn approached, they returned to their pages. Sarah left the library, inspired and filled with stories to tell, forever changed by the magic of the Midnight Library.
"""

# ✅ 난이도 선택
difficulty = st.selectbox("난이도 선택", ["Easy", "Normal", "Hard"])

# ✅ 난이도별 빈칸 개수 비율 설정
if difficulty == "Easy":
    blank_ratio = 0.15
elif difficulty == "Normal":
    blank_ratio = 0.30
else:  # Hard
    blank_ratio = 0.50

# ✅ 단어 리스트로 분리
words = text.split()
word_indices = list(range(len(words)))
num_blanks = int(len(words) * blank_ratio)

# ✅ 무작위로 빈칸 만들 단어 선택
blank_indices = sorted(random.sample(word_indices, num_blanks))

# ✅ 빈칸 처리 + 단서 버튼 추가
processed_words = []
for i, word in enumerate(words):
    if i in blank_indices:
        clean_word = word.strip(".,!?;:")  # 특수문자 제거
        suffix = word[len(clean_word):]  # 문장 부호 등 유지
        hint = clean_word[0] if clean_word else ""

        col1, col2 = st.columns([3, 1])
        with col1:
            st.markdown(f"**_____**{suffix}", unsafe_allow_html=True)
        with col2:
            if st.button("힌트", key=f"hint_{i}"):
                st.markdown(f"`{hint}`")
    else:
        st.write(word, end=" ")

# ✅ CSS 스타일 적용 (선택적)
st.markdown(
    """
    <style>
    div[data-testid="column"] {
        display: inline-block;
        margin: 4px 6px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)
