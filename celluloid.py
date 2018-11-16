from typing import List
from collections import defaultdict

from matplotlib.figure import Figure
from matplotlib.artist import Artist


class Artists:
    """Dumb class to make animations easier."""

    def __init__(self) -> None:
        # need to keep track off artists for each axis
        self.offsets = {
            'collections': defaultdict(int),
            'patches': defaultdict(int),
            'lines': defaultdict(int),
            'texts': defaultdict(int),
            'artists': defaultdict(int),
        }
        self.artists = []

    def frame(self, figure: Figure) -> List[Artist]:
        frame_artists = []
        for name in self.offsets:
            for i, ax in enumerate(figure.axes):
                start = self.offsets[name][i]
                new_artists = getattr(ax, name)[start:]
                frame_artists += new_artists
                self.offsets[name][i] += len(new_artists)
        self.artists.append(frame_artists)
        return frame_artists
