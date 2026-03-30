"""
Given the test scores of 10 students in Physics and History.

1 : compute the Pearson Correlation Coefficient. Round the result to three decimal places.
2 : compute the slope of the regression line obtained by treating Physics as the independent variable. Round the result to three decimal places.
3 : When a student scores 10 in Physics, what is his probable score in History? Compute the answer correct to one decimal place.

The two regression lines of a bivariate distribution are:
4x – 5y + 33 = 0 (line of y on x) 20x – 9y – 107 = 0 (line of x on y).

4 : Estimate the value of x when y = 7. Compute the correct answer to one decimal place.
5 : Find the variance of y when σx = 3 (ecart-type de x = 3). Compute the correct answer to one decimal place.
"""

import sys


class LinearRegression(object):
    def __init__(self, slope, intercept):
        self.slope = slope
        self.intercept = intercept

    def __getitem__(self, item):
        return self.slope * item + self.intercept

    def __str__(self):
        return f"{self.slope}x + {self.intercept}"

    def __repr__(self):
        return f"{self.__class__.__name__}({self.slope}x + {self.intercept})"


def pearsonCorrelationCoef(X: list[int | float], Y: list[int | float]):
    """
    Pearson correlation coefficient. `X` and `Y` must have the same len.
    :param X: list of numbers.
    :param Y: list of numbers.
    :return: Pearson correlation coefficient.
    """
    assert len(X) == len(Y)
    n = len(X)
    xmean, ymean = sum(X) / n, sum(Y) / n
    xcentering, ycentering = [x - xmean for x in X], [y - ymean for y in Y]
    numerator, denominatorX, denominatorY = list(), list(), list()
    for i in range(n):
        numerator.append(xcentering[i] * ycentering[i])
        denominatorX.append(xcentering[i] ** 2)
        denominatorY.append(ycentering[i] ** 2)
    num, den = sum(numerator), (sum(denominatorX) * sum(denominatorY)) ** 0.5
    return num / den


def linearRegression(X, Y) -> LinearRegression:
    """
    Linear regression. `X` and `Y` must have the same length.
    :param X: list of numbers.
    :param Y: list of numbers.
    :return: LinearRegression object.
    """
    assert len(X) == len(Y)
    n = len(X)
    xmean, ymean = sum(X) / n, sum(Y) / n
    xcentering, ycentering = [x - xmean for x in X], [y - ymean for y in Y]
    num, den = list(), list()
    for i in range(n):
        num.append(xcentering[i] * ycentering[i])
        den.append(xcentering[i] ** 2)
    slope = sum(num) / sum(den)
    intercept = ymean - slope * xmean
    return LinearRegression(slope, intercept)


sys.stdin = open("Correlation and Regression Lines.txt")  # to delete

data = sys.stdin.buffer.read().splitlines()
names: list[str] = list()
scores: list[list[float]] = list()
for d in data:
    line = d.split()
    names.append(str(line[0], 'utf-8') + str(line[1], 'utf-8'))
    scores.append(list(map(float, line[2:])))
print(round(pearsonCorrelationCoef(*scores), 3))  # 1
print(round(linearRegression(*scores).slope, 3))  # 2
print(round(linearRegression(*scores)[10], 1))  # 3
# take 20x – 9y – 107 = 0 because we want the regression of x
# get x = 9y/20 + 107/20
print(LinearRegression(9 / 20, 107 / 20)[7])  # 4
# y = 4x/5 + 33/5 and x = 9y/20 + 107/20
lry = LinearRegression(4 / 5, 33 / 5)
lrx = LinearRegression(9 / 20, 107 / 20)
# pente_y|x / pente_x|y = varY / varX
varX = pow(3, 2)
print((lry.slope / lrx.slope) * varX)  # 5
