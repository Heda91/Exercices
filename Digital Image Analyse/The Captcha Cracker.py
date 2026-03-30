""""
A website uses Captchas on a form in order to keep the web-bots away.
However, the captchas it generates, are quite similar each time:

- the number of characters remains the same each time
- the font and spacing is the same each time
- the background and foreground colors and texture, remain largely the same
- there is no skew in the structure of the characters.
- the captcha generator, creates strictly 5-character captchas,
and each of the characters is either an upper-case character (A-Z) or a numeral (0-9)/.

You are provided a set of twenty-five captchas, such that, each of the characters A-Z and 0-9 occur at least once
in one of the Captchas' text. From these captchas, you can identify texture, nature of the font, spacing of the font,
morphological characteristics of the letters and numerals, etc.
Download this sample set for the purpose of creating an offline model for this task.

Given a set of unseen captchas on the same web form, your task is to identify the text on each of the captchas.

## Input Format

The first line of the input will contain two integers, R and C, which represent the number of rows
and the number of columns of image pixels respectively.
A 2D Grid of pixel values will be provided (in regular text format through STDIN),
which represent the pixel-wise values from the images (which were originally in JPG or PNG formats).
Each pixel will be represented by three comma separated values in the range 0 to 255
representing the RGB components respectively.
There will be a space between successive pixels in the same row.

## Output Format

For each input file, the output should contain exactly one line containing a 5-character token,
which represents the text of the captcha.
"""

import sys

matrice = list[list[int]]
type_signature = list[tuple[tuple[int, ...], tuple[int, ...]]]
OCR: dict[tuple[tuple[int, ...], tuple[int, ...]], str] = {}


def data_to_binary(data: list[str]) -> matrice:
    img: list[list[tuple[int, ...]]] = list()
    for y in data[1:]:
        img.append([])
        for pixel in y.split():
            img[-1].append(tuple(map(int, pixel.split(','))))
    binary_img: list[list[int]] = list()
    for iy in range(len(img)):
        binary_img.append([])
        for x in img[iy]:
            binary_img[-1].append(0 if sum(x) / 3 > 100 else 1)
    return binary_img


def get_signature(binary_img: matrice) -> type_signature:
    col_sum = [sum(col) for col in zip(*binary_img)]
    row_index = 0
    signature: type_signature = list()
    while 0 in col_sum:
        if col_sum[0] == 0:
            col_sum.pop(0)
            row_index += 1
        else:
            index = col_sum.index(0)
            row_sum: list[int] = [sum(row[row_index:row_index + index]) for row in binary_img if
                                  sum(row[row_index:row_index + index]) > 0]
            signature.append((tuple(row_sum), tuple(col_sum[:index])))
            col_sum = col_sum[index:]
            row_index += index
    return signature


training = False
if training:
    inputs = [open(f"captcha_training/input/input{i:02}.txt") for i in range(25)]
    outputs = [open(f"captcha_training/output/output{i:02}.txt") for i in range(25)]
    for inp, out in zip(inputs, outputs):
        data = inp.read().splitlines()
        signature = get_signature(data_to_binary(data))
        chars = list(out.read())[:-1]
        for s, c in zip(signature, chars):
            x = OCR.setdefault(s, c)
            assert x == c, f"Une signature ne peux avoir plusieurs lettres: {s} -> {c} or {x} ?"
    # print(OCR)
    sys.stdin = open("captcha_training/input/input10.txt")  # to delete

    data = str(sys.stdin.buffer.read(), 'utf-8').splitlines()
    print(''.join([OCR[s] for s in get_signature(data_to_binary(data))]))
