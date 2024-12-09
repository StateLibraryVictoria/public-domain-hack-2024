import cv2 as cv
import numpy as np
import requests
import urllib
from pathlib import Path

import matplotlib.pyplot as plt

from sklearn.cluster import KMeans


def get_iiif_image_urls(ie_pid: str):

    manifest_url = f"https://rosetta.slv.vic.gov.au/delivery/iiif/presentation/2.1/{ie_pid}/manifest"
    print(manifest_url)
    session = requests.Session()

    response = session.get(manifest_url)

    manifest = response.json()

    image_ids = [
        canvas["images"][0]["resource"]["service"]["@id"]
        for canvas in manifest["sequences"][0]["canvases"]
    ]

    image_urls = [f"{image_id}/full/600,/0/default.jpg" for image_id in image_ids]

    return image_urls


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


def get_palette_clusters(img):

    cluster = KMeans(n_clusters=5)
    cluster.fit(img.reshape(-1, 3))

    clusters = cluster.fit(img.reshape(-1, 3))

    return clusters


image_urls = get_iiif_image_urls("IE1267294")

response = requests.get(image_urls[0])

img = cv.imdecode(np.frombuffer(response.content, np.uint8), -1)
img = cv.cvtColor(img, cv.COLOR_BGR2RGB)

dim = (500, 300)
img = cv.resize(img, dim, interpolation=cv.INTER_AREA)

clt_1 = get_palette_clusters(img)


img_palette = palette(clt_1)

print(img_palette)

show_img_compare(img, img_palette)
