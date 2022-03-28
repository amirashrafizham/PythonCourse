import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler

coffee = pd.read_csv('starbucks_customer.csv')
spent = coffee['spent']

mmscaler = MinMaxScaler()

# reshape our array to prepare it for the mmscaler
spent_reshaped = np.array(spent).reshape(-1, 1)

# .fit_transform our reshaped data
reshaped_scaled = mmscaler.fit_transform(spent_reshaped)

print(np.min(reshaped_scaled))
print(np.max(reshaped_scaled))
