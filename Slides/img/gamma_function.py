#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Plot of the gamma function
"""
from __future__ import division
import numpy as np
from scipy.special import gamma
import matplotlib.pyplot as plt

plt.rcParams["mathtext.fontset"] = "cm"


z = np.linspace(-5, 5, 5000)

plt.figure(figsize=(4, 3))
y = gamma(z)
y[np.abs(y)>5.1] = np.nan
plt.plot(z, y)


plt.xlabel(r"$z$")
plt.ylabel(r"$y$")
plt.ylim(-4, 4)
plt.tight_layout()
plt.savefig("gamma_function.svg", transparent=True)

