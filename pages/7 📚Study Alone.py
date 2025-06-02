import streamlit as st
from gtts import gTTS
from io import BytesIO
import re

st.title("Passage Reading")

# Define tabs
tab1, tab2, tab3 = st.tabs(["Guildlines", "Memorization of the text", "a"])

with tab1: 
  st.title("Guidelines")

with tab2:
  st.title("Memorization of the text")

with tab3:
  st.title("a")
