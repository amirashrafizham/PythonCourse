import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model

df = pd.read_csv(
    "honeyproduction.csv")

""" 
state           object
numcol         float64
yieldpercol      int64
totalprod      float64
stocks         float64
priceperlb     float64
prodvalue      float64
year             int64 
"""

prod_per_year = df.groupby('year').totalprod.mean().reset_index()

X = prod_per_year['year']
X = X.values.reshape(-1, 1)
print(X)
y = prod_per_year['totalprod']

plt.scatter(X, y)
# plt.show()

regr = linear_model.LinearRegression()
regr.fit(X, y)
slope = regr.coef_[0]
intercept = regr.intercept_

print(f"slope:{slope} and intercept: {intercept}")

y_predict = regr.predict(X)

plt.plot(X, y_predict)

nums = np.array(range(2013, 2051))
X_future = nums.reshape(-1, 1)


future_predict = regr.predict(X_future)

plt.plot(X_future, future_predict)
plt.show()
