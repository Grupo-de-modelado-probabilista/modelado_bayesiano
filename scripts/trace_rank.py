#!/usr/bin/env python
# coding: utf-8


import arviz as az
import pymc as pm
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats


az.style.use("arviz-white")


np.random.seed(42)
good_chain = stats.beta.rvs(10, 2, size=1000)
bad_chain0 = [0]
rnd = np.random.normal(0, 0.01, 999)
for val in rnd:
    bad_chain0.append(bad_chain0[-1] + val)
bad_chain0 = np.array(bad_chain0)

bad_chain1 = np.random.normal(np.linspace(0, 1, 1000) ** 0.25, 0.1)

bad_chain2 = good_chain.copy()
for i in np.random.randint(900, size=4):
    bad_chain2[i : i + 100] = np.random.beta(i, 950, size=100)

_, axes = plt.subplots(2, 2, figsize=(10, 4), sharex=True)
for idx, (ax, chain) in enumerate(
    zip(axes.ravel(), (good_chain, bad_chain0, bad_chain1, bad_chain2))
):
    ax.plot(chain, "0.4")
    ax.set_yticks([])
    if idx == 0:
        plt.setp(ax.spines.values(), color="C2", lw=3)
    else:
        plt.setp(ax.spines.values(), color="C1", lw=3)

plt.savefig("../diapo/img/trace_single_good_bad.png")


with plt.style.context("arviz-grayscale"):
    np.random.seed(42)
    good_chains = stats.beta.rvs(10, 2, size=(1000, 4))

    _, ax = plt.subplots(1, 1, figsize=(10, 4), sharex=True)
    ax.plot(good_chains)
    ax.set_yticks([])
plt.setp(ax.spines.values(), color="C2", lw=3)


plt.savefig("../diapo/img/trace_multiple_good.png")


az.plot_trace(good_chains.T)
plt.savefig("../diapo/img/trace_multiple_good_arviz.png")


az.plot_trace(good_chains.T, kind="rank_bars")
plt.savefig("../diapo/img/rank_multiple_good_arviz.png")


np.random.seed(124)
good_chains = stats.beta.rvs(2, 5, size=(4, 1000))

bad_chains0 = np.zeros((4, 1000))
rnd = np.random.normal(0, 0.01, (999, 4))
for idx, val in enumerate(rnd):
    bad_chains0[:, idx] = bad_chains0[:, idx - 1] + val

bad_chains1 = np.stack(
    [
        np.random.normal(np.linspace(0, 1, 1000) ** 0.1, 0.1),
        np.random.normal(np.linspace(0, 1, 1000) ** 0.25, 0.1),
        np.random.normal(np.linspace(0, 1, 1000) ** 0.75, 0.1),
        np.random.normal(np.linspace(0, 1, 1000), 0.1),
    ]
)

bad_chains2 = good_chains.copy()
for i in np.random.randint(900, size=4):
    bad_chains2[0][i : i + 100] = np.random.beta(i, 950, size=100)

_, axes = plt.subplots(2, 2, figsize=(10, 4), sharex=True)
for idx, (ax, chain) in enumerate(
    zip(axes.ravel(), (good_chains, bad_chains0, bad_chains1, bad_chains2))
):

    with plt.style.context("arviz-grayscale"):
        az.plot_rank(chain, ax=ax)

    ax.set_yticks([])
    if idx == 0:
        plt.setp(ax.spines.values(), color="C2", lw=3)
    else:
        plt.setp(ax.spines.values(), color="C1", lw=3)

plt.savefig("../diapo/img/rankbar_single_good_bad.png")


np.random.seed(124)
good_chains = stats.beta.rvs(2, 5, size=(4, 1000))

bad_chains0 = np.zeros((4, 1000))
rnd = np.random.normal(0, 0.01, (999, 4))
for idx, val in enumerate(rnd):
    bad_chains0[:, idx] = bad_chains0[:, idx - 1] + val

bad_chains1 = np.stack(
    [
        np.random.normal(np.linspace(0, 1, 1000) ** 0.1, 0.1),
        np.random.normal(np.linspace(0, 1, 1000) ** 0.25, 0.1),
        np.random.normal(np.linspace(0, 1, 1000) ** 0.75, 0.1),
        np.random.normal(np.linspace(0, 1, 1000), 0.1),
    ]
)

bad_chains2 = good_chains.copy()
for i in np.random.randint(900, size=4):
    bad_chains2[0][i : i + 100] = np.random.beta(i, 950, size=100)

_, axes = plt.subplots(2, 2, figsize=(10, 4), sharex=True)
for idx, (ax, chain) in enumerate(
    zip(axes.ravel(), (good_chains, bad_chains0, bad_chains1, bad_chains2))
):

    with plt.style.context("arviz-grayscale"):
        az.plot_rank(chain, kind="vlines", ax=ax)

    ax.set_yticks([])
    if idx == 0:
        plt.setp(ax.spines.values(), color="C2", lw=3)
    else:
        plt.setp(ax.spines.values(), color="C1", lw=3)

plt.savefig("../diapo/img/rankvlines_single_good_bad.png")
