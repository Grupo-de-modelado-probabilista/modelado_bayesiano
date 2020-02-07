import numpy as np
import arviz as az
from scipy import stats
import matplotlib.pyplot as plt
az.style.use('arviz-darkgrid')

import matplotlib as mpl
mpl.rc('image', cmap='viridis_r')

np.random.seed(42)
x_s = np.linspace(-4.5, 10, 200)

f, ax = plt.subplots(2, 2, figsize=(5.5, 5.5))

T0 = stats.norm(0, 1)
T1 = stats.norm(2, 0.5)
T2 = stats.norm(6, 2)

T = T0.pdf(np.sin(x_s)) * .35 + T1.pdf(x_s) * .35 + T2.pdf(x_s) * .4
T /= T.sum()
ax[0, 0].fill_between(x_s, T, alpha=1, color='C7')
ax[0, 0].set_xticks([])
ax[0, 0].set_yticks([])
ax[0, 0].set_title('Distribución verdadera', fontsize=12)

T_sample = np.random.choice(x_s, size=20, replace=True, p=T)
ax[0, 1].plot(T_sample, np.zeros_like(T_sample) + 0.05, '.', color='C7')
ax[0, 1].set_ylim(0, 1)
ax[0, 1].set_xticks([])
ax[0, 1].set_yticks([])
ax[0, 1].set_title('Muestra', fontsize=12)


cov = np.array([[1, 0.8 ],
                [0.8 ,1]])
xy = np.random.multivariate_normal([0, 0], cov, 10000)
u1 = xy[:,0]
u2 = xy[:,1]

a = 2
b = 0.15

x = u1 * a
y = (u2 / a) + b * (u1**2 + a**2)

az.plot_kde(x, y, ax=ax[1, 1], fill_last=False, contour_kwargs={'alpha':0})
ax[1, 1].set_xticks([])
ax[1, 1].set_yticks([])
ax[1, 1].set_title('Distribución a posteriori', fontsize=12)

T_ppc = np.random.choice(x_s, size=40, replace=True, p=T)
az.plot_kde(T_ppc, ax=ax[1, 0], bw=6, plot_kwargs={'color':'C7', 'alpha':0},
           fill_kwargs={'alpha': 0.75})

ax[1, 0].set_xticks([])
ax[1, 0].set_yticks([])
ax[1, 0].set_title('Distribución\n predictiva a posteriori', fontsize=12)
f.tight_layout()
plt.subplots_adjust(wspace=0.5, hspace=0.5)

ax[1, 0].text(11, 0.032, "muestreo")
ax[1, 0].annotate('', xy=(17.5, 0.031), xytext=(10.5, 0.031),
                 arrowprops=dict(facecolor='black', shrink=0.05),
                 annotation_clip=False)

ax[1, 0].text(25, 0.021, "inferencia")
ax[1, 0].annotate('', xy=(24, 0.018), xytext=(24, 0.023),
                  ha="center",
                 arrowprops=dict(facecolor='black', shrink=0.05),
                 annotation_clip=False)

ax[1, 0].text(12, 0.007, "predicción")
ax[1, 0].annotate('', xy=(10, 0.006), xytext=(17, 0.006),
                 arrowprops=dict(facecolor='black', shrink=0.05),
                 annotation_clip=False)

ax[1, 0].text(8.5, 0.021, "validación")
ax[1, 0].annotate('', xy=(17, 0.023), xytext=(9.5, 0.017),
                 arrowprops=dict(facecolor='black', shrink=0.05),
                 annotation_clip=False)

plt.savefig('bayesian_workflow.png', dpi=300)
