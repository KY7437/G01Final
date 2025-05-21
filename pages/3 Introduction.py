import streamlit as st
import pandas as pd
from gtts import gTTS
from io import BytesIO
import random

st.write("🌱 Vocabulary learning")

# Define tabs
tab1, tab2, tab3 = st.tabs(["❄️ Word List", "❄️ 2. Wordle", "❄️ 3. Role Playing"])

with tab1:
    # Placeholder for tab1 content
    st.write("Content for Word List tab goes here.")
    # Add functionality for the Word List tab here

with tab2:
     # Placeholder for tab3 content
    st.write("Content for Role Playing tab goes here.")
    # Add functionality for the Role Playing tab here
   

with tab3:
     # Grammar example sentence dictionary
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

    # Input expression
    expression = st.text_input("📝 Enter expressions (ex. that, be p.p): ").strip().lower()

    # Output results
    if expression in EXPRESSION_DB:
        data = EXPRESSION_DB[expression]
        st.write("🗣️ Sample sentences:")
        for ex in data["examples"]:
            st.write(f"- {ex}")
    else:
        st.write("⚠️ Please use expressions we used in class!!")

    
   

 
