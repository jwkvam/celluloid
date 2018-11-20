# celluloid

[![Build Status](https://travis-ci.com/jwkvam/celluloid.svg?branch=master)](https://travis-ci.com/jwkvam/celluloid)
[![codecov](https://codecov.io/gh/jwkvam/celluloid/branch/master/graph/badge.svg)](https://codecov.io/gh/jwkvam/celluloid)
[![pypi](https://badge.fury.io/py/celluloid.svg)](https://pypi.org/project/celluloid/)
[![pypi versions](https://img.shields.io/pypi/pyversions/celluloid.svg)](https://pypi.org/project/celluloid/)

Easy Matplotlib Animation

<p align="center">
  <a href="https://github.com/jwkvam/celluloid/blob/master/examples/sines.py">
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

```python
from celluloid import Camera
fig = plt.figure()
camera = Camera(fig)
```

2. Reusing the figure and after each frame is created, take a snapshot with the camera.

```python
plt.plot(...)
plt.fancy_stuff()
camera.snap()
```

3. After all frames have been captured, create the animation.

```python
animation = camera.animate()
animation.save('animation.mp4')
```

The entire [module](https://github.com/jwkvam/celluloid/blob/master/celluloid.py) is less than 50 lines of code.

## Examples

### Minimal

As simple as it gets.

```python
from matplotlib import pyplot as plt
from celluloid import Camera

fig = plt.figure()
camera = Camera(fig)
for i in range(10):
    plt.plot([i] * 10)
    camera.snap()
animation = camera.animate()
```

<p align="center">
  <a href="https://github.com/jwkvam/celluloid/blob/master/examples/simple.py">
    <img src="https://user-images.githubusercontent.com/86304/48666133-66660980-ea70-11e8-9024-b167c21a5e83.gif">
  </a>
</p>

### Subplots

Animation at the top.

```python
import numpy as np
from matplotlib import pyplot as plt
from celluloid import Camera

fig, axes = plt.subplots(2)
camera = Camera(fig)
t = np.linspace(0, 2 * np.pi, 128, endpoint=False)
for i in t:
    axes[0].plot(t, np.sin(t + i), color='blue')
    axes[1].plot(t, np.sin(t - i), color='blue')
    camera.snap()
animation = camera.animate()
```

### Images

Domain coloring example.

```python
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.colors import hsv_to_rgb

from celluloid import Camera

fig = plt.figure()
camera = Camera(fig)

for a in np.linspace(0, 2 * np.pi, 30, endpoint=False):
    x = np.linspace(-3, 3, 800)
    X, Y = np.meshgrid(x, x)
    x = X + 1j * Y
    y = (x ** 2 - 2.5) * (x - 2.5 * 1j) * (x + 2.5 * 1j) \
        * (x - 2 - 1j) ** 2 / ((x - np.exp(1j * a)) ** 2
        * (x - np.exp(1j * 2 * a)) ** 2)

    H = np.angle(y) / (2 * np.pi) + .5
    r = np.log2(1. + np.abs(y))
    S = (1. + np.abs(np.sin(2. * np.pi * r))) / 2.
    V = (1. + np.abs(np.cos(2. * np.pi * r))) / 2.

    rgb = hsv_to_rgb(np.dstack((H, S, V)))
    ax.imshow(rgb)
    camera.snap()
animation = camera.animate()
```

<p align="center">
  <a href="https://github.com/jwkvam/celluloid/blob/master/examples/complex.py">
    <img src="https://user-images.githubusercontent.com/86304/48747098-f483f080-ec26-11e8-9734-c409e9b0c9ec.gif">
  </a>
</p>

### Legends

```python
import matplotlib
from matplotlib import pyplot as plt
from celluloid import Camera

fig = plt.figure()
camera = Camera(fig)
for i in range(5):
    t = plt.plot(range(i, i + 5))
    plt.legend(t, [f'line {i}'])
    camera.snap()
animation = camera.animate()
```

<p align="center">
  <a href="https://github.com/jwkvam/celluloid/blob/master/examples/complex.py">
    <img src="https://user-images.githubusercontent.com/86304/48750564-9100bf80-ec34-11e8-87fb-bc5c7ddcc6e7.gif">
  </a>
</p>

## Limitations

- The axes' limits should be the same for all plots. The limits of the animation will be the limits of the final plot.
- Legends will accumulate from previous frames. Pass the artists to the `legend` function to draw them separately.

## Credits

Inspired by [plotnine](https://github.com/has2k1/plotnine/blob/master/plotnine/animation.py).
