"""
- How are students performing in their math classes?
- What do students' parents do for work?
- How often are students absent from school?
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('students.csv')

print(df.describe(include='all'))

math_grade_mean = df['math_grade'].mean()
math_grade_median = df['math_grade'].median()
math_grade_mode = df['math_grade'].mode()
math_grade_range = df['math_grade'].max() - df['math_grade'].min()
math_grade_std = df['math_grade'].std()
math_grade_mad = df['math_grade'].mad()
print(math_grade_mean)
print(math_grade_median)
print(math_grade_mode[0])
print(math_grade_range)
print(math_grade_std)
print(math_grade_mad)

# sns.histplot(df['math_grade'])
# plt.show()
# plt.clf()
# sns.boxplot(x='math_grade', data=df)
# plt.show()


print(df['Mjob'].value_counts(normalize=True))

sns.countplot(x=df['Mjob'], data=df)
plt.show()
plt.clf()
