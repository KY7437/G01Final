import streamlit as st

st.title("Into the World of Stories")
st.header("The Midnight Library lesson 1")
st.write("""Welcome to the **Middle School English Learning App**, a comprehensive platform designed to help students improve their English skills through **interactive and engaging activities**.  
This app integrates vocabulary, grammar, reading, and quizzes in one easy-to-use interface—perfect for **independent study** or **classroom support**.""")
st.markdown("---")

st.write("Access through the QR code.")

url="https://github.com/KY7437/G01Final/raw/main/data/QR.png"
st.image(url, caption="Lesson 1", width=300)  # width in pixel

st.write("Make sure to make a bookmark on the page so that you can still get access after this lesson.")
