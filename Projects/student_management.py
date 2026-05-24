import json
import os

FILE_NAME = "students.json"


#---------------- FILE HANDLING ---------------- 

def load_students():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)

    except (FileNotFoundError, json.JSONDecodeError):
        return []


def save_students(students):
    with open(FILE_NAME, "w") as file:
        json.dump(students, file, indent=4)


# ---------------- CORE FUNCTIONS ---------------- #

def add_student(students):

    name = input("Enter student name: ")

    try:
        age = int(input("Enter age: "))
        marks = float(input("Enter marks: "))
    except ValueError:
        print("Invalid input!")
        return

    student = {
        "name": name,
        "age": age,
        "marks": marks
    }

    students.append(student)

    save_students(students)

    print("Student added successfully!\n")


def view_students(students):

    if not students:
        print("No students found.\n")
        return

    print("\n--- STUDENT LIST ---")

    for index, student in enumerate(students, start=1):

        print(f"""
Student {index}
Name  : {student['name']}
Age   : {student['age']}
Marks : {student['marks']}
""")



def search_student(students):

    keyword = input("Enter student name to search: ").lower()

    found = False

    for student in students:

        if keyword in student["name"].lower():

            print("\nStudent Found!")
            print(student)

            found = True

    if not found:
        print("Student not found.\n")


def delete_student(students):

    name = input("Enter student name to delete: ")

    for student in students:

        if student["name"].lower() == name.lower():

            students.remove(student)

            save_students(students)

            print("Student deleted successfully!\n")
            return

    print("Student not found.\n")


def update_student(students):

    name = input("Enter student name to update: ")

    for student in students:

        if student["name"].lower() == name.lower():

            print("\nLeave blank if you don't want to change.")

            new_name = input("New name: ")
            new_age = input("New age: ")
            new_marks = input("New marks: ")

            if new_name:
                student["name"] = new_name

            if new_age:
                student["age"] = int(new_age)

            if new_marks:
                student["marks"] = float(new_marks)

            save_students(students)

            print("Student updated successfully!\n")
            return

    print("Student not found.\n")


def show_topper(students):

    if not students:
        print("No students available.\n")
        return

    topper = max(students, key=lambda student: student["marks"])

    print("\n--- TOPPER ---")
    print(f"Name  : {topper['name']}")
    print(f"Marks : {topper['marks']}\n")


# ---------------- MAIN PROGRAM ---------------- #

def main():

    students = load_students()

    while True:

        print("""
====== STUDENT MANAGEMENT SYSTEM ======

1. Add Student
2. View Students
3. Search Student
4. Update Student
5. Delete Student
6. Show Topper
7. Exit

======================================
""")

        choice = input("Enter your choice: ")

        match choice:

            case "1":
                add_student(students)

            case "2":
                view_students(students)

            case "3":
                search_student(students)

            case "4":
                update_student(students)

            case "5":
                delete_student(students)

            case "6":
                show_topper(students)

            case "7":
                print("Thank you for using the system!")
                break

            case _:
                print("Invalid choice!\n")


# ---------------- START PROGRAM ---------------- #

main()