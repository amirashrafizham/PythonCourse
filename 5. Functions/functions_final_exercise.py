
def trip_planner_welcome(name):
    print(f"Welcome to tripplanner v1.0 {name}")


trip_planner_welcome("amir")


def estimated_time_rounded(num):
    rounded_time = round(num)
    return rounded_time


estimate = estimated_time_rounded(2.6)
print(estimate)


def destination_setup(origin, destination, estimated_time, mode_of_transport="Car"):
    print(f"Your trip starts off in {origin}")
    print(f"And you are traveling to {destination}")
    print(f"You will be traveling by {mode_of_transport}")
    print(f"It will take approximately {estimated_time} hours")


destination_setup("kuala lumpur", "manchester", 12, "plane")
