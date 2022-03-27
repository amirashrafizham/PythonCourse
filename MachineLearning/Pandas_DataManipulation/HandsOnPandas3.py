import pandas as pd

# How to read a dataframe
df1 = pd.read_csv('county_whoville.csv')
# print(df1)


# How to read the first few dataframe

df2 = pd.read_csv('imdb.csv')
""" print(df2.head())
print(df2.info()) """


# Select Columns
df = pd.DataFrame([
    ['January', 100, 100, 23, 100],
    ['February', 51, 45, 145, 45],
    ['March', 81, 96, 65, 96],
    ['April', 80, 80, 54, 180],
    ['May', 51, 54, 54, 154],
    ['June', 112, 109, 79, 129]],
    columns=['month', 'clinic_east',
             'clinic_north', 'clinic_south',
             'clinic_west']
)

# Single Column
clinic_north = df['clinic_north']
print(type(clinic_north))


# Multiple Column

clinic_north_south = df[['clinic_north', 'clinic_south']]
print(type(clinic_north_south))

# Select Row
march = df.iloc[2]
print(march)

# Selecting Multiple Rows
april_may_june = df.iloc[3:6]
print(april_may_june)

# Filter dataframe part 1 : filter by column that has 'January'
january = df[df.month == 'January']
print(january)


# Filter dataframe part 2: filter by month = 'March' or month = 'April'
march_april = df[(df.month == 'March') | (df.month == 'April')]
print(march_april)

# Filter dataframe part 3: filter without OR '|' symbol (2 or more variables)
january_february_march = df[df.month.isin(['January', 'February', 'March'])]
print(january_february_march)
