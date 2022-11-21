import arviz as az
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from scipy import stats

az.style.use("arviz-doc")


a0 = np.linspace(1, 0.5, 50)
b0 = a0
a1 = a0[::-1]
b1 = a1
a2 = np.linspace(1, 2, 50)
b2 = a2
a3 = np.repeat(2, 50)
b3 = np.linspace(2, 5, 50)
a4 = a3
b4 = b3[::-1]
a5 = np.linspace(2, 4, 50)
b5 = np.linspace(2, 1, 50)
a6 = np.linspace(4, 1, 50)
b6 = np.repeat(1, 50)


A = np.concatenate((a0, a1, a2, a3, a4, a5, a6))
B = np.concatenate((b0, b1, b2, b3, b4, b5, b6))
params = list(zip(A, B))

x = np.linspace(0, 1, 1000)

fig, ax = plt.subplots(figsize=(8, 2))

#a = ax.plot(x, stats.beta(1, 1).pdf(x))
ax.set_ylim(0, 3)
ax.set_yticks([])
ax.set_xticks([])
ax.spines.left.set_visible(False)
ax.spines.bottom.set_visible(False)

tmp = []


def update(idx):
    global tmp
    for t in tmp:
        t[0].remove()
    tmp = []

    density = stats.beta(*params[idx]).pdf(x)
    a = ax.plot(x, density, color="C0", lw=2)
    b = ax.fill_between(x, density, color="C0", alpha=0.25, edgecolor=None)

    tmp.extend([a, [b]])

ani = FuncAnimation(fig, update, frames=350, interval=30, repeat=False)
ani.save("../diapo/img/con.gif")