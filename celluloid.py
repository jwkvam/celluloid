from typing import Dict, List
from collections import defaultdict

from matplotlib.figure import Figure
from matplotlib.artist import Artist


__version__ = '0.1.0-dev'


class Camera:
    """Dumb class to make animations easier."""

    def __init__(self, figure: Figure) -> None:
        self.figure = figure
        # need to keep track off artists for each axis
        self.offsets: Dict[str, Dict[int, int]] = {
            k: defaultdict(int) for k in ['collections', 'patches', 'lines', 'texts', 'artists']
        }
        self.photos: List[List[Artist]] = []

    def snap(self) -> List[Artist]:
        frame_artists: List[Artist] = []
        for name in self.offsets:
            for i, ax in enumerate(self.figure.axes):
                new_artists = getattr(ax, name)[self.offsets[name][i]:]
                frame_artists += new_artists
                self.offsets[name][i] += len(new_artists)
        self.photos.append(frame_artists)
        return frame_artists
