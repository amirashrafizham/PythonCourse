import numpy as np
import pandas as pd

# List
data = [50, 50, 47, 97, 49, 3, 53, 42, 26, 74, 82,
        62, 37, 15, 70, 27, 36, 35, 48, 52, 63, 64]

# Numpy Array
grades = np.array(data)

# To multiply all elements by 2
grades = grades*2

# The find the mean of grades array
mean = np.mean(grades)
print(mean)

# Creating a 2-D array
# Define an array of study hours
study_hours = [10.0, 11.5, 9.0, 16.0, 9.25, 1.0, 11.5, 9.0, 8.5, 14.5, 15.5,
               13.75, 9.0, 8.0, 15.5, 8.0, 9.0, 6.0, 10.0, 12.0, 12.5, 12.0]

# Create a 2D array (an array of arrays)
student_data = np.array([study_hours, grades])

# Accessing the array
student_data[0]  # will access study_hours sub-array
student_data[1]  # will access grades sub-array
student_data[0][0]  # will access first element in the study_hours sub-array
student_data[1][0]  # will access first element in the grades sub-array


# Calculating the mean of sub-array

# Calculating the mean for study_hours sub-array
# Calculates the mean for study_hours
mean_study_hours = np.mean(student_data[0])

# Calculates the mean for grades
mean_grades = np.mean(student_data[1])


# Pandas Tutorial
df_students = pd.DataFrame({'Name': ['Dan', 'Joann', 'Pedro', 'Rosie', 'Ethan', 'Vicky', 'Frederic', 'Jimmie',
                                     'Rhonda', 'Giovanni', 'Francesca', 'Rajab', 'Naiyana', 'Kian', 'Jenny',
                                     'Jakeem', 'Helena', 'Ismat', 'Anila', 'Skye', 'Daniel', 'Aisha'],
                            "StudyHours": student_data[0],
                            "Grade": student_data[1]})


# Filter data with loc
print(df_students.loc[5])  # filters at index number 5
print(df_students.loc[0:5])  # filters using range, start<->end
print(df_students.iloc[0:5])  # filters using range, start<->end-1

# Finds all associated values in a column
print(df_students[df_students.Name == 'Aisha'])

# Reads from a csv file
url = "https://raw.githubusercontent.com/MicrosoftDocs/mslearn-introduction-to-machine-learning/main/Data/ml-basics/grades.csv"
df_students = pd.read_csv(url, delimiter=',', header='infer')
print(df_students.head())


# Calculate the mean from a column
grade_mean = df_students.Grade.mean()
print(grade_mean)

# Filter using operations
grade_above_mean = df_students[df_students.Grade > grade_mean]
print(grade_above_mean)
