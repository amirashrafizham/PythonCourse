import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

students = pd.read_csv('students2.csv')


scores_urban = students[students.address == 'U'].G3
scores_rural = students[students.address == 'R'].G3

# calculate means for each group:
scores_urban_mean = scores_urban.mean()
scores_rural_mean = scores_rural.mean()

# print mean scores:
print('Mean score - students w/ urban address:')
print(scores_urban_mean)
print('Mean score - students w/ rural address:')
print(scores_rural_mean)

# calculate mean difference:
mean_diff = scores_urban_mean - scores_rural_mean

# print mean difference
print('Mean difference:')
print(mean_diff)

# calculate medians for each group:
scores_urban_median = scores_urban.median()
scores_rural_median = scores_rural.median()

# print median scores
print('Median score - students w/ urban address:')
print(scores_urban_median)
print('Median score - students w/ rural address:')
print(scores_rural_median)

# calculate median difference
median_diff = scores_urban_median - scores_rural_median

# using a boxplot for binary column
sns.boxplot(data=students, x='address', y='G3')
plt.show()
plt.close()


# using a histogram
plt.hist(scores_urban, color="blue", label="Urban", density=True, alpha=0.5)
plt.hist(scores_rural, color="red", label="Rural", density=True, alpha=0.5)
plt.legend()
plt.show()
plt.close()

# using a boxplot for non-binary column
sns.boxplot(data=students, x='Fjob', y='G3')
plt.show()
