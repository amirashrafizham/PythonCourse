import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import math
from sklearn.preprocessing import StandardScaler
import numpy as np

coffee = pd.read_csv("starbucks_customers.csv")

# Centering Data


def center_data():
    ages = coffee['age']
    min_age = ages.min()
    max_age = ages.max()

    mean_age = ages.mean()
    centered_age = ages - mean_age

    plt.hist(centered_age, bins=20)
    plt.title('Centered age')
    plt.xlabel(f'Distance from mean: {round(mean_age,2)}')
    plt.ylabel('Count')
    plt.show()


# Standardizing Data - With StandardScaler()


def standard_data():
    scaler = StandardScaler()
    ages = coffee['age']

    reshaped_ages = np.array(ages).reshape(-1, 1)
    scaled_ages = scaler.fit_transform(reshaped_ages)
    print(f"mean: {ages.mean()}")
    print(f"std: {ages.std()}")

    print(f"scaled mean: {scaled_ages.mean()}")
    print(f"scaled std: {scaled_ages.std()}")


# Binning Data

def binning_data():
    ages = coffee['age']
    max_age = ages.max()
    min_age = ages.min()

    bins = [12, 20, 30, 40, 71]

    coffee['binned_age'] = pd.cut(ages, bins, right=False)
    print(coffee.head())

    distinct_binned_ages = coffee['binned_age'].value_counts()
    distinct_binned_ages.plot(kind='bar')
    plt.show()


# Log Transformation

def log_tranform():
    cars = pd.read_csv('cars.csv')
    prices = cars['sellingprice']
    plt.hist(prices, bins=150)
    plt.title('before log transform')
    plt.show()
    plt.close()

    # Perform Log Transformation
    log_price = np.log(prices)
    plt.hist(log_price, bins=150)
    plt.title('after log transform')
    plt.show()
    plt.close()
