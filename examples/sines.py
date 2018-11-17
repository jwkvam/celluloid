#!/usr/bin/env python

import numpy as np
import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot as plt
from matplotlib.animation import ArtistAnimation

from celluloid import Camera


t = np.linspace(0, 2 * np.pi, 128, endpoint=False)

fig, axes = plt.subplots(2)
camera = Camera()

for i in np.linspace(0, 2 * np.pi, 128, endpoint=False):
    axes[0].plot(t, np.sin(t + i), color='blue')
    axes[1].plot(t, np.sin(t - i), color='blue')
    plt.tight_layout()
    camera.snapshot(fig)

animation = ArtistAnimation(fig, camera.pictures, interval=50, blit=True)
animation.save(
    'sines.mp4',
    dpi=100,
    savefig_kwargs={
        # 'transparent': True,
        'frameon': False,
        # 'bbox_inches': 'tight',
        'pad_inches': 'tight'
    }
)
