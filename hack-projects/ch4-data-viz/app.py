from bokeh import events
from bokeh.models import CustomJS

import streamlit as st

import dataset_wrangler

dataset = "https://raw.githubusercontent.com/StateLibraryVictoria/public-domain-hack-2024/refs/heads/ch4-data-viz/datasets/ch3_colour_data_viz_suggestions_set_2_augmented.csv"

st.write(
    "Scrambled Images  from [https://www.slv.vic.gov.au/images](https://www.slv.vic.gov.au/images)"
)


p = dataset_wrangler.create_grid(dataset)

callback = CustomJS(
    code="""
    console.log(Math.floor(cb_obj.x))
    console.log(Math.floor(cb_obj.y))

    try {
        console.log("Hello mum")
        st.write("Hello mum")
    } catch {
        console.log("error")
    }
"""
)

p.js_on_event(events.Tap, callback)

st.bokeh_chart(p, use_container_width=True)
