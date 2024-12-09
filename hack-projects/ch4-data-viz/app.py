import streamlit as st

import pandas as pd


st.write(
    "Scrambled Images  from [https://www.slv.vic.gov.au/images](https://www.slv.vic.gov.au/images)"
)

try:

    df = pd.read_csv(
        "https://raw.githubusercontent.com/StateLibraryVictoria/public-domain-hack-2024/refs/heads/main/datasets/challenge-3-Image-Pool-2024-11-27.csv"
    )

except:

    df = pd.read_csv(
        "https://raw.githubusercontent.com/StateLibraryVictoria/public-domain-hack-2024/refs/heads/main/datasets/challenge-3-Image-Pool-2024-11-27.csv"
    )


st.dataframe(df.head(10))
