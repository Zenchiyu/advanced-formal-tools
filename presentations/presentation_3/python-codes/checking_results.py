# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 08:42:08 2023

@author: steph
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


if __name__ == "__main__":
    df1 = pd.read_csv("./prism_results_prior_to_tansen_modif.csv", skipinitialspace=True)
    df2 = pd.read_csv("./prism_results_after_to_tansen_modif.csv", skipinitialspace=True)
    print(np.mean(df1["Result"]-df2["Result"]))