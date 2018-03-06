#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Animate the fall of a person with parachute
"""
from __future__ import division, print_function
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import matplotlib.animation as animation


plt.rcParams["font.family"] = "serif"
plt.rcParams["font.size"] = 18
plt.rcParams["mathtext.fontset"] = "cm"


def drag_fall(x, t, gravity, drag, mass):
    y, v = x
    return [v, -gravity + drag/mass*v**2]


def update(num, ax, t, y):
    ax.cla()
    plot = ax.plot(0, y[num], "ko")
    ax.set_title(r"$t={:.2f}$".format(t[num]))
    ax.set_xlim(-1, 1)
    ax.set_xticks([])
    return plot


dist = 500
y0 = [dist, 0]
g = 9.81
mass = 70
drag = 1.2
tmax = np.sqrt(2*dist/g)
t = np.linspace(0, tmax, 101)
sol = odeint(drag_fall, y0, t, args=(g, drag, mass))

fig, (ax1, ax2) = plt.subplots(1, 2, sharey=True, **{"figsize": (8, 5)})
ax1.plot(t, sol[:, 0])
ax1.set_xlabel(r"Time (s)")
ax1.set_ylabel(r"Height (m)")

ani = animation.FuncAnimation(fig, update, fargs=(ax2, t, sol[:, 0]),
                                   interval=50, blit=True)
ani.save("drag_fall.mp4", dpi=600)
#plt.show()
