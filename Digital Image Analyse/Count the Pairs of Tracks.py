import sys
from PIL import Image

sys.stdin = open("Count the Pairs of Tracks.txt")  # to delete

data = str(sys.stdin.buffer.read(), 'utf-8').splitlines()
size = list(map(int, data[0].split()))
size.reverse()
img: list[list[tuple[int, ...]]] = list()
for y in data[1:]:
    img.append([])
    for pixel in y.split():
        img[-1].append(tuple(map(int, pixel.split(','))))
im = Image.new("RGB", size)
for y, row in enumerate(img):
    for x, pixel in enumerate(row):
        im.putpixel((x, y), pixel)
im.show()
