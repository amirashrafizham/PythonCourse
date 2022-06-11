import numpy as np
import pandas as pd


orders = pd.read_csv('orders.csv')

print(orders.head(10))

most_expensive = orders['price'].max()
print(most_expensive)

num_colors = orders['shoe_color'].nunique()
print(num_colors)


pricey_shoes = orders.groupby('shoe_type').price.max().reset_index()
print(pricey_shoes)

cheap_shoes = orders.groupby('shoe_color').price.apply(
    lambda x: np.percentile(x, 25)).reset_index()

shoe_counts = orders.groupby(
    ['shoe_color', 'shoe_type']).id.count().reset_index()


shoe_counts_pivot = shoe_counts.pivot(
    columns='shoe_color',
    index='shoe_type',
    values='id').reset_index()

print(shoe_counts_pivot)
