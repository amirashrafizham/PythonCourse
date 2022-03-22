
toppings = ["pepperoni", "pineapple", "cheese",
            "saussage", "olives", "anchovies", "mushrooms"]

prices = [2, 6, 1, 3, 2, 7, 2]

num_two_dollar_slices = prices.count(2)

print(num_two_dollar_slices)

num_pizzas = len(toppings)


print(f'We sell {num_pizzas} different kinds of pizza!, where {num_pizzas} represents the value of our variable {num_pizzas}')


pizza_and_prices = [[2, "pepperoni"], [6, "pineapple"], [1, "cheese"], [
    3, "sausage"], [2, "olives"], [7, "anchovies"], [2, "mushrooms"]]


print(pizza_and_prices)

pizza_and_prices.sort()

print(pizza_and_prices)

cheapest_pizza = pizza_and_prices[0]

print(cheapest_pizza)

priciest_pizza = pizza_and_prices[-1]
print(priciest_pizza)
pizza_and_prices.remove(priciest_pizza)

pizza_and_prices.append([2.5, "peppers"])
pizza_and_prices.sort()

print(pizza_and_prices)

three_cheapes = pizza_and_prices[:3]
print(three_cheapes)
