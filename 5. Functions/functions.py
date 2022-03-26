def directions_to_timesSq():
    print("Walk 4 mins to 34th St Herald Square train station.")
    print("Take the Northbound N, Q, R, or W train 1 stop.")
    print("Get off the Times Square 42nd Street stop.")
    print("Take lots of pictures!")


def weather_check():
    print("Looks great outside! Enjoy your trip.")
    print("False Alarm, the weather changed! There is a thunderstorm approaching. Cancel your plans and stay inside.")


def generate_trip_instructions(location):
    print(f"Looks like you are planning a trip to visit {location}")
    print(f"You can use the public subway system to get to {location}")


def calculate_expenses(plane_ticket_price, car_rental_rate, hotel_rate, trip_time):
    car_rental_total = car_rental_rate * trip_time
    hotel_total = hotel_rate * trip_time - 10
    print(plane_ticket_price + car_rental_total + hotel_total)


calculate_expenses(200, 100, 100, 5)


def trip_planner(first_destination, second_destination, final_destination="Codecademy HQ"):
    print(
        f"Here is what your trip will look like! First, we will stop in {first_destination}, then {second_destination}, and lastly {final_destination}")


# Built in functions example
tshirt_price = 9.75
shorts_price = 15.50
mug_price = 5.99
poster_price = 2.00

price = [tshirt_price, shorts_price, mug_price, poster_price]

max_price = max(price)
min_price = min(price)
rounded_price = round(tshirt_price)

# Variable Access
favorite_locations = "Paris, Norway, Iceland"


def print_count_locations():
    print("There are 3 locations")


def show_favorite_locations():
    print("Your favorite locations are: " + favorite_locations)


print_count_locations()
show_favorite_locations()

# Returns

current_budget = 3500.75


def print_remaining_budget(budget):
    print("Your remaining budget is: $" + str(budget))


print_remaining_budget(current_budget)


def deduct_expense(budget, expense):
    return budget - expense


shirt_expense = 9

new_budget_after_shirt = deduct_expense(current_budget, shirt_expense)


# Multiple Returns
def top_tourist_locations_italy():
    first = "Rome"
    second = "Venice"
    third = "Florence"
    return first, second, third


most_popular1, most_popular2, most_popular3 = top_tourist_locations_italy()

print(most_popular1)
print(most_popular2)
print(most_popular3)
