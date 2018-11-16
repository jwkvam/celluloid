import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot as plt
import numpy as np

from celluloid import Artists


def test_single():
    fig = plt.figure()

    arts = Artists()
    plt.plot(range(5))
    plt.plot(-np.arange(5))
    artists = arts.frame(fig)
    assert len(artists) == 2

    for _ in range(10):
        plt.plot(range(5))
        plt.plot(-np.arange(5))
        artists = arts.frame(fig)
        assert len(artists) == 2

    assert sum(len(x) for x in arts.artists) == 2 * 11


def test_two_axes():
    fig, axes = plt.subplots(2)

    arts = Artists()
    axes[0].plot(np.zeros(100))
    axes[1].plot(np.zeros(100))
    artists = arts.frame(fig)
    assert len(artists) == 2

    axes[0].plot(np.ones(100))
    axes[1].plot(np.ones(100))
    artists = arts.frame(fig)

    assert sum(len(x) for x in arts.artists) == 4
