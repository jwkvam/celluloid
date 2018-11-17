import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot as plt
import numpy as np

from celluloid import Camera


def test_single():
    fig = plt.figure()
    camera = Camera(fig)

    for _ in range(10):
        plt.plot(range(5))
        plt.plot(-np.arange(5))
        artists = camera.snap()
        assert len(artists) == 2

    assert sum(len(x) for x in camera.photos) == 2 * 10


def test_two_axes():
    fig, axes = plt.subplots(2)
    camera = Camera(fig)
    axes[0].plot(np.zeros(100))
    axes[1].plot(np.zeros(100))
    artists = camera.snap()
    assert len(artists) == 2

    axes[0].plot(np.ones(100))
    axes[1].plot(np.ones(100))
    artists = camera.snap()

    assert sum(len(x) for x in camera.photos) == 4
