import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from teacher.add_teacher import add_teacher
from teacher.view_teacher import view_teachers
from teacher.update_teacher import update_teacher
from teacher.delete_teacher import delete_teacher


def teacher_management():

    while True:

        print("\n===== Teacher Management =====")
        print("1. Add Teacher")
        print("2. View Teachers")
        print("3. Update Teacher")
        print("4. Delete Teacher")
        print("5. Back")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_teacher()

        elif choice == "2":
            view_teachers()

        elif choice == "3":
            update_teacher()

        elif choice == "4":
            delete_teacher()

        elif choice == "5":
            print("Returning to Admin Dashboard...")
            break

        else:
            print("Invalid Choice!")


if __name__ == "__main__":
    teacher_management()