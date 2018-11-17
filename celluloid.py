from typing import Dict, List
from collections import defaultdict

from matplotlib.figure import Figure
from matplotlib.artist import Artist


__version__ = '0.1.0-dev'


class Camera:
    """Dumb class to make animations easier."""

    def __init__(self) -> None:
        # need to keep track off artists for each axis
        self.offsets: Dict[str, Dict[int, int]] = {
            'collections': defaultdict(int),
            'patches': defaultdict(int),
            'lines': defaultdict(int),
            'texts': defaultdict(int),
            'artists': defaultdict(int),
        }
        self.photos: List[List[Artist]] = []

    def snap(self, figure: Figure) -> List[Artist]:
        frame_artists: List[Artist] = []
        for name in self.offsets:
            for i, ax in enumerate(figure.axes):
                start = self.offsets[name][i]
                new_artists = getattr(ax, name)[start:]
                frame_artists += new_artists
                self.offsets[name][i] += len(new_artists)
        self.photos.append(frame_artists)
        return frame_artists
