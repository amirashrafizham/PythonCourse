import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

#import data
reviews = pd.read_csv('reviews.csv')


# print column names
print(reviews.columns)

#print .info
# use the command: print(reviews.info())
""" 
#   Column           Non-Null Count  Dtype
--- ------ -------------- -----
0   clothing_id      5000 non-null   int64
1   age              5000 non-null   int64
2   review_title     4174 non-null   object
3   review_text      4804 non-null   object
4   recommended      5000 non-null   bool
5   division_name    4996 non-null   object
6   department_name  4996 non-null   object
7   review_date      5000 non-null   object
8   rating           5000 non-null   object
dtypes: bool(1), int64(2), object(6) """

# look at the counts of recommended
print(reviews['recommended'].value_counts())


# create binary dictionary
binary_dict = {True: 1, False: 0}


# transform column
reviews['recommended'] = reviews['recommended'].map(binary_dict)

# print your transformed column
# print(reviews['recommended'])
print(reviews['recommended'].value_counts())


# look at the counts of rating

print(reviews['rating'].value_counts())

# create dictionary
reviews_dict = {'Loved it': 5, 'Liked it': 4,
                'Was okay': 3, 'Not great': 2, 'Hated it': 1}

# transform rating column
reviews['rating'] = reviews['rating'].map(reviews_dict)

# print your transformed column values
print(reviews['rating'].value_counts())

# get the number of categories in a feature
print(reviews['department_name'].value_counts())


# perform get_dummies
one_hot_dept_name = pd.get_dummies(reviews['department_name'])

# join the new columns back onto the original
reviews = reviews.join(one_hot_dept_name)

# print column names
print(reviews.columns)

# transform review_date to date-time data
reviews['review_date'] = pd.to_datetime(reviews['review_date'])

# print review_date data type
print(reviews['review_date'].dtype)

# get numerical columns
reviews = reviews[['clothing_id', 'age', 'recommended', 'rating',
                   'Bottoms', 'Dresses', 'Intimate', 'Jackets', 'Tops', 'Trend']].copy()

# reset index
reviews = reviews.set_index('clothing_id')
print(reviews.head())

# instantiate standard scaler
scaler = StandardScaler()

# fit transform data
transform = scaler.fit_transform(reviews)
