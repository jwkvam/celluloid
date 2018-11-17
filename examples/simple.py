#!/usr/bin/env python
"""Simple animation."""

import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot as plt
from matplotlib.animation import ArtistAnimation

from celluloid import Camera


fig = plt.figure()
camera = Camera(fig)
for i in range(10):
    plt.plot([i] * 10)
    camera.snap()


animation = camera.animate(interval=100, blit=True)
animation.save(
    'simple.mp4',
    dpi=100,
    savefig_kwargs={
        'frameon': False,
        'pad_inches': 'tight'
    }
)
