import arviz as az
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from matplotlib.animation import FuncAnimation

az.style.use("arviz-doc")
np.random.seed(172)

fig, axes = plt.subplots(2, 1, figsize=(10, 6), sharey=True, sharex=True)
axes[0].set_xlim(-8, 8)

chains = [
    [(-2.5, 1.15), (-0.9, 1.2), (0.5, 1.6), (2.1, 1.3)],
    [(-2, 1.15), (0.5, 1.2), (0.25, 1.6), (1.5, 1.3)],
    [(0.5, 1.2), (-0.2, 1.2), (0.1, 1.6), (1, 1.3)],
    [(0.1, 1.3), (-0.1, 1.4), (0.2, 1.3), (-0.3, 1.4)],
    [(0.05, 1.3), (-0.05, 1.3), (0, 1.3), (-0.01, 1.3)],
]

leg = []


def update(idx):
    global leg
    if leg:
        leg.remove()
    for ax in axes:
        for line in ax.get_lines():
            line.remove()

    samples = []
    for jdx, chain in enumerate(chains[idx]):
        sample = stats.norm(*chain).rvs(2000)
        az.plot_kde(
            sample, ax=axes[0], plot_kwargs={"color": f"C{jdx}", "lw": 2, "label": f"chain {jdx}"}
        )
        samples.append(sample)

    within_variance = np.mean(np.var(samples, 1))
    az.plot_kde(
        np.stack(samples),
        ax=axes[1],
        plot_kwargs={"color": "k", "lw": 3, "label": "varianza total"},
    )
    az.plot_kde(
        stats.norm(np.mean(samples), within_variance**0.5).rvs(2000),
        ax=axes[1],
        plot_kwargs={"color": "0.5", "ls": "--", "lw": 3, "label": "varianza interna"},
    )

    r_hat = az.rhat({"a": samples})
    axes[1].set_title(
        f"$\hat R$={r_hat['a'].item():.2f}\nvarianza total={np.var(samples):.2f}\nvarianza interna{within_variance:.2f}"
    )
    leg = plt.legend(loc="upper right")
    if idx == 0:
        plt.savefig("r_hat.png")


ani = FuncAnimation(fig, update, frames=4, interval=1000, repeat=False)
ani.save("../diapo/img/r_hat.gif")
