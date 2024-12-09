import streamlit as st

import pandas as pd

st.write("Hello **world**")

df = pd.read_csv(
    "https://raw.githubusercontent.com/StateLibraryVictoria/public-domain-hack-2024/refs/heads/main/datasets/challenge-3-Image-Pool-2024-11-27.csv"
)

print(df.head(5))
