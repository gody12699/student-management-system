students = []

while True:
    print("\n1. Add Student")
    print("2. View Students")
    print("3. Delete Student")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        name = input("Enter student name: ")
        students.append(name)
        print("Student added successfully.")

    elif choice == "2":
        print("\nStudent List:")
        for student in students:
            print(student)

    elif choice == "3":
        name = input("Enter student name to delete: ")
        if name in students:
            students.remove(name)
            print("Student removed.")
        else:
            print("Student not found.")

    elif choice == "4":
        print("Exiting program.")
        break

    else:
        print("Invalid option.")
