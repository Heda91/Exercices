"""
Consider the following binary image where 0 is the background, and 1 represents a pixel on an object.

If you segment this image using an algorithm based on simple 8 pixel connectivity,
how many 8-connected objects do you obtain ?
"""

image = [[0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 1, 0],
         [1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 1],
         [1, 1, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0],
         [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0]]


def count_object(image: list[list[int]]) -> int:
    object_count = 0
    pixels = set()
    for iy in range(len(image)):
        for ix in range(len(image[iy])):
            if image[iy][ix] == 1:
                pixels.add((iy, ix))
    file = list()
    while len(pixels) > 0:
        file.append(pixels.pop())
        object_count += 1
        while len(file) > 0:
            py, px = file.pop()
            for iy in range(-1, 2):
                for ix in range(-1, 2):
                    p = (py + iy, px + ix)
                    if p in pixels:
                        pixels.remove(p)
                        file.append(p)
    return object_count


print(count_object(image))
