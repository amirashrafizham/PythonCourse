import pandas as pd
from pyparsing import col

df = pd.read_csv('imdb.csv')

# Rename columns here

df.rename(columns={'name': 'movie_title'}, inplace=True)

print(df.head())
