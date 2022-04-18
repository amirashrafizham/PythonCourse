medical_costs = {}


# Adding values into a Dictionary
medical_costs["Marina"] = 6607.0
medical_costs["Vinay"] = 3225.0
medical_costs.update({"Connie": 886.0, "Isaac": 16444.0, "Valentina": 6420.0})
print(medical_costs)


# Iterating the value in a Dictionary
total_cost = 0
for i in medical_costs.values():
    total_cost += i

# Getting the len of a Dictionary
average_cost = total_cost/len(medical_costs)
print(f"Average Insurance Cost: {average_cost}")

# Combine 2 Lists into a Dictionary using Zip
names = ["Marina", "Vinay", "Connie", "Isaac", "Valentina"]
ages = [27, 24, 43, 35, 52]

zipped_ages = dict(zip(names, ages))
print(zipped_ages)


# Getting a single value from key
marina_age = zipped_ages.get("Marina")
print(f"Marina's age is {marina_age}")


# Creating multiple values for a single key
medical_records = {}

medical_records["Marina"] = {"Age": 27, "Sex": "Female", "BMI": 31.1,
                             "Children": 2, "Smoker": "Non-smoker", "Insurance_cost": 6607.0}

medical_records["Vinay"] = {"Age": 24, "Sex": "Male", "BMI": 26.9,
                            "Children": 0, "Smoker": "Non-smoker", "Insurance_cost": 3225.0}

medical_records["Connie"] = {"Age": 43, "Sex": "Female", "BMI": 25.3,
                             "Children": 3, "Smoker": "Non-smoker", "Insurance_cost": 8886.0}

medical_records["Isaac"] = {"Age": 35, "Sex": "Male", "BMI": 20.6,
                            "Children": 4, "Smoker": "Smoker", "Insurance_cost": 16444.0}

medical_records["Valentina"] = {"Age": 52, "Sex": "Female", "BMI": 18.7,
                                "Children": 1, "Smoker": "Non-smoker", "Insurance_cost": 6420.0}

# How to access specific value in a Dictionary
print(
    f"Connie's insurance cost is {medical_records['Connie']['Insurance_cost']}")


# How to remove a key in a Dictionary
medical_records.pop("Vinay")

# How to access multiple values at one
# option1
""" for key in medical_records:
    print(
        f"{key} is a {medical_records[key]['Age']} year old {medical_records[key]['Sex']} {medical_records[key]['Smoker']} with a BMI of {medical_records[key]['BMI']} and insurance cost of {medical_records[key]['Insurance_cost']}") """

for key, value in medical_records.items():
    message = f"{key} is a {value['Age']} year old {value['Sex']} {value['Smoker']} with a BMI of {value['BMI']} and insurance cost of {value['Insurance_cost']}"
    print(message)
