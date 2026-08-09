import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from student.add_student import add_student
from student.view_student import view_students
from student.update_student import update_student
from student.delete_student import delete_student


def student_management():

    while True:
        print("\n===== Student Management =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Back")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()

        elif choice == "2":
            view_students()

        elif choice == "3":
            update_student()

        elif choice == "4":
            delete_student()

        elif choice == "5":
            print("Returning to Admin Dashboard...")
            break

        else:
            print("Invalid Choice! Please Try Again.")


if __name__ == "__main__":
    student_management()