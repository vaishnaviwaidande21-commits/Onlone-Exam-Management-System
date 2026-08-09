import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


from student.view_available_exam import view_available_exam
from student.start_exam import start_exam
from student.view_result import view_result
from student.ai_analysis import ai_analysis

from session.user_session import get_user, clear_user



def student_menu():

    while True:

        print("\n" + "=" * 45)
        print("          STUDENT DASHBOARD")
        print("=" * 45)
        print("1. View Available Exams")
        print("2. Start Exam")
        print("3. View Result")
        print("4. AI Performance Analysis")
        print("5. Logout")
        print("=" * 45)


        choice = input("Enter your choice: ")



        user = get_user()
        if not user or "id" not in user:
            print("\nPlease Login First! ")
            break


        if choice == "1":

            view_available_exam()



        elif choice == "2":

            student_id = user["id"]

            start_exam()



        elif choice == "3":

            student_id = user["id"]

            view_result(student_id)



        elif choice == "4":

            student_id = user["id"]

            ai_analysis(student_id)



        elif choice == "5":

            clear_user()

            print("\nLogout Successfully! ✅")
            break



        else:

            print("\nInvalid Choice!")




if __name__ == "__main__":

    student_menu()