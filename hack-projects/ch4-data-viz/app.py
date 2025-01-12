import streamlit as st
from PIL import Image

import dataset_wrangler, image_analysis

dataset = "https://raw.githubusercontent.com/StateLibraryVictoria/public-domain-hack-2024/refs/heads/ch4-data-viz/datasets/ch3_colour_data_viz_suggestions_set_2_augmented.csv"

palette_columns = ["pal_1", "pal_3", "pal_5"]

ner_categories = {
    "Organisation": "ORD",
    "Country": "GPE",
    "Person": "PERSON",
    "Event name": "EVENT",
    "Address": "FAC",
}

st.write(
    "Scrambled Images  from [https://www.slv.vic.gov.au/images](https://www.slv.vic.gov.au/images)"
)


df = dataset_wrangler.clean_df(dataset=dataset, subset=palette_columns)


df["created_year"] = df["Created - W 3 CDTF (DCTERMS)"].apply(
    lambda x: dataset_wrangler.split_created_year(x)[0]
)


with st.form("my_form"):
    # st.write("")
    min_year = df["created_year"].min()
    max_year = df["created_year"].max()
    values = st.slider(
        "Select a year range: ",
        min_year,
        max_year,
        (min_year, max_year),
    )

    selection = st.pills("Named entity filter", ner_categories.keys())
    st.write(f"NER selection {selection}")

    st.form_submit_button("Visualise my selection")


df = df[df["created_year"].between(values[0], values[1])]

if selection:

    df = df[df["ner"].str.contains(ner_categories[selection])]

n = 3

random_selection = df.sample(n=n)

random_selection["iiif_url"] = random_selection["IE PID"].apply(
    lambda x: image_analysis.get_iiif_image_urls(x)
)

p = dataset_wrangler.create_grid(df)


with st.container():
    st.write(f"Plotting images from {values[0]} to {values[1]}")
    st.bokeh_chart(p, use_container_width=True)


cols = st.columns(n)

with st.container():
    st.write(f"Random image selection")
    for idx, img in enumerate(random_selection.values.tolist()):
        iiif_url = img[-1][0]
        title = img[2]
        palette = image_analysis.get_colour_palette_iiif_image(iiif_url=iiif_url)
        pal_im = Image.fromarray(palette, "RGB")
        with cols[idx]:
            st.image(iiif_url, use_container_width=True, caption=title)
            st.image(pal_im, use_container_width=True, caption="Colour palette")


# # !
# import re

# df = dataset_wrangler.clean_df(dataset=dataset, subset=palette_columns)

# random_selection = df.sample(2)

# random_selection["iiif_url"] = random_selection["IE PID"].apply(
#     lambda x: image_analysis.get_iiif_image_urls(x)
# )


# for ner in random_selection["ner"].values.tolist():
#     print(ner)

#     str_start = "→"
#     str_end = " "

#     res = re.findall(str_start + "(.*)" + str_end, ner)

#     print(res)
