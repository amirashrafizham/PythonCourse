from cProfile import label
from random import random
from statistics import mode
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import MeanShift
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score


# Function to sublot scatterplot of Features vs Label


bike = pd.read_csv('daily-bike-share.csv')

# Feature Engineering

# Extracting day from date
bike['day'] = pd.DatetimeIndex(bike['dteday']).day

# Numeric Features, Categorical Features and Label
numeric_features = ["temp", "atemp", "hum", "windspeed"]
categorical_features = ['season', 'mnth', 'holiday',
                        'weekday', 'workingday', 'weathersit', 'day']
label = bike['rentals']

print(bike[numeric_features].describe())
print(bike[categorical_features].describe())

# Study Correlation of Numeric Features and Label


def numeric_label():
    # Create a figure for 2 subplots (4 rows, 1 column)
    fig, ax = plt.subplots(4, 1, figsize=(8, 10))
    ax[0].scatter(x=bike['temp'], y=bike['rentals'])
    correlation = bike['rentals'].corr(bike['temp'])
    ax[0].set_title(f"rentals vs temp {correlation:.2f}")

    ax[1].scatter(x=bike['atemp'], y=bike['rentals'])
    correlation = bike['rentals'].corr(bike['atemp'])
    ax[1].set_title(f"rentals vs atemp {correlation:.2f}")

    ax[2].scatter(x=bike['hum'], y=bike['rentals'])
    correlation = bike['rentals'].corr(bike['hum'])
    ax[2].set_title(f"rentals vs hum {correlation:.2f}")

    ax[3].scatter(x=bike['windspeed'], y=bike['rentals'])
    correlation = bike['rentals'].corr(bike['windspeed'])
    ax[3].set_title(f"rentals vs windspeed {correlation:.2f}")

    plt.show()


def numeric_label_alternative():
    for col in numeric_features:
        fig = plt.figure(figsize=(9, 6))
        ax = fig.gca()
        feature = bike_data[col]
        label = bike_data['rentals']
        correlation = feature.corr(label)
        plt.scatter(x=feature, y=label)
        plt.xlabel(col)
        plt.ylabel('Bike Rentals')
        ax.set_title('rentals vs ' + col +
                     '- correlation: ' + str(correlation))
    plt.show()


def categorical_label():
    # Create a figure for 2 subplots (4 rows, 1 column)
    for col in categorical_features:
        fig = plt.figure(figsize=(9, 6))
        ax = fig.gca()
        bike.boxplot(column='rentals', by=col, ax=ax)
        ax.set_title('Label by ' + col)
        ax.set_ylabel("Bike Rentals")
    plt.show()

# For Numerical: temp and atemp shows a correlation
# For Categorical: weekends-workingday, holiday-workingday shows a trend.


# Training a Model

# Separating Features and Labels

X, y = bike[['season', 'mnth', 'holiday', 'weekday', 'workingday', 'weathersit',
             'temp', 'atemp', 'hum', 'windspeed']].values, bike['rentals'].values
print('Features:', X[:10], '\nLabels:', y[:10], sep='\n')


X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.30, random_state=0)

print('Training Set: %d rows\nTest Set: %d rows' %
      (X_train.shape[0], X_test.shape[0]))

model = LinearRegression().fit(X_train, y_train)

predictions = model.predict(X_test)
print(f"Predicted labels: {np.round(predictions)[:10]}")
print(f"Actual labels: {y_test[:10]}")

mse = mean_squared_error(y_test, predictions)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, predictions)


# Cheking the accuracy of the model
print("RMSE: ", rmse)
print("R2: ", r2)