else:
    OCR = {((7, 2, 2, 2, 6, 2, 2, 2, 2, 7), (10, 10, 3, 3, 3, 3, 2)): 'E',  # trouvé grace au training
           ((5, 4, 2, 2, 2, 5, 4, 4, 4, 5), (6, 8, 4, 2, 2, 3, 7, 5)): 'G',
           ((4, 4, 4, 4, 2, 2, 2, 2, 2, 2), (2, 3, 2, 7, 7, 2, 3, 2)): 'Y',
           ((4, 4, 4, 4, 4, 4, 4, 4, 4, 4), (10, 10, 2, 4, 4, 4, 4, 2)): 'K',
           ((2, 3, 4, 4, 4, 4, 8, 2, 2, 2), (2, 3, 3, 3, 3, 10, 10, 1)): '4',
           ((7, 4, 4, 4, 7, 5, 4, 4, 4, 4), (10, 10, 3, 3, 4, 4, 8, 5)): 'R',
           ((5, 4, 3, 2, 2, 2, 2, 3, 4, 5), (6, 8, 4, 2, 2, 2, 4, 4)): 'C',
           ((5, 4, 2, 2, 3, 2, 2, 2, 4, 5), (2, 4, 2, 3, 3, 7, 7, 3)): '3',
           ((7, 2, 2, 5, 5, 2, 2, 4, 4, 4), (6, 7, 4, 3, 3, 5, 6, 3)): '5',
           ((4, 4, 3, 2, 5, 5, 4, 4, 4, 4), (6, 8, 5, 3, 3, 6, 6, 2)): '6',
           ((4, 4, 4, 4, 4, 4, 4, 4, 4, 4), (6, 8, 4, 2, 2, 4, 8, 6)): 'O',
           ((4, 4, 4, 4, 6, 6, 6, 8, 6, 4), (10, 10, 2, 4, 4, 2, 10, 10)): 'W',
           ((2, 3, 4, 2, 2, 2, 2, 2, 2, 6), (2, 3, 10, 10, 1, 1)): '1',
           ((4, 2, 2, 2, 2, 2, 2, 3, 4, 3), (2, 2, 2, 3, 9, 8)): 'J',
           ((4, 4, 4, 2, 2, 2, 2, 2, 2, 8), (2, 4, 5, 4, 4, 5, 5, 3)): '2',
           ((8, 2, 2, 2, 2, 2, 2, 2, 2, 2), (3, 4, 3, 3, 3, 3, 4, 3)): '7',
           ((4, 4, 4, 4, 4, 4, 4, 4, 2, 2), (3, 6, 5, 4, 4, 5, 6, 3)): 'V',
           ((2, 2, 2, 2, 2, 2, 2, 2, 2, 7), (10, 10, 1, 1, 1, 1, 1)): 'L',
           ((6, 2, 2, 2, 2, 2, 2, 2, 2, 6), (2, 2, 10, 10, 2, 2)): 'I',
           ((4, 4, 4, 4, 4, 4, 6, 6, 4, 5), (6, 8, 4, 3, 4, 5, 8, 7)): 'Q',
           ((8, 2, 2, 2, 2, 2, 2, 2, 2, 2), (1, 1, 1, 10, 10, 1, 1, 1)): 'T',
           ((2, 4, 4, 4, 4, 4, 8, 4, 4, 4), (7, 8, 3, 3, 3, 3, 8, 7)): 'A',
           ((6, 4, 4, 4, 4, 4, 4, 4, 4, 6), (10, 10, 2, 2, 2, 4, 8, 6)): 'D',
           ((7, 2, 2, 2, 2, 2, 2, 2, 2, 7), (4, 5, 4, 4, 4, 5, 4)): 'Z',
           ((4, 6, 8, 6, 6, 6, 4, 4, 4, 4), (10, 10, 2, 4, 4, 2, 10, 10)): 'M',
           ((4, 4, 4, 4, 4, 4, 4, 4, 4, 4), (8, 9, 2, 1, 1, 2, 9, 8)): 'U',
           ((4, 5, 6, 6, 6, 6, 6, 5, 5, 4), (10, 10, 3, 4, 3, 3, 10, 10)): 'N',
           ((4, 4, 4, 4, 5, 5, 2, 3, 4, 4), (2, 6, 6, 3, 3, 5, 8, 6)): '9',
           ((6, 4, 2, 2, 6, 2, 2, 2, 4, 6), (4, 7, 3, 3, 3, 3, 8, 5)): 'S',
           ((6, 4, 4, 4, 6, 4, 4, 4, 4, 6), (10, 10, 3, 3, 3, 7, 7, 3)): 'B',
           ((7, 4, 4, 4, 7, 2, 2, 2, 2, 2), (10, 10, 2, 2, 2, 2, 5, 3)): 'P',
           ((4, 4, 4, 4, 2, 2, 4, 4, 4, 4), (4, 6, 4, 4, 4, 4, 6, 4)): 'X',
           ((2, 4, 4, 4, 4, 4, 4, 4, 4, 2), (4, 6, 4, 4, 4, 4, 6, 4)): '0',
           ((4, 4, 4, 4, 8, 4, 4, 4, 4, 4), (10, 10, 1, 1, 1, 1, 10, 10)): 'H',
           ((4, 4, 4, 4, 4, 4, 4, 4, 4, 4), (3, 7, 7, 3, 3, 7, 7, 3)): '8',
           ((8, 2, 2, 2, 6, 2, 2, 2, 2, 2), (10, 10, 2, 2, 2, 2, 1, 1)): 'F'}
    sys.stdin = open("The Captcha Cracker.txt")  # to delete

    data = str(sys.stdin.buffer.read(), 'utf-8').splitlines()
    print(''.join([OCR[s] for s in get_signature(data_to_binary(data))]))
