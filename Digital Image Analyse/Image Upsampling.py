"""
To reduce the size of a 2-dimensional image, I, containing R rows and C columns of pixels,
the image is downsampled using a crude algorithm.

The downsampling algorithm begins sampling from the top-left pixel position, (0,0),
of the original image and then proceeds to retain only those pixels which are located in those positions where both
the row number and the column number are either 0, or integer multiples of some integer N.
The downsampled image only contains r rows and c columns where these values correspond to {1+floor((R-1)/N)}
and {1+floor((C-1)/N)}

## Task

You are provided with the RGB values for a downsampled image and the downsampling coefficient (N).
Given the size of the original image (and assuming that the algorithm used for downsampling is the one described above),
restore the original image using the interpolation or upsampling algorithm of your choice.

## Input Format

The first line contains 3 space-separated integers, r, c and N.
The second line contains 2 space-separated integers, R and C.

The R subsequent lines describe the 2D grid representing the pixel-wise values from the images.
Each line contains C pixels, and each pixel is represented by three comma-separated values in the range from 0 to 255
denoting the respective *Blue, Green, and Red* components. There is a space between successive pixels in the same row.

No input test case will exceed 3MB in size. This is the size of the RGB test matrix, NOT the original image from which it was generated.

## Output Format

Print a 2D grid of pixel values describing the upsampled image.
Your output should follow the same format as the grid received as input.

Note: You should only print the grid; there is no need to specify the number of rows and columns here.
"""
import sys
from itertools import batched

img_int = list[list[tuple[int, ...]]]


def img_int_to_str(img: img_int) -> list[str]:
    img_str: list[str] = list()
    for row in img:
        img_str.append(' '.join([','.join(map(str, p)) for p in row]))
    return img_str


def img_str_to_int(data: list[str]) -> img_int:
    img: img_int = list()
    for y in data:
        img.append([])
        for pixel in y.split():
            img[-1].append(tuple(map(int, pixel.split(','))))
    return img


def upsampling(img: img_int) -> img_int:
    def upsampling_x(y: list[tuple[int, ...]]):
        rgb: list[tuple[int, ...]] = list(zip(*y))
        y_add = (tuple(zip(*[((pair[1] - pair[0]) / N for pair in zip(p, p[1:])) for p in rgb])))
        y_new: list[tuple[int, ...]] = list()
        for i, x in enumerate(y[:-1]):
            y_new.append(x)
            for n in range(1, N):
                add = (round(n * a) for a in y_add[i])
                y_new.append(tuple(map(sum, zip(x, add))))
        y_new.extend((C - len(y_new)) * [y[-1]])
        return y_new

    def upsampling_y(y1: list[tuple[int, ...]], y2: list[tuple[int, ...]]) -> list[list[tuple[int, ...]]]:
        rgb: list[tuple[int, ...]] = [(y1[i][j], y2[i][j]) for i in range(len(y1)) for j in range(3)]
        y_add = [(p[1] - p[0]) / N for p in rgb]
        y_new = list()
        for n in range(1, N):
            y_new.append(
                [tuple(map(sum, zip(t1, t2))) for t1, t2 in zip(batched((round(n * a) for a in y_add), 3), y1)])
        return y_new

    upsampled_img: img_int = list()
    upsampled_x: img_int = list()
    for y in img:
        upsampled_x.append(upsampling_x(y))
    for i, y in enumerate(upsampled_x[:-1]):
        upsampled_img.append(upsampled_x[i])
        upsampled_img.extend(upsampling_y(y, upsampled_x[i + 1]))
    upsampled_img.extend((R - len(upsampled_img)) * [img[-1]])
    return upsampled_img


sys.stdin = open("Image Upsampling.txt")  # to delete

data = str(sys.stdin.buffer.read(), 'utf-8').splitlines()
r, c, N = map(int, data[0].split())
R, C = map(int, data[1].split())
img = img_str_to_int(data[2:])
upsampled_img = upsampling(img)
testcase = img_str_to_int(str(open("Image Upsampling testcase.txt").read()).splitlines())


def scoring(img: img_int, testcase: img_int) -> float:
    def s(z: tuple[tuple[int, ...], tuple[int, ...]]) -> float:
        return (sum([pow(p[0] - p[1], 2) for p in zip(z[0], z[1])]) / 3) ** 0.5

    score = [sum([s(z) for z in zip(img[i], testcase[i])]) / C for i in range(R)]
    return sum(score) / R


# print(scoring(upsampled_img, testcase))
# print('\n'.join(img_int_to_str(upsampled_img)))


# print(img_str)
def upsample(img, R, C, N):
    r, c = len(img), len(img[0])
    res = []

    for i in range(R):
        row = []
        y = i / N
        y0 = int(y)
        y1 = min(y0 + 1, r - 1)
        dy = y - y0

        for j in range(C):
            x = j / N
            x0 = int(x)
            x1 = min(x0 + 1, c - 1)
            dx = x - x0

            p00 = img[y0][x0]
            p01 = img[y0][x1]
            p10 = img[y1][x0]
            p11 = img[y1][x1]

            pixel = []
            for k in range(3):  # RGB
                val = (
                        p00[k] * (1 - dx) * (1 - dy) +
                        p01[k] * dx * (1 - dy) +
                        p10[k] * (1 - dx) * dy +
                        p11[k] * dx * dy
                )
                pixel.append(round(val))

            row.append(tuple(pixel))
        res.append(row)

    return res


"""
chat_rep = upsample(img, R, C, N)
score = list()
for i in range(R):
    score.append(sum([scoring(z) for z in zip(chat_rep[i], testcase[i])]) / C)
print(sum(score) / R)
"""
