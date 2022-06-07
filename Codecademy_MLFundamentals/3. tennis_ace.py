import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Load Data
df = pd.read_csv('tennis_stats.csv')

# Check Data Types
print(df.dtypes)

""" 
Player                         object
Year                            int64
FirstServe                    float64
FirstServePointsWon           float64
FirstServeReturnPointsWon     float64
SecondServePointsWon          float64
SecondServeReturnPointsWon    float64
Aces                            int64
BreakPointsConverted          float64
BreakPointsFaced                int64
BreakPointsOpportunities        int64
BreakPointsSaved              float64
DoubleFaults                    int64
ReturnGamesPlayed               int64
ReturnGamesWon                float64
ReturnPointsWon               float64
ServiceGamesPlayed              int64
ServiceGamesWon               float64
TotalPointsWon                float64
TotalServicePointsWon         float64
Wins                            int64
Losses                          int64
Winnings                        int64
Ranking                         int64
 """

numeric_features = ["FirstServe", "FirstServePointsWon",
                    "FirstServeReturnPointsWon", "SecondServePointsWon", "SecondServeReturnPointsWon", "Aces", "BreakPointsConverted", "BreakPointsFaced", "BreakPointsOpportunities", "BreakPointsSaved", "DoubleFaults", "ReturnGamesPlayed", "ReturnGamesWon", "ReturnPointsWon", "ServiceGamesPlayed", "ServiceGamesWon", "TotalPointsWon", "TotalServicePointsWon"]


# Finding correlations, method 1

def numeric_label_alternative():
    for col in numeric_features:
        fig = plt.figure(figsize=(9, 6))
        ax = fig.gca()
        feature = df[col]
        label = df['Wins']
        correlation = feature.corr(label)
        plt.scatter(x=feature, y=label)
        plt.xlabel(col)
        plt.ylabel('Wins')
        ax.set_title('Wins vs ' + col +
                     '- correlation: ' + str(correlation))
        print(f"{col} vs wins correlation: {round(correlation,2)}")
    plt.show()

# numeric_label_alternative()
# strong correlations for : Aces, BreakPointsFaced, ServiceGamesPlayed, BreakPointsOpportunities, DoubleFaults, ReturnGamesPlayed. However, ServiceGamesPlayed and ReturnGamesPlayed don't determine anything during a player's winning match

# Finding correlations, method 2


tennis_correlation = df.corr()
tennis_correlation = tennis_correlation[[
    'Winnings']].reset_index()
tennis_correlation.rename(columns={'index': 'Feature'}, inplace=True)
tennis_correlation = tennis_correlation[
    (tennis_correlation.Feature != 'Wins')
    & (tennis_correlation.Feature != 'Losses')
    & (tennis_correlation.Feature != 'Winnings')
    & (tennis_correlation.Feature != 'ServiceGamesPlayed')
    & (tennis_correlation.Feature != 'ReturnGamesPlayed')
    & (tennis_correlation.Feature != 'Ranking')]
tennis_correlation = tennis_correlation.sort_values(
    ['Winnings'], ascending=False)

print(tennis_correlation)

# Thus, BreakPointsOpportunities, BreakPointsFaced, DoubleFaults, Aces are good labels to predict a player's winning probability

# Build Model
X, y = df[['BreakPointsOpportunities', 'BreakPointsFaced',
           'DoubleFaults', 'Aces']].values, df['Winnings'].values

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.30, random_state=0)

print('Training Set: %d rows\nTest Set: %d rows' %
      (X_train.shape[0], X_test.shape[0]))

model = LinearRegression().fit(X_train, y_train)

y_predictions = model.predict(X_test)

# Assess Model Accuracy
mse = mean_squared_error(y_test, y_predictions)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_predictions)

# Print accuracy
print(f"RMSE: {rmse:.2f}; R-squared: {r2:.2f}")
