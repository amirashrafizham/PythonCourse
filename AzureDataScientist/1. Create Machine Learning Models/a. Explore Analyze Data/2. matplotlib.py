from tarfile import HeaderError
import pandas as pd
from matplotlib import pyplot as plt

url = "https://raw.githubusercontent.com/MicrosoftDocs/mslearn-introduction-to-machine-learning/main/Data/ml-basics/grades.csv"

# Reads data from a CSV
df_students = pd.read_csv(url, delimiter=',', header='infer')
print(len(df_students['Grade']))

# Removes any row with missing data
df_students = df_students.dropna(axis=0, how='any')
print(len(df_students['Grade']))

# Calculates students who passed, where passing grade is 60
passes = df_students[df_students['Grade'] >= 60]
print(len(passes['Grade']))

# Sets up matplotlib bar chart
plt.bar(x=passes['Name'], height=passes['Grade'])
plt.title("Students vs Grade chart")
plt.xlabel("Student's Name")
plt.ylabel("Grade")

plt.show()
