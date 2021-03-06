class Patient:
    def __init__(self, name, age, sex, bmi, num_of_children, smoker):
        self.name = name
        self.age = age
        # add more parameters here
        self.sex = sex
        self.bmi = bmi
        self.num_of_children = num_of_children
        self.smoker = smoker

    def estimated_insurance_cost(self):
        estimated_cost = 250*self.age - 128*self.sex + 370*self.bmi + \
            425*self.num_of_children + 24000*self.smoker - 12500
        print(f"{self.name}'s estimated insurance costs is {estimated_cost} dollars.")

    def update_age(self, new_age):
        self.age = new_age
        print(f"{self.name} is now {self.age} years old")
        self.estimated_insurance_cost()

    def update_num_children(self, new_num_of_children):
        self.num_of_children = new_num_of_children
        print(f"{self.name} has {new_num_of_children} children.")
        self.estimated_insurance_cost()

    def patient_profile(self):
        patient_information = {"Name": self.name, "Age": self.age, "Sex": self.sex,
                               "BMI": self.bmi, "Children": self.num_of_children, "Smoker": self.smoker}
        print(patient_information)


patient1 = Patient("John Doe", 25, 1, 22.2, 0, 0)
patient1.estimated_insurance_cost()

patient1.update_age(32)
patient1.update_num_children(3)
patient1.patient_profile()
