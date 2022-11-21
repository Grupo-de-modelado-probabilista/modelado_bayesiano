import arviz as az
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats


az.style.use("arviz-doc")


cmap = plt.cm.get_cmap('viridis')
plt.figure(figsize=(11, 4))
for c, d in enumerate([1, 20, 100, 300]):
    samples = stats.multivariate_normal([0]*d, np.eye(d)).rvs(10000)
    if d == 1:
        radial_dist = np.sum(samples[:, None]**2, 1)**0.5
    else:
        radial_dist = np.sum(samples**2, 1)**0.5
    az.plot_kde(radial_dist, bw=0.2, plot_kwargs={"color":cmap(c*60+50), "lw":3}, label=f'd = {d}')
plt.yticks([])
plt.xlabel('Distancia a la moda')
plt.savefig("../img/gauss_mode.png")