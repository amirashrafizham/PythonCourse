import pandas as pd
import numpy as np

# DATA STANDARDIZATION

starbucks = pd.read_csv('starbucks_customer.csv')
age = starbucks['age']

mean_age = np.mean(age)
print(mean_age)

std_dev_age = np.std(age)
print(std_dev_age)

ages_standardized = []

for item in age:
    num = mean_age-item
    ages_standardized.append(num/std_dev_age)

print(ages_standardized)

print(np.mean(ages_standardized))
print(np.std(ages_standardized))
