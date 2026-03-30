"""
You need to construct a feature in a Digital Camera, which will auto-detect and suggest to the photographer
whether the picture should be clicked in day or night mode,
depending on whether the picture is being clicked in the daytime or at night.

You only need to implement this feature for cases which are directly distinguishable to the eyes
(and not fuzzy scenarios such as dawn, dusk, sunrise, sunset, overcast skies
which might require more complex aperture adjustments on the camera).

## Input Format

A 2D Grid of pixel values will be provided (in regular text format through STDIN),
which represent the pixel wise values from the images (which were originally in JPG or PNG formats).
Each pixel will be represented by three comma separated values in the range 0 to 255
representing the RGB components respectively.
There will be a space between successive pixels in the same row.

## Output Format

Just one word: 'day' or 'night'. Do NOT include the single quote marks.
"""

import sys

sys.stdin = open("Digital Camera Autodetect - Day or Night.txt")  # to delete

data = sys.stdin.buffer.read().splitlines()
img: list[list[tuple[int, ...]]] = list()
for y in data:
    img.append([])
    for pixel in y.split():
        img[-1].append(tuple(map(int, pixel.split(b','))))
total = 0
count = 0
for row in img:
    for (r, g, b) in row:
        total += 0.299 * r + 0.587 * g + 0.114 * b  # ratio des couleurs pour l'oeil humain
        count += 1

avg = total / count
print('day' if avg > 85 else 'night')  # 85 est une valeur a jaugé (entre 80 et 130)
