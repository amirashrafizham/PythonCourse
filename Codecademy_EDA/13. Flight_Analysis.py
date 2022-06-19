import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import statsmodels


## Read in Data
flight = pd.read_csv("flight.csv")

""" 
miles                       int64
passengers                  int64
delay                       int64
inflight_meal              object
inflight_entertainment     object
inflight_wifi              object
day_of_week                object
redeye                     object
weekend                    object
coach_price               float64
firstclass_price          float64
hours                       int6 
"""

# Task 1: Investigate the coach price


def task_1():
    print(f"mean coach price: {flight.coach_price.mean()}")
    print(f"median coach price: {flight.coach_price.median()}")

    sns.boxplot(data=flight, x='coach_price')
    plt.show()
    plt.close()


# Task 2: Investigate the price for flights more than 8 hours
def task_2():
    flight_more_than_eight = flight[flight.hours >= 8]
    print(flight_more_than_eight.head())

    print(flight_more_than_eight.coach_price.mean())
    print(flight_more_than_eight.coach_price.median())

    sns.boxplot(data=flight_more_than_eight, x="coach_price")
    plt.show()
    plt.close()


# Task 3: Investigate the flight delay distribution
def task_3():
    print(flight.delay.describe())
    delay_less_than_50 = flight[flight.delay <= 50]
    print(delay_less_than_50.head())

    sns.histplot(data=delay_less_than_50, x='delay')
    plt.show()


# Task 4: Investigate the relationship between coach and first-class price

def task_4():
    sns.scatterplot(data=flight, x='coach_price', y='firstclass_price')
    plt.show()


# Task 5: Investigate the relationship between coach_price-inflight_meal, coach_price-inflight_entertainment, coach_price-inflight_wifi
def task_5():
    sns.boxplot(data=flight, x='inflight_meal', y='coach_price')
    plt.show()
    plt.close()

    sns.boxplot(data=flight, x='inflight_entertainment', y='coach_price')
    plt.show()
    plt.close()

    sns.boxplot(data=flight, x='inflight_wifi', y='coach_price')
    plt.show()
    plt.close()


# Task 6: Investigate the relationship between number of passengers and length of flight
def task_6():
    sns.scatterplot(data=flight, x='passengers', y='hours')
    plt.show()


# Task 7: Investigate whether flight prices are more expensive on weekends or not
def task_7():
    sns.scatterplot(data=flight, y='firstclass_price',
                    x='coach_price', hue='weekend')
    plt.show()


# Task 8: Investigate whether coach prices are more expensive for redeyes/non-redeyse on each day
def task_8():
    sns.boxplot(data=flight, x='day_of_week', y='coach_price', hue='redeye')
    plt.show()
