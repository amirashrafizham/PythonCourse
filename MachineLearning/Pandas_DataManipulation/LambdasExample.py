
from site import addsitedir


def add_two(input): return input + 2


def add_str(input): return f"my name is {input}"


def check_grade(
    input): return "Grade is distinction" if input >= 70 else "Not a distinction grade"


print(add_two(3))

print(add_str("amir"))

print(check_grade(30))
