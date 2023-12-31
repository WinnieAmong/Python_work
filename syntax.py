def register_students():
    students = []  # Initialize an empty list to store student information
    num_students = int(input("Enter the number of students to register: "))

    for _ in range(num_students):
        print("\nStudent", len(students) + 1)
        age = int(input("Enter age: "))
        class_name = input("Enter class name: ")
        location = input("Enter location: ")
        parent_name = input("Enter parent's name: ")

        # Perform conditional checks using if and else statements
        if age < 3:
            print("Student must be at least 3 years old to register.")
            continue  # Skip the current iteration and move to the next student

        if location == "":
            print("Please enter a valid location.")
            continue

        if class_name == "":
            print("Please enter a valid class name.")
            continue

        if parent_name == "":
            print("Please enter a valid parent's name.")
            continue

        student = {
            "age": age,
            "class_name": class_name,
            "location": location,
            "parent_name": parent_name
        }

        students.append(student)  # Add the student to the list

    return students

# Example usage
register_students()

# Print the registered students
for student in registered_students:
    print("\nStudent Details:")
    print("Age:", student["age"])
    print("Class Name:", student["class_name"])
    print("Location:", student["location"])
    print("Parent's Name:", student["parent_name"])
