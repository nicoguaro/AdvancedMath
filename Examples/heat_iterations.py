"""
Illustration of the heat equation

Solve the heat equation using finite differences and Forward Euler.

Based on: https://commons.wikimedia.org/wiki/File:Heat_eqn.gif
"""

from __future__ import division, print_function
import numpy as np
from mayavi import mlab


def step_function(N, scale, X, Y, shape="crescent"):
    """Function that is 1 on a set and 0 outside of it"""
    shapes = ["crescent", "cylinder", "hexagon", "superquadric", "smiley"]

    if shape not in shapes:
        shape = "crescent"

    if shape == "cylinder":
        Z = np.ones_like(X)
        Z[X**2 + Y**2 < 0.5] = 0
        Z[X**2 + Y**2 > 2] = 0

    if shape == "superquadric":
        Z = np.ones_like(X)
        Z[np.abs(X)**0.5 + np.abs(Y)**0.5 > 1.5] = 0

    if shape == "hexagon":
        Z = np.ones_like(X)
        hexa = 2*np.abs(X) + np.abs(X - Y*np.sqrt(3)) +\
            np.abs(X + Y*np.sqrt(3))
        Z[hexa > 6] = 0

    if shape == "crescent":
        c = 2
        d = -1
        e = 1
        f = 0.5
        k = 1.2
        shift = 10
        Z = (c**2 - (X/e - d)**2 - (Y/f)**2)**2 + k*(c + d - X/e)**3 - shift
        Z = 1 - np.maximum(np.sign(Z), 0)

    if shape == "smiley":
        Z = np.ones_like(X)
        fac = 1.2
        x_eye = 0.5
        y_eye = 0.4
        bicorn = fac**2*(Y + 0.3)**2*(1 - fac**2*X**2) -\
                (fac**2*X**2 - 2*fac*(Y + 0.3) - 1)**2
        left_eye = (X + x_eye)**2/0.1 + (Y - y_eye)**2/0.4 - 1
        right_eye = (X - x_eye)**2/0.1 + (Y - y_eye)**2/0.4 - 1
        Z[X**2 + Y**2 > 2] = 0
        Z[bicorn > 0] = 0
        Z[left_eye < 0] = 0
        Z[right_eye < 0] = 0


    Z = scale * Z
    return Z


def data_gen(num):
    # Solve the heat equation with zero boundary conditions
    for cont in range(ntime_anim):
        Z[1:N-1, 1:N-1] = Z[1:N-1, 1:N-1] + dt*(Z[2:N, 1:N-1] +
                             Z[0:N-2, 1:N-1] + Z[1:N-1, 0:N-2] +
                             Z[1:N-1, 2:N] - 4*Z[1:N-1, 1:N-1])/dx**2

    surf = mlab.surf(X, Y, Z, colormap='autumn', warp_scale=1)
    # Change the visualization parameters.
    surf.actor.property.interpolation = 'phong'
    surf.actor.property.specular = 0.3
    surf.actor.property.specular_power = 20
    surf.module_manager.scalar_lut_manager.reverse_lut = True
    surf.module_manager.scalar_lut_manager.data_range = np.array([ 0.,  scale])

    return surf


N = 500  # Grid points
L = 2.5  # Box size
X, Y = np.mgrid[-L:L:N*1j, -L:L:N*1j]
scale = 2
Z = step_function(N, scale, X, Y, shape="smiley")
CFL = 0.125
dx = X[1, 0] - X[0, 0]
dy = dx
dt = CFL*dx**2
end_time = 0.05
time = np.arange(0, end_time, dt)
nframes = 50
ntime = time.shape[0]
ntime_anim = int(ntime/nframes)

#%% Plot frames
fname = "heat_smiley"
bgcolor = (1, 1, 1)
fig = mlab.figure(size=(1200, 1000), bgcolor=bgcolor)
fig.scene.camera.azimuth(180)
mlab.get_engine()
engine = mlab.get_engine()
scene = engine.scenes[0]
for cont in range(nframes):
    mlab.clf()
    surf = data_gen(cont)
    scene.scene.camera.position = [-8, -8,  7]
    scene.scene.camera.clipping_range = [7, 22]
    scene.scene.camera.focal_point = [0, 0, 1]
    print(cont)
    mlab.savefig("{}_{n:02d}.png".format(fname, n=cont))


