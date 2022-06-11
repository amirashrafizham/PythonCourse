import pandas as pd
from scipy.stats import trim_mean
import matplotlib.pyplot as plt
import seaborn as sns


movies = pd.read_csv('movies.csv')

# Print the first 5 rows
print(movies.head())

# Print the summary statistics for all columns
print(movies.describe(include='all'))


# Quantitative Data: Calculating Central Tendency
mean_budget = movies['production_budget'].mean()
med_budget = movies['production_budget'].median()
mode_budget = movies['production_budget'].mode()

trmean_budget = trim_mean(movies['production_budget'], proportiontocut=0.2)


# Quantitative Data: Calculating Spread (The spread of a quantitative variable describes the amount of variability; it provides context for measures of central tendency)

range_budget = movies['production_budget'].max() - \
    movies['production_budget'].min()

iqr_budget = movies['production_budget'].quantile(0.75) - \
    movies['production_budget'].quantile(0.25)


var_budget = movies['production_budget'].var()
std_budget = movies['production_budget'].std()
mad_budget = movies['production_budget'].mad()

# Quantitative Data: Visualization [Boxplots & Histograms]
sns.boxplot(x='production_budget', data=movies)
# plt.show()

sns.histplot(x='production_budget', data=movies)
# plt.show()
# plt.close()


# Qualitative Data: mean(), std() don't make sense. We use frequency
genre_counts = movies['genre'].value_counts()
print(genre_counts)

# Qualitative Data: but frequency is vague, we can check the percentage of proportion of categorical data
genre_props = movies['genre'].value_counts(normalize=True)
print(genre_props)

# Qualitative Data: Visualization [Bar Chart and Pie Chart]
sns.countplot(x='genre', data=movies)
plt.show()


movies['genre'].value_counts().plot.pie()
plt.show()
plt.close()
