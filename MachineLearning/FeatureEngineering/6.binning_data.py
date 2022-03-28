from email.errors import MissingHeaderBodySeparatorDefect
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

coffee = pd.read_csv('starbucks_customer.csv')
ages = coffee['age']

min_age = np.min(ages)
max_age = np.max(ages)

print(min_age)
print(max_age)

age_bins = [12, 20, 30, 40, 71]

coffee['binned_ages'] = pd.cut(ages, age_bins, right=False)

print(coffee['binned_ages'].head(10))

coffee['binned_ages'].value_counts().plot(kind='bar')
plt.show()
