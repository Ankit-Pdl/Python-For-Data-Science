# Function to calculate grade
def calculate_grade(mark):
    if mark >= 90:
        return "A+"
    elif mark >= 80:
        return "A"
    elif mark >= 70:
        return "B"
    elif mark >= 60:
        return "C"
    elif mark >= 50:
        return "D"
    else:
        return "Fail"


# List to store student records
students = []

# Adding students (tuple)
students.append(("Ankit", 85))
students.append(("Ram", 72))
students.append(("Sita", 45))
students.append(("Hari", 91))


# Display results
print("===== Student Report =====")

for student in students:
    name = student[0]
    mark = student[1]

    grade = calculate_grade(mark)

    # Conditional for pass/fail
    if mark >= 50:
        status = "Pass"
    else:
        status = "Fail"

    print(f"Name: {name}")
    print(f"Marks: {mark}")
    print(f"Grade: {grade}")
    print(f"Status: {status}")
    print("----------------------")