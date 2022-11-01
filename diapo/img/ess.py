import arviz as az
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from matplotlib.animation import FuncAnimation

az.style.use("arviz-white")
np.random.seed(252)

fig, axes = plt.subplots(2,1, figsize=(10, 6), sharey=True, sharex=True)

x = np.linspace(0, 1, 1000)
pdf = stats.beta(2, 5).pdf(x)
axes[0].plot(x, pdf, "k--")
axes[1].plot(x, pdf, "k--")
axes[0].set_ylim(0, 3.5)
axes[0].set_yticks([])
axes[0].set_title("Muestras independientes")
axes[1].set_title("Muestras autocorrelacionadas")


ind = np.random.beta(2, 5, 1000)
dep = np.empty(1000)
dep[0::2] = ind[:500] + 0.05
dep[1::2] = np.sort(ind[500:]) - 0.05


tmp = []
def update(idx):
    global tmp
    for t in tmp:
        try:
            t.remove()
        except:
            pass

    if idx > 20:
        idx = 20

    fig.suptitle(f"Número de muestras = {idx*50}", fontsize=18)
    a = axes[0].hist(ind[:idx*50], bins="auto", density=True, color="C1")[2]
    b = axes[1].hist(dep[:idx*50], bins="auto", density=True, color="C1")[2]
    tmp.extend([a, b])

ani = FuncAnimation(fig, update, frames=25, interval=500, repeat=False)
ani.save("ess.gif")