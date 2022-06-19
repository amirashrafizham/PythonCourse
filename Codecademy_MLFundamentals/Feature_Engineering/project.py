import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OrdinalEncoder
from sklearn.preprocessing import StandardScaler

reviews = pd.read_csv('reviews.csv')

print(reviews.info())
"""
clothing_id         int64
age                 int64
review_title       object
review_text        object
recommended          bool
division_name      object
department_name    object
review_date        object
rating             object
"""

# Label Encoding for recommended column
label_encoder = LabelEncoder()
reviews['recommend_encode'] = label_encoder.fit_transform(reviews.recommended)


# Ordinal Encoding for the rating column
ordinal_encoder = OrdinalEncoder(
    categories=[['Loved it', 'Liked it', 'Was okay', 'Not great', 'Hated it']])

rating_reshaped = reviews['rating'].values.reshape(-1, 1)

reviews['rating_encode'] = ordinal_encoder.fit_transform(rating_reshaped)

# One Hot Encoding for the department_name

one_hot_department_name = pd.get_dummies(reviews['department_name'])
reviews = reviews.join(one_hot_department_name)


# Transform datetime for review_date

reviews['review_datetime'] = pd.to_datetime(reviews['review_date'])


# Transform for numerical data by Scaling

print(reviews.dtypes)
""" 
age                          int64
review_title                object
review_text                 object
recommended                   bool
division_name               object
department_name             object
review_date                 object
rating                      object
recommend_encode             int64
rating_encode              float64
Bottoms                      uint8
Dresses                      uint8
Intimate                     uint8
Jackets                      uint8
Tops                         uint8
Trend                        uint8
review_datetime     datetime64[ns] 
"""

numerical_reviews = reviews[['clothing_id', 'age', 'recommend_encode',
                             'Bottoms', 'Dresses', 'Intimate', 'Tops', 'Trend']]

numerical_reviews = numerical_reviews.set_index('clothing_id')

standard_scaler = StandardScaler()

scaled_numerical_reviews = standard_scaler.fit_transform(numerical_reviews)
