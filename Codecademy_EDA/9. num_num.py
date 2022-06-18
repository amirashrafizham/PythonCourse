import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from scipy.stats import pearsonr

housing = pd.read_csv("housing_sample.csv")


# Use scatter plot for relationship between 2 numerical categories
plt.scatter(x=housing['beds'], y=housing['sqfeet'])


# Finding the covariance to establish the relationships
cov_mat_sqfeet_beds = np.cov(housing['beds'], housing['sqfeet'])
print(cov_mat_sqfeet_beds)

cov_sqfeet_beds = 228.2

# Using Pearson's correlation to establish the relationship
corr_sqfeet_beds, p = pearsonr(housing.beds, housing.sqfeet)
print(corr_sqfeet_beds)
