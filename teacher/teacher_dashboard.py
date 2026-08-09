import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


from teacher.view_teacher import view_teacher_exam

from question.add_question import add_question
from question.view_question import view_questions
from question.update_question import update_question
from question.delete_question import delete_question



def teacher_dashboard():

    while True:

        print("\n" + "="*45)
        print("          TEACHER DASHBOARD")
        print("="*45)

        print("1. View Assigned Exams")
        print("2. Manage Questions")
        print("3. View Student Results")
        print("4. Logout")

        print("="*45)


        choice = input("Enter your choice: ")



        if choice == "1":

            teacher_id = input("Enter Teacher ID: ")

            view_teacher_exam(teacher_id)



        elif choice == "2":

            while True:

                print("\n===== Manage Questions =====")
                print("1. Add Question")
                print("2. View Questions")
                print("3. Update Question")
                print("4. Delete Question")
                print("5. Back")


                q_choice = input("Enter your choice: ")



                if q_choice == "1":

                    add_question()



                elif q_choice == "2":

                    view_questions()



                elif q_choice == "3":

                    update_question()



                elif q_choice == "4":

                    delete_question()



                elif q_choice == "5":

                    break



                else:

                    print("Invalid Choice!")




        elif choice == "3":

            print("\nStudent Result Report Coming Soon...")



        elif choice == "4":

            print("\nLogout Successfully!")
            break



        else:

            print("\nInvalid Choice!")




if __name__ == "__main__":

    teacher_dashboard()