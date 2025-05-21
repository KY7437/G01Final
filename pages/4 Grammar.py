import streamlit as st
import pandas as pd
from gtts import gTTS
from io import BytesIO
import random

st.write("🌱 Vocabulary learning")

tab1, tab2, tab3, tab4 = st.tabs(["❄️ Read after TTS", "❄️ ", "❄️ "])
