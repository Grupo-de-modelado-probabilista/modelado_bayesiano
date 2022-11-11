import arviz as az
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from matplotlib.animation import FuncAnimation

az.style.use("arviz-white")

fig, axes = plt.subplots(1, 2, figsize=(10, 4), sharex=True, sharey=True)

def func(x):
    return np.sin(x+0.3)**2+np.cos(x)**0.5

x = np.linspace(-1.5, 1.5, 500)
landscape = func(x)

for ax, title, in zip(axes, ("maximización", "exploración")):
    ax.plot(x, landscape, "k", lw=3)
    ax.set_title(title)

axes[0].set_ylim(0.8, 1.8)
axes[0].set_yticks([])
axes[0].set_xticks([])


max_x = x[np.argmax(landscape)]
x_up = np.linspace(-0.45, max_x, 100)
x_up = np.concatenate((x_up, np.full(100, max_x)))
up = func(x_up) + 0.02

move= np.linspace(-1.4, 1.4, 100)
x_move = np.concatenate((move, move[::-1]))
move = func(x_move) + 0.02

tmp = []

def update(idx):
    global tmp
    for t in tmp:
        t[0].remove()
    tmp = []

    a = axes[0].plot(x_up[idx-1:idx], up[idx-1:idx], "C1o", mec="k",  ms=7,   zorder=3)
    b = axes[1].plot(x_move[idx-1:idx], move[idx-1:idx], "C1o", mec="k",  ms=7, zorder=3)

    tmp.extend([a, b])


ani = FuncAnimation(fig, update, frames=200, interval=40, repeat=False)
ani.save("../diapo/img/hmc_landscape.gif")
