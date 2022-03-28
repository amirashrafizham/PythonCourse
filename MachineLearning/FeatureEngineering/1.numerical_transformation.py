import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# DATA CENTERING

coffee = pd.read_csv('starbucks_customer.csv')

ages = coffee['age']
print(ages)

min_age = np.min(ages)
max_age = np.max(ages)

# Spread of Data
print(max_age-min_age)

mean_age = np.mean(ages)
print(mean_age)


# Center your data
centered_ages = ages - mean_age
print(centered_ages)

plt.hist(centered_ages)
plt.show()

# Conclusion from this exercise, there are a lot of ages in the csv that is below the 27 (the mean) and a few above the mean
