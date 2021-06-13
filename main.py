import curses
import time
from PIL import Image

img = Image.open('default.png')
pixel_map = img.load()
pixel = pixel_map[1,0]
print(pixel)