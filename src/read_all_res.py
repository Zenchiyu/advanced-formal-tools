# -*- coding: utf-8 -*-
"""
Created on Fri Apr 21 08:50:09 2023

@author: steph
"""
import numpy as np
import pandas as pd


def read_all_res(filename="results/all_res.csv",
                 properties_path="properties.props"):
    df = pd.read_csv(filename, header=None, names=range(3))
    with open(properties_path, "r") as f:
        table_names = list(line for line in (l.strip() for l in f) if line)

    groups = df[0].isin(table_names).cumsum()
    tables = {g.iloc[0,0]: ((g.iloc[1:].rename(columns=g.iloc[1].str.strip())).iloc[1:]).astype(float)
     for k,g in df.groupby(groups)}
    return tables
