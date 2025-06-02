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

with tab3:
    vocabulary_quiz("Meaning Master", "meaning")

with tab4:
    vocabulary_quiz("Spelling Master", "spelling")
