# -*- coding: utf-8 -*-
"""
Created on Sun Mar 26 21:19:07 2023

@author: steph

Importing exported results from PRISM and surface plot
"""
import pandas as pd
import matplotlib.pyplot as plt


if __name__ == "__main__":
    df = pd.read_csv("./prism_results_prior_to_tansen_modif.csv", skipinitialspace=True)
    X = df["p_bar"].values.reshape((11, 11))
    Y = df["v_init"].values.reshape((11, 11))
    Z = df["Result"].values.reshape((11, 11))
    
    fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
    surf = ax.plot_surface(X, Y, Z, cmap="coolwarm",
                       linewidth=0, antialiased=False)
    plt.xlabel("probability of choosing to bar: p_bar")
    plt.ylabel("initial value of the shares: v_init")
    ax.set_zlabel("maximum reward")
    plt.savefig("./prism_results.PNG")
    
