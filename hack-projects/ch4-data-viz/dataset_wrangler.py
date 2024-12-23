import pandas as pd
import math

from bokeh.plotting import figure, show


dataset = "https://raw.githubusercontent.com/StateLibraryVictoria/public-domain-hack-2024/refs/heads/ch4-data-viz/datasets/ch3_colour_data_viz_suggestions_set_2_augmented.csv"


def clean_df(columns=None, dataset=dataset, subset=[]):

    df = pd.read_csv(dataset)

    if columns:
        df = df[columns]

    if subset:
        df = df.dropna(subset=subset)
    else:
        df = df.dropna()

    df = df.reset_index(drop=True)

    return df


def parse_rgb(df):

    palette_col = df["pal_5"]

    palette_col = palette_col.strip("[")
    palette_col = palette_col.strip("]")

    (
        r,
        g,
        b,
    ) = palette_col.split(",")

    return r, g, b


def create_rgba(df):

    rgba = f'rgb({df["red"]}, {df["green"]}, {df["blue"]})'

    return rgba


def get_square_coords(df):
    start = 0
    x = 0

    length = len(df)
    sq = math.sqrt(length)
    increment = round(sq)
    end = increment

    coords = []
    while end <= length:
        arr = [(x, y) for y, item in enumerate(df.index[start:end])]
        coords.extend(arr)
        end += increment
        start += increment
        x += 1

    return coords


def create_grid():

    df = clean_df(subset=["pal_5"])
    coords = get_square_coords(df)

    df[["red", "green", "blue"]] = df.apply(parse_rgb, result_type="expand", axis=1)

    df["rgba"] = df.apply(create_rgba, axis=1)

    rgba_list = df["rgba"].values.tolist()

    df["red"] = df["red"].astype("int64")
    df["green"] = df["green"].astype("int64")
    df["blue"] = df["blue"].astype("int64")

    x = [coord[0] for coord in coords]
    y = [coord[1] for coord in coords]

    # TOOLS = "hover,crosshair,pan,wheel_zoom,zoom_in,zoom_out,box_zoom,undo,redo,reset,tap,save,box_select,poly_select,lasso_select,examine,help"
    TOOLS = "hover,crosshair,pan,wheel_zoom,zoom_in,zoom_out,box_zoom,undo,redo,reset"

    p = figure(tools=TOOLS)

    p.circle(
        x=x,
        y=y,
        radius=0.4,
        color=rgba_list,
        alpha=0.5,
        hover_alpha=0.9,
        hover_line_color="white",
    )

    return p


p = create_grid()
show(p)
