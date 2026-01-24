students = []

def add_student():
    name = input("Enter student name: ")
    students.append(name)
    print("Student added successfully!")

def view_students():
    if not students:
        print("No students found.")
    else:
        for i, s in enumerate(students, 1):
            print(i, s)

while True:
    print("\n1. Add Student")
    print("2. View Students")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid choice")