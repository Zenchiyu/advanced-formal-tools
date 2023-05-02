# -*- coding: utf-8 -*-
"""
Created on Sun Mar 26 21:19:07 2023

@author: steph

Importing exported results from PRISM and surface plot
"""
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from read_all_res import read_all_res


def plot_res(df):
    # df = pd.read_csv("./prism_results_prior_to_tansen_modif.csv", skipinitialspace=True)
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

def plot_all_res(tables,
                 suptitle=None,
                 savepath="./all_res.PNG"):
    fig, axs = plt.subplots(2, len(tables)//2,
                            figsize=(7, 7),
                            subplot_kw={"projection": "3d"})
    i= 0
    for k, data in tables.items():
        print(2*i//len(tables), i % (len(tables)//2))
        ax = axs[2*i//len(tables), i % (len(tables)//2)]
        
        df = data
        X = df["p_bar"].values.reshape((11, 11))
        Y = df["v_init"].values.reshape((11, 11))
        Z = df["Result"].values.reshape((11, 11))
        
        surf = ax.plot_surface(X, Y, Z, cmap="coolwarm",
                           linewidth=0, antialiased=False)
        ax.set_xlabel("p_bar")
        ax.set_ylabel("v_init")
        # ax.set_zlabel(k)
        ax.set_title(k)
        
        i+=1
    if suptitle is None:
        plt.suptitle("Some quantitive properties with:\n"+\
                     "p_bar=0:0.1:1, interest=0,\nv_init=0:1:10, tmax=12 months\n")
    else:
        plt.suptitle(suptitle)
    plt.gcf().subplots_adjust(top=0.85)
    plt.savefig(savepath)

if __name__ == "__main__":
    
    tables = {}
    interests = [0.5, -0.5, 1, -1]
    for interest in interests:
        name = fr"interest=${interest}$"
        filename = "max_avg_reward_interest_" + int(np.sign(interest)/2 + 1)*"minus_" + str(np.abs(interest)).replace(".", "_")
        tables[name] = pd.read_csv(filename + ".csv", skipinitialspace=True)
    suptitle = "Rmax=? [ F is_done=1 ] with:\n"+\
                 "p_bar=0:0.1:1, interest"+ r"$\in\{0.5,-0.5,1,-1\},$"+\
                 "\nv_init=0:1:10, tmax=12 months\n"
    plot_all_res(tables, suptitle=suptitle, savepath="./max_avg_reward_different_interest.PNG")