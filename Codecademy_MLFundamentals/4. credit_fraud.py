import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Load the data
transactions = pd.read_csv('transactions.csv')
print(transactions.head())

# Summary statistics on amount column
print(transactions['amount'].describe())

# Create isPayment field


# Create isMovement field


# Create accountDiff field


# Create features and label variables


# Split dataset


# Normalize the features variables


# Fit the model to the training data


# Score the model on the training data


# Score the model on the test data


# Print the model coefficients


# New transaction data
transaction1 = np.array([123456.78, 0.0, 1.0, 54670.1])
transaction2 = np.array([98765.43, 1.0, 0.0, 8524.75])
transaction3 = np.array([543678.31, 1.0, 0.0, 510025.5])

# Create a new transaction


# Combine new transactions into a single array


# Normalize the new transactions


# Predict fraud on the new transactions


# Show probabilities on the new transactions
