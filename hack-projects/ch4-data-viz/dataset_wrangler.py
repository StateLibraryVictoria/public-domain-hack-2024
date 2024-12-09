import pandas as pd

dataset = "https://raw.githubusercontent.com/StateLibraryVictoria/public-domain-hack-2024/refs/heads/main/datasets/challenge-3-Image-Pool-2024-11-27.csv"

columns = [
    "IE PID",
    "Title (DC)",
    "ALMA _ MMS (Object Identifier - IE)",
    "HANDLE (Object Identifier - IE)",
    "Creator (DC)",
    "Genre (DCTERMS)",
    "Created (DCTERMS)",
]


def clean_df(columns=columns, dataset=dataset):

    df = pd.read_csv(dataset)

    df = df[columns]
    df = df.dropna()

    return df
