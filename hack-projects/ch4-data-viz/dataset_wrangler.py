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


def create_rgba(df, palette_col):

    rgba = f'rgb({df[f"red_{palette_col}"]}, {df[f"green_{palette_col}"]}, {df[f"blue_{palette_col}"]})'

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


def create_grid(palette_columns=["pal_1", "pal_3", "pal_5"]):

    markers = {
        "pal_1": "circle",
        "pal_3": "square_pin",
        "pal_5": "triangle",
    }

    df = clean_df(subset=palette_columns)
    coords = get_square_coords(df)

    x = [coord[0] for coord in coords]
    y = [coord[1] for coord in coords]

    TOOLS = "hover,crosshair,pan,wheel_zoom,zoom_in,zoom_out,box_zoom,undo,redo,reset"

    p = figure(tools=TOOLS)

    radius = 10
    alpha = 0.3
    hover_alpha = 0.6

    for col in palette_columns:

        df[col] = df[col].str.strip("[")
        df[col] = df[col].str.strip("]")

        df[[f"red_{col}", f"green_{col}", f"blue_{col}"]] = df[col].str.split(
            ",", expand=True
        )

        df[f"rgba_{col}"] = (
            "rgb("
            + df[f"red_{col}"]
            + ","
            + df[f"green_{col}"]
            + ","
            + df[f"blue_{col}"]
            + ")"
        )

        rgba_list = df[f"rgba_{col}"].values.tolist()

        p.scatter(
            x=x,
            y=y,
            size=radius,
            color=rgba_list,
            alpha=alpha,
            hover_alpha=hover_alpha,
            hover_line_color="white",
            marker=markers[col],
        )

    return p


# p = create_grid(palette_columns=["pal_1"])
# show(p)
