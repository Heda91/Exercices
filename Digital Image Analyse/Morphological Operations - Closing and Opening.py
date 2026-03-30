"""
You are provided an image B, the structuring element S which its origin is the middle pixel.

What is the number of pixels marked 1 in the image obtained after B is opened with the structuring element S ?
What is the number of pixels marked 1 in the image obtained after B is closed with the structuring element S ?
"""

from typing import Callable, Iterable

matrice = list[list[int]]

B = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 1, 1, 1, 1, 1, 1, 1, 0, 0],
     [0, 0, 0, 0, 1, 1, 1, 1, 0, 0],
     [0, 0, 0, 0, 1, 1, 1, 1, 0, 0],
     [0, 0, 0, 1, 1, 1, 1, 1, 0, 0],
     [0, 0, 0, 0, 1, 1, 1, 1, 0, 0],
     [0, 0, 0, 1, 1, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

S = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
B2 = [[0, 0, 0, 0],
      [0, 1, 1, 0],
      [0, 0, 0, 0]]
S2 = [[1, 0], [1, 1]]


def over_matrice(B: matrice, S: matrice, origin_xy: tuple[int, int], fct: Callable[[Iterable], int | bool]) -> matrice:
    xo, yo = origin_xy
    I: matrice = list()
    Sr = S.copy()
    [s.reverse() for s in Sr]
    Sr.reverse()
    for yb in range(len(B)):
        I.append(list())
        for xb in range(len(B[yb])):
            p = list()
            for ys in range(len(Sr)):
                for xs in range(len(Sr[ys])):
                    if Sr[ys][xs] == 1:
                        if 0 <= (yb + ys - yo) < len(B) and 0 <= (xb + xs - xo) < len(B[ys]):
                            p.append(B[yb + ys - yo][xb + xs - xo])
                        else:
                            p.append(0)
            I[yb].append(int(fct(p)))
    return I


def print_matrice(I: matrice) -> None:
    for y in range(len(I)):
        for x in range(len(I[y])):
            print(I[y][x], end="")
        print()


def count_matrice(I: matrice, x) -> int:
    c = 0
    for y in range(len(I)):
        c += I[y].count(x)
    return c


dilation = any
erosion = all
# closing
"""
mat_dila_clos = over_matrice(B, S, (1, 1), dilation)
mat_ero_clos = over_matrice(mat_dila_clos, S, (1, 1), erosion)
print_matrice(B)
print('-------------------------------')
print_matrice(mat_dila_clos)
print('-------------------------------')
print_matrice(mat_ero_clos)
print('-------------------------------')
print(count_matrice(mat_ero_clos, 1))
# """
# opening
"""
mat_ero_open = over_matrice(B, S, (1, 1), erosion)
mat_dila_open = over_matrice(mat_ero_open, S, (1, 1), dilation)
print_matrice(B)
print('-------------------------------')
print_matrice(mat_ero_open)
print('-------------------------------')
print_matrice(mat_dila_open)
print('-------------------------------')
print(count_matrice(mat_dila_open, 1))
# """
