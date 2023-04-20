import arviz as az
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from matplotlib.animation import FuncAnimation

az.style.use("arviz-white")

fig, axes = plt.subplots(1, 3, figsize=(10, 4), sharex=True, sharey=True)

x = np.linspace(-2, 2, 100)
for ax in axes:
    ax.plot(x, x**2, lw=3)

padding = 0.15

short = np.linspace(-1, -0.7, 10)
short2 = short**2 + padding
long0 = np.linspace(-1, 1, 10)
long1 = np.linspace(1, -1, 10)
long = np.concatenate((long0, long1))
long2 = long**2 + padding
right = np.linspace(-1, 1, 10)
right2 = right**2 + padding


axes[0].plot(short, short2, "C1o", mec="k", alpha=0.25)
axes[0].set_title("muy corta")
axes[1].plot(long, long2, "C1o", mec="k", alpha=0.25)
axes[1].set_title("muy larga")
axes[2].plot(right, right2, "C1o", mec="k", alpha=0.25)
axes[2].set_title("muy buena!")


tmp = []

def update(idx):
    global tmp
    for t in tmp:
        t[0].remove()
    tmp = []

    a = axes[0].plot(short[idx-1:idx], short2[idx-1:idx], "C1o", mec="k", zorder=3)
    b = axes[1].plot(long[idx-1:idx], long2[idx-1:idx], "C1o", mec="k",  zorder=3)
    c = axes[2].plot(right[idx-1:idx], right2[idx-1:idx], "C1o", mec="k",  zorder=3)
    tmp.extend([a, b, c])
    for ax in axes:
        ax.set_yticks([])

ani = FuncAnimation(fig, update, frames=25, interval=300, repeat=False)
ani.save("hmc_1D.gif")