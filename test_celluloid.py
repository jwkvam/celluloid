"""Test animations."""
# pylint: disable=wrong-import-position
import numpy as np
import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot as plt

from celluloid import Camera


def test_single():
    """Test plt.figure()"""
    fig = plt.figure()
    camera = Camera(fig)

    for _ in range(10):
        plt.plot(range(5))
        plt.plot(-np.arange(5))
        artists = camera.snap()
        assert len(artists) == 2

    # pylint: disable=protected-access
    assert sum(len(x) for x in camera._photos) == 2 * 10

    anim = camera.animate()
    assert len(list(anim.frame_seq)) == 10


def test_two_axes():
    """Test subplots."""
    fig, axes = plt.subplots(2)
    camera = Camera(fig)
    axes[0].plot(np.zeros(100))
    axes[1].plot(np.zeros(100))
    artists = camera.snap()
    assert len(artists) == 2

    axes[0].plot(np.ones(100))
    axes[1].plot(np.ones(100))
    artists = camera.snap()

    # pylint: disable=protected-access
    assert sum(len(x) for x in camera._photos) == 4

    anim = camera.animate()
    assert len(list(anim.frame_seq)) == 2
