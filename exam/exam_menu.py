import sys
import os

sys.path.append(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
)


from exam.create_exam import create_exam
from exam.view_exam import view_exam
from exam.update_exam import update_exam
from exam.delete_exam import delete_exam
from exam.assign_questions import assign_questions
from exam.start_exam import start_exam



def exam_menu():

    while True:

        print("\n" + "=" * 50)
        print("             EXAM MANAGEMENT")
        print("=" * 50)

        print("1. Create Exam")
        print("2. View Exams")
        print("3. Update Exam")
        print("4. Delete Exam")
        print("5. Assign Questions")
        print("6. Start Exam")
        print("7. Back")

        print("=" * 50)


        choice = input("Enter your choice: ")



        if choice == "1":

            create_exam()



        elif choice == "2":

            view_exam()



        elif choice == "3":

            update_exam()



        elif choice == "4":

            delete_exam()



        elif choice == "5":

            assign_questions()



        elif choice == "6":

            start_exam()



        elif choice == "7":

            print("\nReturning...")
            break



        else:

            print("\nInvalid Choice!")



if __name__ == "__main__":

    exam_menu()