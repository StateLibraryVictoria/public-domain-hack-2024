import cv2 as cv
import numpy as np
import requests
from pathlib import Path
import pandas as pd

import matplotlib.pyplot as plt

from sklearn.cluster import KMeans


def get_iiif_image_urls(ie_pid: str):
    try:

        manifest_url = f"https://rosetta.slv.vic.gov.au/delivery/iiif/presentation/2.1/{ie_pid}/manifest"

        session = requests.Session()

        response = session.get(manifest_url)

        manifest = response.json()

        image_ids = [
            canvas["images"][0]["resource"]["service"]["@id"]
            for canvas in manifest["sequences"][0]["canvases"]
        ]

        image_urls = [f"{image_id}/full/600,/0/default.jpg" for image_id in image_ids]

    except Exception as e:

        print(f"Could not get iiif image URLs for {ie_pid}, here's the error {e}")
        print(f"Manifest url {manifest_url}")

        image_urls = []

    return image_urls


# print(get_iiif_image_urls("IE1258179"))


def show_img_compare(img_1, img_2):
    f, ax = plt.subplots(1, 2, figsize=(10, 10))
    ax[0].imshow(img_1)
    ax[1].imshow(img_2)
    ax[0].axis("off")  # hide the axis
    ax[1].axis("off")
    f.tight_layout()
    plt.show()


def palette(clusters):
    width = 300
    palette = np.zeros((50, width, 3), np.uint8)
    steps = width / clusters.cluster_centers_.shape[0]
    for idx, centers in enumerate(clusters.cluster_centers_):
        palette[:, int(idx * steps) : (int((idx + 1) * steps)), :] = centers
    return palette


def get_palette_clusters(img, no_of_clusters=5):

    cluster = KMeans(n_clusters=no_of_clusters)
    cluster.fit(img.reshape(-1, 3))

    clusters = cluster.fit(img.reshape(-1, 3))

    return clusters


def get_colour_palette_iiif_image(ie_pid="", dim=(500, 300), iiif_url=None):

    if not iiif_url:
        # get iiif image urls
        image_urls = get_iiif_image_urls(ie_pid)
        iiif_url = image_urls[0]
        if not image_urls:
            return False

    response = requests.get(iiif_url)

    # decode image
    img = cv.imdecode(np.frombuffer(response.content, np.uint8), -1)
    img = cv.cvtColor(img, cv.COLOR_BGR2RGB)

    img = cv.resize(img, dim, interpolation=cv.INTER_AREA)

    palette_clusters = get_palette_clusters(img)
    img_palette = palette(palette_clusters)

    return img_palette


def get_palette_rgbs(ie_pid: str):
    print("Getting palette RGBs for", ie_pid)

    img_palette = get_colour_palette_iiif_image(ie_pid)

    if isinstance(img_palette, bool):

        return ""

    palette_rgbs = np.unique(img_palette[0], axis=0)

    palette_rgbs = palette_rgbs.tolist()

    return palette_rgbs


# print(get_palette_rgbs("IE1391238"))
# img, palette = get_colour_palette_iiif_image("IE1423319")
# img, palette = get_colour_palette_iiif_image("IE1391238")
# show_img_compare(img, palette)
