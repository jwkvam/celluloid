from typing import Dict, List
from collections import defaultdict

from matplotlib.figure import Figure
from matplotlib.artist import Artist


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
        self.artists: List[List[Artist]] = []

    def snapshot(self, figure: Figure) -> List[Artist]:
        frame_artists: List[Artist] = []
        for name in self.offsets:
            for i, ax in enumerate(figure.axes):
                start = self.offsets[name][i]
                new_artists = getattr(ax, name)[start:]
                frame_artists += new_artists
                self.offsets[name][i] += len(new_artists)
        self.artists.append(frame_artists)
        return frame_artists
