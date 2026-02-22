from database import *

def menu():
    print("\n===== Student Management System =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

def main():
    create_table()

    while True:
        menu()
        choice = input("Enter choice: ")

        if choice == "1":
            name = input("Name: ")
            age = input("Age: ")
            course = input("Course: ")
            email = input("Email: ")

            add_student(name, age, course, email)
            print("Student added successfully!")

        elif choice == "2":
            students = get_students()
            print("\n--- Student List ---")
            for student in students:
                print(student)

        elif choice == "3":
            name = input("Enter name to search: ")
            students = search_student(name)
            for student in students:
                print(student)

        elif choice == "4":
            id = input("Enter student ID: ")
            name = input("New name: ")
            age = input("New age: ")
            course = input("New course: ")
            email = input("New email: ")

            update_student(id, name, age, course, email)
            print("Student updated successfully!")

        elif choice == "5":
            id = input("Enter student ID to delete: ")
            delete_student(id)
            print("Student deleted successfully!")

        elif choice == "6":
            print("Thank you!")
            break

        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()