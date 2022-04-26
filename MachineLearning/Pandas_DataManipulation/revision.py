import pandas as pd


df = pd.read_csv('imdb.csv')

genre = df['genre']

year_name = df[['year', 'name']]
year_2012 = df[(df.year == 2012) & (df.genre == 'action')]
print(year_2012.iloc[0:3])
