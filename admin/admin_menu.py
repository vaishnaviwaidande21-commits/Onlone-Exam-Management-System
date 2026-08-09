import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from student.student_management import student_management
from teacher.teacher_management import teacher_management
from exam.exam_management import exam_management
from question.question_management import question_management


def admin_menu():

    while True:

        print("\n===== Admin Dashboard =====")
        print("1. Manage Students")
        print("2. Manage Teachers")
        print("3. Manage Exams")
        print("4. Manage Questions")
        print("5. View Reports")
        print("6. Logout")

        choice = input("Enter your choice: ")

        if choice == "1":
            student_management()

        elif choice == "2":
            teacher_management()

        elif choice == "3":
            exam_management()

        elif choice == "4":
            question_management()

        elif choice == "5":
            print("Reports Module Coming Soon")

        elif choice == "6":
            print("Logout Successfully!")
            break

        else:
            print("Invalid Choice!")


if __name__ == "__main__":
    admin_menu()