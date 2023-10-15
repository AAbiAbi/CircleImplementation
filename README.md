# CircleImplementation
The 1st assignment of COEN 290


This repository provides a Python script to apply anti-aliasing to the boundary pixels of a filled circle in an image. The anti-aliasing technique used here is based on calculating the overlap of the circle's edge with each pixel and blending the circle's color with the original pixel color based on this overlap.

## Prerequisites
Python 3.11

Pillow library

You can install the required library using pip:

```bash

pip install Pillow
```

## Usage
Import the necessary libraries:
```python

from PIL import Image, ImageDraw
```

Define the anti_aliasing function:
```python

def anti_aliasing(img, center, radius, color):
    ...
```
Create an image and apply anti-aliasing:
```python

img = Image.new('RGB', (320, 240), "white")
draw = ImageDraw.Draw(img)
draw.ellipse([(60, 90), (260, 190)], fill=(255, 0, 0))

center = (160, 140)
radius = 100
color = (255, 0, 0)
anti_aliased_img = anti_aliasing(img, center, radius, color)
anti_aliased_img.show()
```
## Explanation
The anti_aliasing function works by iterating over each pixel in the image and calculating its distance from the center of the circle. It then determines the overlap of the circle's edge with the pixel. If the pixel is on the boundary of the circle, it blends the circle's color with the pixel's original color based on the overlap.

The blending is achieved using a linear interpolation formula, which takes into account the overlap of the circle's edge with the pixel. The result is a smoother appearance for the circle's boundary.



