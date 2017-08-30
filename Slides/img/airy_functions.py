#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Plots of the Airy functions
"""
from __future__ import division
import numpy as np
from scipy.special import airy
import matplotlib.pyplot as plt

plt.rcParams["mathtext.fontset"] = "cm"


z = np.linspace(-10, 5, 500)
Ai, _, Bi, _  = airy(z)


plt.figure(figsize=(4, 3))
plt.plot(z, Ai)
plt.plot(z, Bi)
plt.ylim(-0.5, 1)
plt.xlabel(r"$z$")
plt.ylabel(r"$y$")
plt.legend([r"$\mathrm{Ai}(z)$", r"$\mathrm{Bi}(z)$"])
plt.tight_layout()
plt.savefig("airy_functions.svg", transparent=True)
