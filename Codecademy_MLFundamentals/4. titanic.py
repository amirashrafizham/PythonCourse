from random import sample
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Load the passenger data
passengers = pd.read_csv('passengers.csv')
""" 
PassengerId      int64
Survived         int64
Pclass           int64
Name            object
Sex             object
Age            float64
SibSp            int64
Parch            int64
Ticket          object
Fare           float64
Cabin           object
Embarked        object 
"""

# Update sex column to numerical
sex_dict = {'female': 1, 'male': 0}
passengers['Sex'] = passengers['Sex'].map(sex_dict)

# Fill the nan values in the age column
mean = np.round(passengers['Age'].mean(skipna=True), 1)
passengers['Age'].fillna(mean, inplace=True)

# Create a first class column

passengers['FirstClass'] = passengers['Pclass'].apply(
    lambda x: 1 if x == 1 else 0)

# Create a second class column

passengers['SecondClass'] = passengers['Pclass'].apply(
    lambda x: 1 if x == 2 else 0)

# Select the desired features

features = passengers[['Sex', 'Age', 'FirstClass', 'SecondClass']]

label = passengers[['Survived']]

# Perform train, test, split
X_train, X_test, y_train, y_test = train_test_split(
    features, label, test_size=0.30, random_state=0)


# Scale the feature data so it has mean = 0 and standard deviation = 1
scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Create and train the model
model = LogisticRegression()
model.fit(X_train, y_train)


# Score the model on the train data
print(model.score(X_train, y_train))


# Score the model on the test data
print(model.score(X_test, y_test))


# Analyze the coefficients
print(model.coef_)


# Sample passenger features
Jack = np.array([0.0, 20.0, 0.0, 0.0])
Rose = np.array([1.0, 17.0, 1.0, 0.0])
You = np.array([1.0, 27.0, 0.0, 1.0])

# Combine passenger arrays
sample_passengers = np.array([Jack, Rose, You])

# Scale the sample passenger features
sample_passengers = scaler.transform(sample_passengers)

# Make survival predictions!

print(model.predict(sample_passengers))
print(model.predict_proba(sample_passengers))
