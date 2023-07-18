def register_students():
    students = []  # Initialize an empty list to store student information
    num_students = int(input("Enter the number of students to register: "))

    for _ in range(num_students):
        print("\nStudent", len(students) + 1)
        age = int(input("Enter age: "))
        class_name = input("Enter class name: ")
        location = input("Enter location: ")
        payment_mode = input("Enter mode of payment: ")

        student = {
            "age": age,
            "class_name": class_name,
            "location": location,
            "payment_mode": payment_mode
        }

        students.append(student)  # Add the student to the list

    return students

# Example usage
registered_students = register_students()

# Print the registered students
for student in registered_students:
    print("\nStudent Details:")
    print("Age:", student["age"])
    print("Class Name:", student["class_name"])
    print("Location:", student["location"])
    print("Mode of Payment:", student["payment_mode"])
