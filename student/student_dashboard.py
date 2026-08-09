import sys
import os

sys.path.append(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
)


from student.view_available_exam import view_available_exam
from student.start_exam import start_exam
from student.view_result import view_result
from student.ai_analysis import ai_analysis

from session.user_session import get_user




def student_dashboard():


    while True:


        print("\n=============================================")
        print("          STUDENT DASHBOARD")
        print("=============================================")


        print("1. View Available Exams")
        print("2. Start Exam")
        print("3. View Result")
        print("4. AI Performance Analysis")
        print("5. Logout")


        print("=============================================")



        choice = input("Enter your choice: ")



        # Current Logged Student

        user = get_user()

        student_id = user.get("id")



        if choice == "1":


            view_available_exam()



        elif choice == "2":


            start_exam()



        elif choice == "3":


            if student_id:

                view_result(student_id)

            else:

                print("Student Session Not Found ❌")



        elif choice == "4":


            if student_id:

                ai_analysis(student_id)

            else:

                print("Student Session Not Found ❌")



        elif choice == "5":


            from session.user_session import clear_user

            clear_user()

            print("\nLogout Successfully!")

            break



        else:


            print("\nInvalid Choice!")




if __name__ == "__main__":

    student_dashboard()