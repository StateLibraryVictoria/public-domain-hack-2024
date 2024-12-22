import os
import requests
from xml.etree import ElementTree as ET


def get_alma_information(endpoint: str, params={}):
    alma_url = "https://api-ap.hosted.exlibrisgroup.com"
    api_key = os.environ.get("ALMA_API_KEY", "l8xx313574e38e5c48f2af9ed8c3fa017926")

    print("Key", api_key)

    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": f"apikey {api_key}",
    }

    r = requests.get(f"{alma_url}{endpoint}", headers=headers, params=params)

    if r.status_code != 200:
        print(
            f"Could not retrieve info from ALMA, status {r.status_code} return with the following text {r.text}"
        )
        return False

    return r.json()


def retrieve_bib(mms_id: str):

    endpoint = f"/almaws/v1/bibs/{mms_id}"
    mms_data = get_alma_information(endpoint)

    return mms_data


def extract_mms_id_metadata(mms_id):

    try:

        bib_data = retrieve_bib(mms_id)

        mms_id = bib_data.get("mms_id")
        title = bib_data.get("title")

        anies = bib_data["anies"]

        tree = ET.fromstring(anies[0])

        p_950 = "n/a"
        summary = "Could not find"
        title_statement = "n/a"

        for node in tree:
            if node.attrib.get("tag") == "520":
                for n in node:
                    summary = n.text

            if node.attrib.get("tag") == "245":
                for n in node:
                    if n.attrib.get("code") == "a":
                        title_statement = n.text

            if node.attrib.get("tag") == "950":
                for n in node:
                    if n.attrib.get("code") == "p":
                        p_950 = n.text

        mms_id_metadata = [title, title_statement, summary, p_950]

        print(mms_id, mms_id_metadata)

        return mms_id_metadata

    except Exception as e:

        print(f"Couldn't retrieve metadata for {mms_id}. here's the error {e}")

        return ["", "", "", ""]
