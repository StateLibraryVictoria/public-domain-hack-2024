import pandas as pd
import math
import re

from bokeh.models import HoverTool
from bokeh.plotting import figure
from bokeh.models import CustomJS


def split_created_year(created_year):

    matches = re.findall("([1-3][0-9]{3})", created_year)

    start_date = int(matches[0])

    if len(matches) > 1:
        end_date = int(matches[-1])
    else:
        end_date = start_date

    return start_date, end_date


def display_event() -> CustomJS:

    js_code = """
        console.log('Hello mum!)
    """

    return CustomJS(code=js_code)


def clean_df(columns=None, dataset="", subset=[]):

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


def get_tooltips_dict(df, columns):

    df = df[columns]

    tooltips = df.to_dict()

    return tooltips


def create_grid(df, palette_columns=["pal_1", "pal_3", "pal_5"]):

    markers = {
        "pal_1": "circle",
        "pal_2": "hex",
        "pal_3": "square_pin",
        "pal_4": "plus",
        "pal_5": "triangle",
    }

    coords = get_square_coords(df)

    # bodge the df to ensure the length matches the coords
    df = df.head(len(coords))

    df["viewer_link"] = (
        "https://viewer.slv.vic.gov.au/?entity="
        + df["IE PID"].astype(str)
        + "&mode=browse"
    )

    TOOLS = "crosshair,pan,wheel_zoom,zoom_in,zoom_out,box_zoom,undo,redo,reset"

    data = pd.DataFrame(
        {
            "x": [coord[0] for coord in coords],
            "y": [coord[1] for coord in coords],
            "titles": df["Title (DC)"].values.tolist(),
            "created": df["Created - W 3 CDTF (DCTERMS)"].values.tolist(),
            "viewer_link": df["viewer_link"].values.tolist(),
        }
    )

    tt = """
    <div>
        <p>@title</p>
        <p>@created</p>
        <p><a href=@viewer_link{safe}}>@viewer_link{safe}</a></p>
    </div>
    """

    p = figure(sizing_mode="stretch_width", max_width=1000, tools=TOOLS)
    p.grid.grid_line_color = None
    p.axis.visible = False
    hover = HoverTool(tooltips=tt)
    p.add_tools(hover)

    radius = 12
    alpha = 0.25
    hover_alpha = 0.5

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

        data["rgba"] = df[f"rgba_{col}"].values.tolist()

        p.scatter(
            x="x",
            y="y",
            size=radius,
            color="rgba",
            alpha=alpha,
            hover_alpha=hover_alpha,
            hover_line_color="white",
            marker=markers[col],
            source=data,
        )

    return p


# div = Div(width=1000)
# curdoc().on_event(events.DocumentReady, display_event(div))

# from bokeh import events

# dataset = "https://raw.githubusercontent.com/StateLibraryVictoria/public-domain-hack-2024/refs/heads/ch4-data-viz/datasets/ch3_colour_data_viz_suggestions_set_2_augmented.csv"

# p = create_grid(dataset)

# show(p)
