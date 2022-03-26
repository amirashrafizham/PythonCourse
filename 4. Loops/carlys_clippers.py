# name of the cuts offered
from ast import While


hairstyles = ["bouffant", "pixie", "dreadlocks",
              "crew", "bowl", "bob", "mohawk", "flattop"]

# price of each haristyle
prices = [30, 25, 40, 20, 20, 35, 50, 35]

# number of purchases for each hairstyle last week
last_week = [2, 3, 5, 8, 4, 4, 6, 2]

total_price = 0
for i in prices:
    total_price += i

print(total_price)

average_price = total_price/len(prices)
print(f"Average Haircut Price: {average_price}")

new_prices = [price - 5 for price in prices]
print(new_prices)

total_revenue = 0
length_array = len(prices)
i = 0
while i < length_array:
    revenue = prices[i] * last_week[i]
    total_revenue += revenue
    i += 1

print(f"Total revenue: {total_revenue}")
average_daily_revenue = total_revenue/length_array
print(average_daily_revenue)

cuts_under_30 = [hairstyles[new_prices.index(i)] for i in new_prices if i < 30]

print(cuts_under_30)
