from lib2to3.pgen2.pgen import DFAState
from os import removedirs
import pandas as pd
from matplotlib import pyplot as plt
from pyparsing import col
from sklearn.utils import column_or_1d
from sklearn.preprocessing import MinMaxScaler
from scipy import stats

df = pd.read_csv('grades.csv', delimiter=",", header="infer")

# print(df.head())

# Original number of rows
print(f"Original number of rows: {len(df.index)}")

# Filter rows that have NaN in the Grade column
missing_data = pd.isnull(df["Grade"])

print("---------------------------")
print("Rows that have missing data")
print(df[missing_data].head())


print("---------------------------")
# Removed NA rows in dataframe
df = df.dropna()
print(f"Number of rows after dropping na: {len(df.index)}")
print("---------------------------")

# Filters students who have passed into rows of True/False
passed = pd.Series(df["Grade"] >= 60)

# adds a new column called Pass in the dataframe, with the derived values from the filter function above
df = pd.concat([df, passed.rename("Pass")], axis=1)

grades = df['Grade']
studyHours = df['StudyHours']

# Create a function that stores the statistics and plots of a Column


def show_stats(df_column: pd.Series):
    min_val = df_column.min()
    max_val = df_column.max()
    mode_val = df_column.mode()[0]
    med_val = df_column.median()
    mean_val = df_column.mean()
    rng = df_column.max() - df_column.min()
    variance = df_column.var()
    std = df_column.std()

    print(f"Min: {min_val}\nMax: {max_val}\
        \nMode: {mode_val}\nMedian: {med_val}\nMean: {mean_val}\
        \nRange: {rng} \nVariance:{variance}\nStd Deviation: {std}")

    fig, ax = plt.subplots(2, 1, figsize=(10, 4))

    # Plot the histogram
    ax[0].hist(df_column)
    ax[0].set_ylabel('Frequency')

    # Add lines for the mean, median, and mode
    ax[0].axvline(x=min_val, color='gray', linestyle='dashed', linewidth=2)
    ax[0].axvline(x=mean_val, color='cyan', linestyle='dashed', linewidth=2)
    ax[0].axvline(x=med_val, color='red', linestyle='dashed', linewidth=2)
    ax[0].axvline(x=mode_val, color='yellow', linestyle='dashed', linewidth=2)
    ax[0].axvline(x=max_val, color='gray', linestyle='dashed', linewidth=2)

    # Plot the boxplot
    ax[1].boxplot(df_column, vert=False)
    ax[1].set_xlabel('Value')

    # Add a title to the Figure
    fig.suptitle(f'{df_column.name} Distribution')

    # Show the figure
    plt.show()


# show_stats(grades)
# show_stats(studyHours)

# Remove the outlier for StudyHours
removedOutlier = df[df['StudyHours'] > 1]  # dataframe
removedOutlier = removedOutlier['StudyHours']

# show_stats(removedOutlier)


# Create a function that shows the density of a Column

def show_density(df_column: pd.Series):
    fig = plt.figure(figsize=(10, 4))
    df_column.plot.density()

    plt.title(df_column.name + 'Density')
    plt.axvline(x=df_column.mean(), color='cyan',
                linestyle='dashed', linewidth=2)
    plt.axvline(x=df_column.median(), color='red',
                linestyle='dashed', linewidth=2)
    plt.axvline(x=df_column.mode()[0], color='yellow',
                linestyle='dashed', linewidth=2)
    plt.show()


# show_density(removedOutlier)


# Establish Relationship between Features
df = df[df['StudyHours'] > 1]  # remove outliers from the original dataframe

# Numerical: StudyHours, Grade
# Categorical: Name, Pass

# Establish Relationship between StudyHours and Pass


def relationship1():
    df.boxplot(column='StudyHours', by='Pass', figsize=(8, 5))
    plt.show()


# Establish Relationship between Features(Name, Grade and StudyHours)
def relationship2():
    df.plot(x='Name', y=['Grade', 'StudyHours'], kind='bar')
    plt.show()


# Normalize data using Scaling (MinMaxScaler)
scaler = MinMaxScaler()
df_normalized = df[['Name', 'Grade', 'StudyHours']].copy()
df_normalized[['Grade', 'StudyHours']] = scaler.fit_transform(
    df_normalized[['Grade', 'StudyHours']])

# Establish Relationship between Features (Name, Grade, StudyHours) and  after Normalization


def relationship_scaled():
    df_normalized.plot(
        x='Name', y=['Grade', 'StudyHours'], kind='bar', figsize=(8, 5))
    plt.show()


# relationship_scaled()

# Check statistical correlation between Grade and StudyHours

def show_correlation():
    correlation = df_normalized['Grade'].corr(df_normalized['StudyHours'])
    # closer to 1 means the relationship is high
    print(f"Correlation between Grade and StudyHours: {correlation:.2f}")
    df.plot(x='StudyHours', y='Grade', kind='scatter')
    plt.show()


show_correlation()

# Building the Machine Learning Model

# Get the regression slope (m) and intercept (b)
m, b, r, p, se = stats.linregress(df['StudyHours'], df['Grade'])
print('slope: {:.4f}\ny-intercept: {:.4f}'.format(m, b))

# Get the f(x), using the slope(m) and intercept(b) that you have calculated to draw the line
df['f(x)'] = (m * df['StudyHours'] + b)


# Calculate the error of each point between f(x) and actual y(Grade)
df['y'] = df['f(x)'] - df['Grade']

# Plot the Scatter Plot
df.plot(x='StudyHours', y='Grade', kind='scatter')

# Plot the regression line
plt.plot(df['StudyHours'], df['f(x)'], color='cyan')
plt.show()

# Now that we have the slope(m) and intercept (b), we can make prediction for the f(x) (Grade), with the x (Study Hours) as its input

# Example, Study Hours = 14, what is the predicted Grade?

study_hours = 14
fx = m*study_hours + b
predicted_grade = fx

print(
    f"Studying for {study_hours} hours will result in a grade of {predicted_grade:.2f}")
