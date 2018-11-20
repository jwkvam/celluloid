#!/usr/bin/env python
"""Complex domain coloring."""

import numpy as np
import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot as plt
from matplotlib.colors import hsv_to_rgb
from tqdm import tqdm
from celluloid import Camera

fig = plt.figure()
# hack to remove border
# https://stackoverflow.com/a/37810568/744520
fig.set_size_inches(4, 4, forward=False)
ax = plt.Axes(fig, [0, 0, 1, 1])
ax.set_axis_off()
fig.add_axes(ax)
camera = Camera(fig)

for a in tqdm(np.linspace(0, 2 * np.pi, 30, endpoint=False)):
    x = np.linspace(-3, 3, 800)
    X, Y = np.meshgrid(x, x)
    x = X + 1j * Y
    y = (x ** 2 - 2.5) * (x - 2.5 * 1j) * (x + 2.5 * 1j) * (x - 2 - 1j) ** 2 / ((x - np.exp(1j * a)) ** 2 * (x - np.exp(1j * 2 * a)) ** 2)

    H = np.angle(y) / (2 * np.pi) + .5
    r = np.log2(1. + np.abs(y))
    S = (1. + np.abs(np.sin(2. * np.pi * r))) / 2.
    V = (1. + np.abs(np.cos(2. * np.pi * r))) / 2.

    rgb = hsv_to_rgb(np.dstack((H, S, V)))
    ax.imshow(rgb)
    camera.snap()
animation = camera.animate(interval=50, blit=True)
animation.save(
    'complex.mp4',
    dpi=100,
    savefig_kwargs={
        'frameon': False,
        'pad_inches': 0
    }
)
