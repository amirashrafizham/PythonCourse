import pandas as pd
import numpy as np

diabetes_data = pd.read_csv('diabetes.csv')

print(diabetes_data.dtypes)
""" 
Pregnancies                 0
Glucose                     0
BloodPressure               0
SkinThickness               0
Insulin                     0
BMI                         0
DiabetesPedigreeFunction    0
Age                         0
Outcome                     0 
"""

print(diabetes_data.isnull().sum())


diabetes_data[['Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI']] = diabetes_data[[
    'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI']].replace(0, np.NaN)

print(diabetes_data.isnull().sum())
print(diabetes_data[diabetes_data.isnull().any(axis=1)])


print(diabetes_data['Outcome'].unique())
