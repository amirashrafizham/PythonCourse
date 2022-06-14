from re import I
import pandas as pd


df = pd.read_csv('ad_clicks.csv')

print(df.head())

print(df.groupby('utm_source').user_id.count().reset_index())

df['is_click'] = df['ad_click_timestamp'].notna()

clicks_by_source = df.groupby(
    ['utm_source', 'is_click']).user_id.count().reset_index()

clicks_pivot = clicks_by_source.pivot(
    columns='is_click',
    index='utm_source',
    values='user_id').reset_index()

clicks_pivot['percent_clicked'] = (clicks_pivot[True] /
                                   (clicks_pivot[True] + clicks_pivot[False])) * 100


clicks_by_ads = df.groupby(
    ['experimental_group', 'is_click']).user_id.count().reset_index()

clicks_by_ads_pivot = clicks_by_ads.pivot(
    columns='is_click',
    index='experimental_group',
    values='user_id').reset_index()

clicks_a = df[df['experimental_group'] == 'A']
clicks_b = df[df['experimental_group'] == 'B']

clicks_by_day_a = clicks_a.groupby([
    'day', 'is_click']).user_id.count().reset_index()

clicks_by_day_a_pivot = clicks_by_day_a.pivot(
    columns='is_click',
    index='day',
    values='user_id').reset_index()

clicks_by_day_a_pivot['percent_clicked'] = (clicks_by_day_a_pivot[True] /
                                            (clicks_by_day_a_pivot[True] + clicks_by_day_a_pivot[False])) * 100

clicks_by_day_b = clicks_b.groupby([
    'day', 'is_click']).user_id.count().reset_index()

clicks_by_day_b_pivot = clicks_by_day_b.pivot(
    columns='is_click',
    index='day',
    values='user_id').reset_index()

clicks_by_day_b_pivot['percent_clicked'] = (clicks_by_day_b_pivot[True] /
                                            (clicks_by_day_b_pivot[True] + clicks_by_day_b_pivot[False])) * 100

print(clicks_by_day_a_pivot['percent_clicked'].mean())
print(clicks_by_day_b_pivot['percent_clicked'].mean())
