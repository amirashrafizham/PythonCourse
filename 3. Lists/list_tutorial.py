
first_names = ["Amir, Ashraf, Ahmad, Izham"]

preffered_size = ["Small", "Medium", "Large"]

# to append
preffered_size.append("Medium")
print(preffered_size)

# Multidimensional List (2-D example)
customer_data = [["Amir", "Small", True], [
    "Ashraf", "Large", False], ["Ahmad", "Medium", False]]
print(customer_data)


# Change Data Value in array (second element, last value)
customer_data[2][-1] = True
print(customer_data)


# Remove Data value in array (second element, an input)
customer_data[1].remove(False)
print(customer_data)

# Adding more array into multidimensional array
customer_data_final = customer_data + \
    [["Amit", "Large", True], ["Karim", "X-Large", False]]

print(customer_data_final)
