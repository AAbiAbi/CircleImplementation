from PIL import Image, ImageDraw
from create_circle import create_circle_edge, area_fill,anti_aliasing


img = Image.new('RGB', (320, 240))

center_x = 320 // 2
center_y = 240 // 2

# This creates a new image with a size of 320x240 pixels. 
# The image mode is 'RGB', which means it can contain red, green, and blue channels.
#  By default, the image will be black because the default color is set to (0,0,0).
pixels = img.load()

img_with_circle = create_circle_edge(img, (center_x, center_y),50, (255, 0, 0))


# The load() method gives access to the pixel data of the image. 
# You can use this to modify the image's pixels directly.
# pixels[100,100] = (255,0,0) 
# This sets the color of the pixel at position (100,100) to red. 
# The color is given as an RGB tuple, where (255,0,0) represents red.
img_with_circle.show()

img_fill = area_fill(img_with_circle, (255, 0, 0))

img_fill.show()

img_anti_aliasing = anti_aliasing(img,(center_x, center_y), 50 , (255, 0, 0))

img_anti_aliasing.show()


