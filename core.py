#!/usr/bin/env python

import pandas as pd


def get_stats19(year=2023, type="collision"):
    URL = "https://data.dft.gov.uk/road-accidents-safety-data/"
    URI = f"{URL}/dft-road-casualty-statistics-{type}-{year}.csv"
    return pd.read_csv(URI, low_memory=False)



#df = get_stats19(2022, "collision")
