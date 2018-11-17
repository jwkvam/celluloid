# celluloid

[![Build Status](https://travis-ci.com/jwkvam/celluloid.svg?branch=master)](https://travis-ci.com/jwkvam/celluloid)
[![codecov](https://codecov.io/gh/jwkvam/celluloid/branch/master/graph/badge.svg)](https://codecov.io/gh/jwkvam/celluloid)

Easy Matplotlib Animation

<p align="center">
  <a href="https://github.com/jwkvam/celluloid/examples/sines.py">
    <img src="https://user-images.githubusercontent.com/86304/48657442-9c11e080-e9e5-11e8-9f54-f46a960be7dd.gif">
  </a>
</p>

Creating animations should be easy.
This module makes it easy to adapt your existing visualization code to create an animation.

## Install

```
pip install celluloid
```

## Manual

Follow these steps:

1. Create a matplotlib `Figure` and create a `Camera` from it:

```
fig = plt.figure()
camera = Camera(fig)
```

2. Reusing the figure and after each frame is created, take a snapshot with the camera.

```
plt.plot(...)
plt.fancy_stuff()
camera.snap()
```

3. After all frames have been captured, create the animation.

```
animation = camera.animate()
animation.save('animation.mp4')
```

The entire [module](https://github.com/jwkvam/celluloid/blob/master/celluloid.py) is less than 50 lines of code.

## Examples

```python
import numpy as np
from matplotlib import pyplot as plt
from celluloid import Camera

fig = plt.figure()
camera = Camera(fig)
for i in range(10):
    plt.plot(range(i, i + 5))
    camera.snap()
animation = camera.animate()
```

```python
import numpy as np
from matplotlib import pyplot as plt
from celluloid import Camera

fig, axes = plt.subplots(2)
camera = Camera(fig)
t = np.linspace(0, 2 * np.pi, 128, endpoint=False)
for i in np.linspace(0, 2 * np.pi, 128, endpoint=False):
    axes[0].plot(t, np.sin(t + i), color='blue')
    axes[1].plot(t, np.sin(t - i), color='blue')
    camera.snap()
animation = camera.animate()
```

## Credits

Inspired by [plotnine](https://github.com/has2k1/plotnine/blob/master/plotnine/animation.py).
