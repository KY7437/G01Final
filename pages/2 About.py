import streamlit as st


# 새로운 유튜브 영상 삽입
st.markdown("""
<iframe width="300" height="200" src="https://www.youtube.com/embed/38SFyPRu_WU" 
frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
allowfullscreen></iframe>
""", unsafe_allow_html=True)

st.write("This video is designed to help you better understand the lesson.")

st.title("📘 About This App")

st.markdown("""
Welcome to the **Middle School English Learning App**, a comprehensive platform designed to help students improve their English skills through **interactive and engaging activities**.  
This app integrates vocabulary, grammar, reading, and quizzes in one easy-to-use interface—perfect for **independent study** or **classroom support**.


---

### 🎯 App Goals
- Build a strong foundation in English vocabulary and grammar.  
- Improve reading comprehension and listening skills.  
- Make language learning interactive and enjoyable.  
- Provide tools for self-assessment and personalized practice.  
- Encourage consistent and independent study habits.

---

### 👩‍🏫 Who Is This For?
- Middle school English learners  
- Teachers looking for supplementary digital materials  
- Students preparing for exams or doing self-study  

---

### 💡 Tips for Best Use
- Start with **Voca Starter** to build up your vocabulary before diving into reading and grammar.  
- Use **Grammar Drawing** to visualize difficult rules in your own way.  
- Try **Study Alone** when you need focused review or grammar transformation practice.  
- Listen to the **TTS audio repeatedly** to improve pronunciation and intonation.  
- Use **quizzes regularly** to check your progress.  

---

### 🚀 Let’s Get Started!
Click on any section in the sidebar to begin your journey.  
Each activity is designed to make learning **meaningful**, **visual**, and **active**.  

**Happy studying! 🌱📚✨**
""")
