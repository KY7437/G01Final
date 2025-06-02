import streamlit as st
from gtts import gTTS
from io import BytesIO
import re

st.title("📚Study Alone")

# Define tabs
tab1, tab2, tab3 = st.tabs(["Guildlines", "Memorization of the text", "a"])

with tab1: 
  st.title("Guidelines")

with tab2:
  st.title("Memorization of the text")
  import streamlit as st
import random

st.set_page_config(page_title="빈칸 영어 본문 학습", layout="wide")

# 본문 텍스트
text = """In the small town of Willowby, there stood an old library that was rumored to be enchanted. Every night at midnight, the books inside would whisper stories to each other, bringing their characters to life. One evening, Sarah, a curious 15-year-old book lover, decided to sneak into the library to see if the rumors were true.

As the clock struck twelve, the books began to rustle. To Sarah's amazement, characters stepped out of their pages. She met Alice from Wonderland, the White Rabbit, and even pirates from Treasure Island. They invited her to join their midnight council, where they discussed the tales of their adventures and the wisdom they contained.

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

# ✅ 정답 단어 리스트 추출
answer_words = []
processed_words = []

for i, word in enumerate(words):
    if i in blank_indices:
        stripped = word.strip(".,!?;:")
        suffix = word[len(stripped):]  # 기호 추출
        answer_words.append(stripped)
        blank = "_____" + suffix
        processed_words.append(blank)
    else:
        processed_words.append(word)

# ✅ 한 줄로 출력
st.markdown(" ".join(processed_words))

# ✅ 사용자 입력 받기
user_input = st.text_input("빈칸에 들어갈 단어들을 순서대로, 콤마로 입력하세요 (예: Willowby,Sarah,books,...)")

if st.button("제출"):
    user_answers = [w.strip() for w in user_input.split(",")]
    
    st.subheader("정답 확인")
    for idx, (correct, user) in enumerate(zip(answer_words, user_answers)):
        if correct.lower() == user.lower():
            st.markdown(f"✅ **{idx+1}. {user}** (정답)")
        else:
            st.markdown(f"❌ **{idx+1}. {user}** → 정답: **{correct}**")

    if len(user_answers) < len(answer_words):
        st.warning(f"❗ 입력한 단어 수가 부족합니다. {len(answer_words)}개의 빈칸이 있습니다.")
    elif len(user_answers) > len(answer_words):
        st.warning(f"❗ 입력한 단어 수가 너무 많습니다. {len(answer_words)}개의 빈칸이 있습니다.")
    else:
        score = sum([a.lower() == b.lower() for a, b in zip(answer_words, user_answers)])
        st.success(f"총 맞은 개수: {score} / {len(answer_words)}")


with tab3:
  st.title("a")
