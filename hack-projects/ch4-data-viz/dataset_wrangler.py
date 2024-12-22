import pandas as pd

dataset = "https://raw.githubusercontent.com/StateLibraryVictoria/public-domain-hack-2024/refs/heads/ch4-data-viz/datasets/ch3_colour_data_viz_suggestions_set_2_augmented.csv"


def clean_df(columns=None, dataset=dataset):

    df = pd.read_csv(dataset)

    if columns:
        df = df[columns]
    df = df.dropna()

    return df
