import arviz as az
import numpy as np
import matplotlib.pyplot as plt
import preliz as pz

az.style.use("arviz-doc")


grid = np.linspace(0, 1, 200)
prior = pz.Beta(8, 4).rv_frozen.pdf(grid)
likelihood = pz.Binomial(36, grid).rv_frozen.pmf(14)
posterior = likelihood * prior
prior /= prior.sum()
likelihood /= likelihood.sum()
posterior /= posterior.sum()
_, ax = plt.subplots(sharex=True, figsize=(16, 4))
ax.plot(grid, prior, '-', label="prior", lw=2)
ax.plot(grid, likelihood, '-', label="likelihood", lw=2)
ax.plot(grid, posterior, '-', label="posterior", lw=4)

ax.fill_between(grid, prior, where=posterior>0.0005, color="0.9")
ax.fill_between(grid, likelihood, where=posterior>0.0005, color="0.9")

ax.set_yticks([])
ax.set_xlabel("θ")

ax.legend()
plt.savefig("../img/grid.png")