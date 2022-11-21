import time

import arviz as az
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import preliz as pz

az.style.use("arviz-doc")


grid = np.linspace(0, 1, 200)
prior = pz.Beta(8, 4).rv_frozen.pdf(grid)
likelihood = pz.Binomial(36, grid).rv_frozen.pmf(14)
posterior = likelihood * prior
prior /= prior.sum()
likelihood /= likelihood.sum()
posterior /= posterior.sum()
fig, ax = plt.subplots(sharex=True, figsize=(16, 4))
ax.plot(grid, prior, '-', label="prior", lw=2)
ax.plot(grid, likelihood, '-', label="likelihood", lw=2)
ax.set_xlim(0, 1)
ax.set_ylim(None, posterior.max()*1.1)
ax.set_yticks([])
ax.set_xlabel("θ")
ax.legend()

lower = 50
upper = 150
evals = np.arange(lower, upper, 5)
zeros = np.zeros_like(evals)
tmp = []


def master_update(idx):
    # dirty hack to emulate different duration for different frames
    global tmp

    for t in tmp:
        t.remove()
    tmp = []

    if idx < 3:
        return
    elif idx == 4:
        ax.plot(grid[evals], zeros, "ko")
    elif idx < 5:
        return
    elif idx < 19+5:
        update(idx-5)
    elif idx == 19+5:
        ax.plot(grid[evals], posterior[evals], label="posterior", color="C2")
        ax.legend()
    else:
        return

def update(idx):



    ax.scatter(grid[evals][idx], posterior[evals][idx], edgecolor="k", color="C2", zorder=3)

    a = ax.hlines(likelihood[evals][idx], 0, grid[evals][idx], colors="C1", ls=":")
    b = ax.hlines(prior[evals][idx], 0, grid[evals][idx], colors="C0", ls=":")
    c = ax.vlines(grid[evals][idx], 0, prior[evals][idx], colors="k", ls=":")
    d = ax.vlines(grid[evals][idx], 0, likelihood[evals][idx], colors="k", ls=":")
    tmp.extend([a, b, c, d])



ani = FuncAnimation(fig, master_update, frames=30, interval=500, repeat=False)
ani.save("../img/grid.gif")