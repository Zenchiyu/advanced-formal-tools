# -*- coding: utf-8 -*-
"""
Created on Fri Apr 21 08:50:09 2023

@author: steph
"""
import numpy as np
import pandas as pd

if __name__ == "__main__":
    df = pd.read_csv("all_res.csv", header=None, names=range(3))
    table_names = ["Rmax=? [ F is_done=1 ]",
                   "Rmin=? [ F is_done=1 ]",
                   'R{"steps"}max=? [ F is_done=1 ]',
                   'R{"steps"}min=? [ F is_done=1 ]']
    groups = df[0].isin(table_names).cumsum()
    tables = {g.iloc[0,0]: (g.iloc[1:].rename(columns=g.iloc[1])).iloc[1:]
     for k,g in df.groupby(groups)}