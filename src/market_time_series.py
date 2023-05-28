# -*- coding: utf-8 -*-
"""
Created on Sun Mar 26 21:29:15 2023

@author: steph
"""
import numpy as np
import matplotlib.animation as animation
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
    length = 50
    nb_runs = 20
    # v, c = generate_time_series(length=length)
    # plt.plot(v, label="market value v")
    # plt.plot(c, "--r", label="cap")
    # plt.legend()
    # plt.title("Market value")
    # plt.xlabel("Month")
    # plt.ylabel("Market value")
    # vs_non_flat, cs_non_flat = zip(*[generate_time_series(length=length) for _ in range(nb_runs)])
    vs_non_flat, cs_non_flat = zip(*[generate_time_series(v_init=np.random.randint(11), length=length) for _ in range(nb_runs)])
    vs, cs = np.array(vs_non_flat).flatten(), np.array(cs_non_flat).flatten()
    xs = np.tile(np.arange(length), 20)
   
    fig, ax = plt.subplots()
    line1 = ax.plot(vs[0], label="market value v")[0]
    line2 = ax.plot(cs[0], "--r", label="cap")[0]
    plt.legend()
    plt.title("Market value")
    plt.xlabel("Month")
    plt.ylabel("Market value")
    plt.xlim([0, length])
    plt.ylim([0, 10.5])
    
    def update(frame):
        # update the line plot:
        m = xs[frame]
        begin = length*(frame//length)
        end = begin + m
        begin_c = (length+1)*(frame//length)
        end_c = begin_c + m
        line1.set_xdata(np.arange(m))
        line1.set_ydata(vs[begin:end])
        line2.set_xdata(np.arange(length+1))
        line2.set_ydata(np.concatenate([cs[begin_c:end_c],
                                        cs[end_c]*np.ones(length+1-m)]))
        
        # line1.set_ydata(vs[frame-m:frame])
        # line2.set_xdata(np.arange(length))
        # line2.set_ydata(np.concatenate([cs[frame-m:frame],
        #                                 cs[frame]*np.ones(length-m)]))
        # line1.set_xdata(np.arange(frame))
        # line1.set_ydata(v[:frame])
        # line2.set_xdata(np.arange(length))
        # line2.set_ydata(np.concatenate([c[:frame],
        #                                 c[frame]*np.ones(length-frame)]))
        
        return (line1, line2)

    ani = animation.FuncAnimation(fig=fig, func=update, frames=length*nb_runs, interval=64)
    plt.show()
    ani.save("./images/market_dynamics.gif", writer=animation.PillowWriter(fps=30))
