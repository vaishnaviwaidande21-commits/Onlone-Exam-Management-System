import sys
import os

sys.path.append(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
)


from exam.add_exam import add_exam
from exam.view_exam import view_exam
from exam.update_exam import update_exam
from exam.delete_exam import delete_exam



def exam_management():

    while True:

        print("\n" + "=" * 50)
        print("          EXAM MANAGEMENT")
        print("=" * 50)

        print("1. Add Exam")
        print("2. View Exams")
        print("3. Update Exam")
        print("4. Delete Exam")
        print("5. Back")

        print("=" * 50)


        choice = input("Enter your choice: ")



        if choice == "1":

            add_exam()



        elif choice == "2":

            view_exam()



        elif choice == "3":

            update_exam()



        elif choice == "4":

            delete_exam()



        elif choice == "5":

            print("\nReturning...")
            break



        else:

            print("\nInvalid Choice! ❌")



if __name__ == "__main__":

    exam_management()