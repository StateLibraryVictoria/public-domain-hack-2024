import streamlit as st

import dataset_wrangler, image_analysis

dataset = "https://raw.githubusercontent.com/StateLibraryVictoria/public-domain-hack-2024/refs/heads/ch4-data-viz/datasets/ch3_colour_data_viz_suggestions_set_2_augmented.csv"

st.write(
    "Scrambled Images  from [https://www.slv.vic.gov.au/images](https://www.slv.vic.gov.au/images)"
)

palette_columns = ["pal_1", "pal_3", "pal_5"]

df = dataset_wrangler.clean_df(dataset=dataset, subset=palette_columns)

random_selection = df.sample(n=3)

random_selection["iiif_url"] = random_selection["IE PID"].apply(
    lambda x: image_analysis.get_iiif_image_urls(x)
)

for img in random_selection["iiif_url"].values.tolist():
    st.image(img)


df["created_year"] = df["Created - W 3 CDTF (DCTERMS)"].apply(
    lambda x: dataset_wrangler.split_created_year(x)[0]
)

values = st.slider(
    "Select a year range: ",
    df["created_year"].min(),
    df["created_year"].max()(df["created_year"].min(), df["created_year"].max()),
)

# print(df["created_year"])

p = dataset_wrangler.create_grid(df)

st.bokeh_chart(p, use_container_width=True)
