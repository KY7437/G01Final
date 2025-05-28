import streamlit as st
import pandas as pd
from gtts import gTTS
from io import BytesIO
import random
import tempfile

st.write("🌱 Vocabulary learning")

# Define tabs
tab1, tab2, tab3 = st.tabs(["❄️ Level 1", "❄️ Level 2", "❄️ Level 3"]
