import pandas as pd

# Load CSV file
df = pd.read_csv('student.csv')
# Show first 5 rows
print(df.head())

# Total Marks
df['Total'] = df['Maths'] + df['Science'] + df['English']

# Average Marks
df['average'] = df['Total'] / 3

# Topper of the class
topper = df[df['average'] == df['average'].max()]
print("Topper of the class:")
print(topper)

# Lowest Marks
lowest_marks = df[df['average'] == df['average'].min()]
print("Lowest marks in the class:")
print(lowest_marks)

# Subject Averages
maths_average = sum(df['Maths']) / 20
science_average = sum(df['Science']) / 20
english_average = sum(df['English']) / 20

print("Average of Maths:", maths_average)
print("Average of Science:", science_average)
print("Average of English:", english_average)

# Overall Class Average
avg_sum = sum(df['average']) / 20
print("Overall class average:", avg_sum)

# Grades
grades = []

for avg in df['average']:
    if avg >= 90:
        grades.append('A')
    elif avg >= 80:
        grades.append('B')
    elif avg >= 70:
        grades.append('C')
    elif avg >= 60:
        grades.append('D')
    else:
        grades.append('F')

df['Grades'] = grades

# Count Grades
a_sum = b_sum = c_sum = d_sum = f_sum = 0

for grade in df['Grades']:
    if grade == 'A':
        a_sum += 1
    elif grade == 'B':
        b_sum += 1
    elif grade == 'C':
        c_sum += 1
    elif grade == 'D':
        d_sum += 1
    else:
        f_sum += 1

print("Number of students with grade A:", a_sum)
print("Number of students with grade B:", b_sum)
print("Number of students with grade C:", c_sum)
print("Number of students with grade D:", d_sum)
print("Number of students with grade F:", f_sum)

# Bar Chart - Total Marks
import matplotlib.pyplot as plt

plt.figure(figsize=(10,5))
plt.bar(df['Name'], df['Total'])
plt.xlabel('Name of Students')
plt.ylabel('Total Marks')
plt.title('Class Performance Analysis')
plt.show()

# Subject Average Chart
subjects = ['Maths', 'Science', 'English']
averages = [maths_average, science_average, english_average]

plt.figure(figsize=(6,4))
plt.bar(subjects, averages)
plt.xlabel('Subjects')
plt.ylabel('Average Marks')
plt.title('Subject-wise Average Marks')
plt.show()

# Grade Distribution Pie Chart
grades = ['A', 'B', 'C', 'D', 'F']
counts = [a_sum, b_sum, c_sum, d_sum, f_sum]

plt.figure(figsize=(6,6))
plt.pie(counts, labels=grades, autopct='%1.1f%%')
plt.title('Grade Distribution')
plt.show()

# Students Above Overall Average
above_avg = df[df['average'] > avg_sum]

print("Students above overall class average:")
print(above_avg[['Name', 'average']])

# Students Below Overall Average
below_avg = df[df['average'] < avg_sum]

print("Students below overall class average:")
print(below_avg[['Name', 'average']])

# Topper vs Lowest Performer
students = [topper['Name'].values[0], lowest_marks['Name'].values[0]]
averages = [topper['average'].values[0], lowest_marks['average'].values[0]]

plt.figure(figsize=(5,4))
plt.bar(students, averages)
plt.xlabel('Students')
plt.ylabel('Average Marks')
plt.title('Topper vs Lowest Performer')
plt.show()