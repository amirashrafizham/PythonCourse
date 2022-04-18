nested_lists = [[4, 8], [16, 15], [23, 42]]


first_only = [item1 for (item1, item2) in nested_lists]

print(first_only)
