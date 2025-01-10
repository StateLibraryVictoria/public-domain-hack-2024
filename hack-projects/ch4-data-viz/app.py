import streamlit as st

import dataset_wrangler, image_analysis

dataset = "https://raw.githubusercontent.com/StateLibraryVictoria/public-domain-hack-2024/refs/heads/ch4-data-viz/datasets/ch3_colour_data_viz_suggestions_set_2_augmented.csv"

st.write(
    "Scrambled Images  from [https://www.slv.vic.gov.au/images](https://www.slv.vic.gov.au/images)"
)

palette_columns = ["pal_1", "pal_3", "pal_5"]

df = dataset_wrangler.clean_df(dataset=dataset, subset=palette_columns)


df["created_year"] = df["Created - W 3 CDTF (DCTERMS)"].apply(
    lambda x: dataset_wrangler.split_created_year(x)[0]
)


with st.form("my_form"):
    st.write
    min_year = df["created_year"].min()
    max_year = df["created_year"].max()
    values = st.slider(
        "Select a year range: ",
        min_year,
        max_year,
        (min_year, max_year),
    )
    st.form_submit_button("Visualise my selection")

df = df[df["created_year"].between(values[0], values[1])]

random_selection = df.sample(n=3)

random_selection["iiif_url"] = random_selection["IE PID"].apply(
    lambda x: image_analysis.get_iiif_image_urls(x)
)

col1, col2 = st.columns([0.3, 0.7])

with col1:
    st.write(f"Random image selection")
    for img in random_selection["iiif_url"].values.tolist():
        st.image(img, use_container_width=True)


p = dataset_wrangler.create_grid(df)

with col2:
    st.write(f"Plotting images from {values[0]} to {values[1]}")
    st.bokeh_chart(p, use_container_width=True)
