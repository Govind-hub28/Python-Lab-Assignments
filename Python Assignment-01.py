# Python Assignment-01

# Student Data Management Using Python Collections

# List to store student records
students = []


def add_student():
    roll_number = int(input("Enter Roll Number: "))

    # Check for duplicate roll number
    for student in students:
        if student["roll_number"] == roll_number:
            print("Student with this Roll Number already exists.")
            return

    name = input("Enter Student Name: ")
    branch = input("Enter Branch: ")
    marks = float(input("Enter Marks: "))

    # Tuple containing student details
    details = (name, branch, marks)

    # Dictionary containing student record
    student = {
        "roll_number": roll_number,
        "details": details
    }

    # Add dictionary to list
    students.append(student)

    print("Student added successfully.")


def delete_student():
    roll_number = int(input("Enter Roll Number to delete: "))

    for student in students:
        if student["roll_number"] == roll_number:
            students.remove(student)
            print("Student deleted successfully.")
            return

    print("Student not found.")


def update_student():
    roll_number = int(input("Enter Roll Number to update: "))

    for student in students:
        if student["roll_number"] == roll_number:
            name = input("Enter New Name: ")
            branch = input("Enter New Branch: ")
            marks = float(input("Enter New Marks: "))

            student["details"] = (name, branch, marks)

            print("Student updated successfully.")
            return

    print("Student not found.")


def display_students():
    if not students:
        print("No student records available.")
        return

    print("\nStudent Records")
    print("-" * 50)

    for student in students:
        roll_number = student["roll_number"]
        name, branch, marks = student["details"]

        print("Roll Number:", roll_number)
        print("Name:", name)
        print("Branch:", branch)
        print("Marks:", marks)
        print("-" * 50)


# Main program
while True:
    print("\n===== Student Data Management =====")
    print("1. Add Student")
    print("2. Delete Student")
    print("3. Update Student")
    print("4. Display Students")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        delete_student()

    elif choice == "3":
        update_student()

    elif choice == "4":
        display_students()

    elif choice == "5":
        print("Program ended.")
        break

    else:
        print("Invalid choice. Please try again.")
