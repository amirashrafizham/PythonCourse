# Write your function here

def add_greetings(names):
    list = []
    for i in names:
        string = (f'Hello, {i}')
        list.append(string)
    return list


# Uncomment the line below when your function is done
print(add_greetings(["Owen", "Max", "Sophie"]))
