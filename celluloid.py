class Artists:
    """Dumb class to make animations easier."""

    def __init__(self):
        self.offsets = {
            'collections': 0,
            'patches': 0,
            'lines': 0,
            'texts': 0,
            'artists': 0
        }

    def new(self, ax):
        frame_artists = []
        for name, start in self.artist.items():
            new_artists = getattr(ax, name)[start:]
            frame_artists += new_artists
            self.offsets[name] += len(new_artists)
        return frame_artists
