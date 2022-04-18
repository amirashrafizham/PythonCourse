names = ["Mohamed", "Sara", "Xia", "Paul", "Valentina",
         "Jide", "Aaron", "Emily", "Nikita", "Paul"]
insurance_costs = [13262.0, 4816.0, 6839.0, 5054.0,
                   14724.0, 5360.0, 7640.0, 6072.0, 2750.0, 12064.0]

# Add your code here


def get_insurance(lst):
    return lst[1]  # gets the second element, we will sort it in the list


names.append("Priscilla")
insurance_costs.append(8320.0)

medical_records = list(zip(names, insurance_costs))

num_medical_records = len(medical_records)
print(f"There are {num_medical_records} medical records.")

first_medical_record = medical_records[0]
print(f"Here is the first medical record: {first_medical_record}")

medical_records.sort(key=get_insurance)
print(
    f"Here are the medical records sorted by insurance costs: {medical_records}")

cheapest_three = medical_records[0:3]
print(
    f"Here are the three cheapest insurance costs in our medical records: {cheapest_three}")

priciest_three = medical_records[-3:]
print(
    f"Here are the three most expensive insurance cossts in our medical records: {priciest_three}")
