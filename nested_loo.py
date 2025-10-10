python_students = [
    ["Harry", 37.21],
    ["Berry", 37.21],
    ["Tina", 37.2],
    ["Akriti", 41],
    ["Harsh", 39]
]

# Extracting all marks
marks = [student[1] for student in python_students]

# Finding the second lowest mark
unique_marks = sorted(set(marks))
second_lowest = unique_marks[1]

# Getting names of students who have that mark
names = [student[0] for student in python_students if student[1] == second_lowest]

# Printing names in alphabetical order
for name in sorted(names):
    print(name)
