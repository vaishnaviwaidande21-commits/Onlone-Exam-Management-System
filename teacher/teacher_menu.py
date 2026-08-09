import sys
import os

sys.path.append(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
)

from session.user_session import get_user, clear_user



def teacher_menu():

    user = get_user()

    if not user or "id" not in user:

        print("\nPlease Login First! ❌")
        return



    while True:


        print("\n" + "=" * 50)
        print("             TEACHER DASHBOARD")
        print("=" * 50)

        print("1. Create Exam")
        print("2. View Exams")
        print("3. Generate Questions Using AI 🤖")
        print("4. Manage Exams")
        print("5. View Student Results")
        print("6. Logout")

        print("=" * 50)



        choice = input("Enter your choice: ")




        if choice == "1":


            from exam.create_exam import create_exam

            create_exam()





        elif choice == "2":


            from exam.view_exam import view_exam

            view_exam()





        elif choice == "3":


            from question.smart_question_generator import (
                create_questions,
                display_questions
            )


            print("\n" + "=" * 50)
            print("        AI QUESTION GENERATOR 🤖")
            print("=" * 50)



            subject = input("\nEnter Subject: ")



            print("\nSelect Question Type")
            print("1. MCQ")
            print("2. True / False")
            print("3. Fill in the Blanks")


            type_choice = input("\nEnter Question Type: ")




            if type_choice == "1":

                question_type = "MCQ"



            elif type_choice == "2":

                question_type = "True/False"



            elif type_choice == "3":

                question_type = "Fill in the Blanks"



            else:

                print("\nInvalid Question Type!")
                continue





            difficulty = input(
                "\nEnter Difficulty (Easy/Medium/Hard): "
            )



            number = int(
                input("Enter Number of Questions: ")
            )





            questions = create_questions(
                subject,
                difficulty,
                number,
                question_type
            )



            display_questions(questions)







        elif choice == "4":


            from exam.exam_management import exam_management

            exam_management()





        elif choice == "5":


            print("\nStudent Result Module Coming Soon")






        elif choice == "6":


            clear_user()

            print("\nTeacher Logout Successfully! ✅")

            break





        else:

            print("\nInvalid Choice!")




if __name__ == "__main__":

    teacher_menu()