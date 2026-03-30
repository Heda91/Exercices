"""
Charlie wants to buy office space and has conducted a survey of the area. He has quantified and normalized various office space features, and mapped them to values between 0 and 1. Each row in Charlie's data table contains these feature values followed by the price per square foot. However, some prices are missing. Charlie needs your help to predict the missing prices.

The prices per square foot are approximately a polynomial function of the features, and you are tasked with using this relationship to predict the missing prices for some offices.

The prices per square foot, are approximately a polynomial function of the features in the observation table. This polynomial always has an order less than 4

## Input Format

The first line contains two space separated integers, F and N. Over here, F is the number of observed features. N is the number of rows for which features as well as price per square-foot have been noted.
This is followed by a table with F+1 columns and N rows with each row in a new line and each column separated by a single space. The last column is the price per square foot.

The table is immediately followed by integer T followed by T rows containing F space-separated columns.

## Output Format

T lines. Each line 'i' contains the predicted price for the 'i'th test case.
"""
import sys

import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.preprocessing import PolynomialFeatures

sys.stdin = open('Polynomial Regression Input.txt')

data = sys.stdin.buffer.read().splitlines()
Fstr, Nstr = data.pop(0).split()
F, N = int(Fstr), int(Nstr)
dataX, dataY = [], []
for d in data[:N]:
    d = list(map(float, d.split()))
    dataX.append(d[:F] + [1])
    dataY.append(d[F])
# independent value
X = pd.DataFrame(data=dataX, columns=[f'feat_{x + 1}' for x in range(F)] + ["bias"])
# target value
Y = pd.DataFrame(data=dataY, columns=["price"])
# predictions values
T = int(data[N])
X_pred = pd.DataFrame(data=[list(map(float, d.split())) + [1] for d in data[N + 1:N + T + 1]],
                      columns=[f'feat_{x + 1}' for x in range(F)] + ["bias"])

r_list = list()
for d in range(1, 5):
    poly_reg = PolynomialFeatures(degree=d)
    X_poly = poly_reg.fit_transform(X)
    regressor_poly = LinearRegression()
    regressor_poly.fit(X_poly, Y)
    y_poly_pred = regressor_poly.predict(X_poly)
    predictions = poly_reg.fit_transform(X_pred)
    pred = regressor_poly.predict(predictions)
    r_list.append((r2_score(Y, y_poly_pred), pred))

print('\n'.join(list(map(lambda x: str(x[0]), max(r_list, key=lambda r: r[0])[1]))))
