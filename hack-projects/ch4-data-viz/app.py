import streamlit as st

import pandas as pd

import dataset_wrangler


st.write(
    "Scrambled Images  from [https://www.slv.vic.gov.au/images](https://www.slv.vic.gov.au/images)"
)

df = dataset_wrangler.clean_df()


st.dataframe(df.head(10))
