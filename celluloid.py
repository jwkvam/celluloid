"""Easy matplotlib animation."""
from typing import Dict, List
from collections import defaultdict

from matplotlib.figure import Figure
from matplotlib.artist import Artist
from matplotlib.animation import ArtistAnimation


__version__ = '0.1.0'


class Camera:
    """Make animations easier."""

    def __init__(self, figure: Figure) -> None:
        """Create camera from matplotlib figure."""
        self._figure = figure
        # need to keep track off artists for each axis
        self._offsets: Dict[str, Dict[int, int]] = {
            k: defaultdict(int) for k in ['collections', 'patches', 'lines', 'texts', 'artists']
        }
        self._photos: List[List[Artist]] = []

    def snap(self) -> List[Artist]:
        """Capture current state of the figure."""
        frame_artists: List[Artist] = []
        for name in self._offsets:
            for i, axis in enumerate(self._figure.axes):
                new_artists = getattr(axis, name)[self._offsets[name][i]:]
                frame_artists += new_artists
                self._offsets[name][i] += len(new_artists)
        self._photos.append(frame_artists)
        return frame_artists

    def animate(self, *args, **kwargs) -> ArtistAnimation:
        """Animate the snapshots taken.

        Uses matplotlib.animation.ArtistAnimation

        Returns
        -------
        ArtistAnimation

        """
        return ArtistAnimation(self._figure, self._photos, *args, **kwargs)
