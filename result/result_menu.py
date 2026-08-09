import sys
import os

sys.path.append(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
)


from result.save_result import save_result
from result.view_result import view_result



def result_menu():

    while True:

        print("\n" + "=" * 50)
        print("             RESULT MANAGEMENT")
        print("=" * 50)

        print("1. Save Result")
        print("2. View Result")
        print("3. Back")

        print("=" * 50)


        choice = input("Enter your choice: ")



        if choice == "1":

            save_result()



        elif choice == "2":

            view_result()



        elif choice == "3":

            print("\nReturning...")
            break



        else:

            print("\nInvalid Choice!")



if __name__ == "__main__":

    result_menu()