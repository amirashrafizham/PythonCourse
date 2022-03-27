import pandas as pd
import numpy as np


list1 = [1, 2, 3, 4]
array1 = np.array(list1)
print(array1)


list2 = [[1, 2, 3], [4, 5, 6]]
array2 = np.array(list2)
print(array2)

toyPrices = [5, 8, 3, 6]

# without numpy
for i in range(len(toyPrices)):
    toyPrices[i] = toyPrices[i] - 2
print("Without numpy")
print(toyPrices)

# with numpy
toyPrices = np.array([5, 8, 3, 6])
print("With numpy")
print(toyPrices-2)
