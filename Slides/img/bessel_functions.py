#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Plots of the Bessel functions of the first kind
"""
from __future__ import division
import numpy as np
from scipy.special import jn
import matplotlib.pyplot as plt

plt.rcParams["mathtext.fontset"] = "cm"


z = np.linspace(0, 10, 500)

plt.figure(figsize=(4, 3))
for nu in [0, 1, 2, 3]:
    J = jn(nu,z)
    plt.plot(z, J, label=r"$J_{}$".format(nu))


plt.xlabel(r"$z$")
plt.ylabel(r"$y$")
plt.legend()
plt.tight_layout()
plt.savefig("bessel_functions.svg", transparent=True)
