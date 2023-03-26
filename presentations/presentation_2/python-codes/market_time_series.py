# -*- coding: utf-8 -*-
"""
Created on Sun Mar 26 21:29:15 2023

@author: steph
"""
import numpy as np
import matplotlib.pyplot as plt


def increase_p_with_some_proba_otherwise_decrease(p, proba):
    if np.random.uniform() < proba:
        p = min(1, p+0.1)
    else:
        p = max(0, p-0.1)
    return p
    

def generate_time_series(v_init=10, p=1/2, cap_init=10, length=100):
    v = np.zeros((length, ))
    c = np.zeros((length+1, ))
    v[0] = v_init
    c[[0, 1]] = cap_init
    
    for i in range(1, length):
        
        # Value increases or decreases by 1
        if np.random.uniform() < p:
            # Increase value by 1 but is capped by cap
            v[i] = min(c[i], v[i-1]+1)
        else:
            # Decrease value by 1 but cannot go below 0
            v[i] = min(c[i], max(0, v[i-1]-1))
        
        # Probability p can change over time too, either increases or decreases
        # by 0.1
        # ~ reaction of actors in the market
        if v[i] < 5:
            p = increase_p_with_some_proba_otherwise_decrease(p, 2/3)
        elif v[i] == 5:
            p = increase_p_with_some_proba_otherwise_decrease(p, 1/2)
        else:
            p = increase_p_with_some_proba_otherwise_decrease(p, 1/3)
        
        # Cap can decrease with a proba of 1/2
        c[i+1] = max(0, c[i] + np.random.choice([0, -1]))
    return v, c
if __name__ == "__main__":
    v, c = generate_time_series(length=50)
    plt.plot(v, label="market value v")
    plt.plot(c, "--r", label="cap")
    plt.legend()
    plt.title("Market value")
    plt.xlabel("Month")
    plt.ylabel("Market value")