from cProfile import label
import pandas as pd
import matplotlib.pyplot as plt


# Function to subplot histogram of distribution
def plot_numeric(features, dataframe):
    for i in features:
        value = dataframe[i]
        plt.ylabel("Frequency")
        plt.xlabel(i)
        plt.axvline(value.mean(), color="magenta")
        plt.axvline(value.median(), color="magenta")
        plt.title(i + "Distribution")
        plt.hist(value, bins=100)

# Function to sublot scatterplot of Features vs Label


bike = pd.read_csv('daily-bike-share.csv')

# Feature Engineering
bike['day'] = pd.DatetimeIndex(bike['dteday']).day

print(bike.describe())  # getting some basic stats


# Numeric Features EDA
numeric_features = ["temp", "atemp", "hum", "windspeed", "rentals"]


plot_numeric(numeric_features, bike)
plt.show()
