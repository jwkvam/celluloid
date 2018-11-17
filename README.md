# celluloid

[![Build Status](https://travis-ci.com/jwkvam/celluloid.svg?branch=master)](https://travis-ci.com/jwkvam/celluloid)

Easy matplotlib animation

<p align="center">
  <img src="https://user-images.githubusercontent.com/86304/48657442-9c11e080-e9e5-11e8-9f54-f46a960be7dd.gif">
</p>

```python
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.animation import ArtistAnimation
from celluloid import Camera

fig = plt.figure()
camera = Camera(fig)
for _ in range(10):
    plt.plot(t, np.sin(t + i), color='blue')
    camera.snap()
animation = ArtistAnimation(fig, camera.photos)
```

```python
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.animation import ArtistAnimation
from celluloid import Camera

fig, axes = plt.subplots(2)
camera = Camera(fig)
t = np.linspace(0, 2 * np.pi, 128, endpoint=False)
for i in np.linspace(0, 2 * np.pi, 128, endpoint=False):
    axes[0].plot(t, np.sin(t + i), color='blue')
    axes[1].plot(t, np.sin(t - i), color='blue')
    camera.snap()
animation = ArtistAnimation(fig, camera.photos)
```

## Credits

Inspired by [plotnine](https://github.com/has2k1/plotnine/blob/master/plotnine/animation.py).
