import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv('titanic.csv')

mean_fare = df.groupby('Survived').Fare.mean().reset_index()

died = df[df['Survived'] == 0]['Fare']
survived = df[df['Survived'] == 1]['Fare']

sns.boxplot(data=df, x='Survived', y='Fare')
plt.show()
plt.close()


plt.hist(died, color="red", label="Died", density=True, alpha=0.5)
plt.hist(survived, color="blue", label="Survived", density=True, alpha=0.5)
plt.legend()
plt.show()
