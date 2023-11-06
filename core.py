#!/usr/bin/env python

import pandas as pd
import requests
from bs4 import BeautifulSoup

pd.set_option("display.max_columns", None)


def get_available_csv():
    url = "https://www.data.gov.uk/dataset/cb7ae6f0-4be6-4935-9277-47e5ce24a11f/road-safety-data"
    r = requests.get(url, timeout=10.0)
    soup = BeautifulSoup(r.content, "html.parser")
    path = []
    for hit in soup.findAll("a"):
        href = hit.get("href")
        if "dft-road-casualty-statistics-" in href:
            path.append(href)
    if not path:
        return pd.DataFrame()
    r = pd.DataFrame(path, columns=["uri"])
    r["filename"] = r["uri"].str.split("/", expand=True).iloc[:, -1]
    r[["type", "year", "file"]] = (
        r["filename"].str.split(r"[-.]", expand=True).iloc[:, 4:7]
    )
    ix = r["file"] == "csv"
    r = r[ix]
    r["year"] = pd.to_numeric(r["year"])
    return r.sort_values(["year", "type"]).reset_index(drop=True)


def get_stats19(year=2023, incident="collision"):
    url = "https://data.dft.gov.uk/road-accidents-safety-data/"
    uri = f"{url}/dft-road-casualty-statistics-{incident}-{year}.csv"
    return pd.read_csv(uri, low_memory=False)


# df = get_stats19(2022, "collision")
