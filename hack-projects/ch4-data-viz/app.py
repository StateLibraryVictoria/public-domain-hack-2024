import streamlit as st

import dataset_wrangler


st.write(
    "Scrambled Images  from [https://www.slv.vic.gov.au/images](https://www.slv.vic.gov.au/images)"
)


p = dataset_wrangler.create_grid()


st.bokeh_chart(p, use_container_width=True)
