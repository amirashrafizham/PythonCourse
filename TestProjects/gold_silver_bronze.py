import math

bronze = 1
silver = 5
gold = 10

num = int(input("Enter an amount: "))

gold_count = num // gold
num = math.floor(num % gold)

silver_count = num // silver
num = math.floor(num % silver)

bronze_count = num // bronze

print(f"number of gold coins: {gold_count}")
print(f"number of silver coins: {silver_count}")
print(f"number of bronze coins: {bronze_count}")
