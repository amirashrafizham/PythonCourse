import pandas as pd
import numpy as np

coffee = pd.read_csv('starbucks_customer.csv')


spent = coffee['spent']
print(spent)

max_spent = np.max(spent)
min_spent = np.min(spent)
spent_range = max_spent - min_spent

print(spent_range)

spent_normalized = (spent - min_spent) / spent_range
print(spent_normalized)
