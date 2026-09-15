import numpy as np
import pandas as pd

# Dataset
marks = np.array([
    [85, 80, 90],
    [70, 75, 65],
    [92, 88, 95],
    [60, 72, 68],
    [78, 82, 80]
])

# 1. Total marks
total = np.sum(marks, axis=1)

# 2. Average marks of each student
average = np.mean(marks, axis=1)

# 3. Average marks of each subject
subject_average = np.mean(marks, axis=0)

# 4. Highest score in each subject
highest = np.max(marks, axis=0)

# 5. Lowest score in each subject
lowest = np.min(marks, axis=0)

# 6. Students with average above 80
above_80 = average > 80
print("Students above 80:", np.where(above_80)[0])

# 7. Pass/Fail using np.where()
status = np.where(average >= 50, "Pass", "Fail")

# 8. Highest-performing student
highest_student = np.argmax(average)
print("Highest-performing student index:", highest_student)

# 9. Standard deviation of each subject
std = np.std(marks, axis=0)

# Convert into DataFrame
df = pd.DataFrame({
    "Python": marks[:, 0],
    "SQL": marks[:, 1],
    "Machine Learning": marks[:, 2],
    "Total": total,
    "Average": average,
    "Status": status
})

print("\nStudent Performance:")
print(df)

print("\nSubject Average:")
print(subject_average)

print("\nHighest Score:")
print(highest)

print("\nLowest Score:")
print(lowest)

print("\nStandard Deviation:")
print(std)