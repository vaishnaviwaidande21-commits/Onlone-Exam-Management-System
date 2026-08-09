import sys
import os

sys.path.append(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
)


from question.smart_question_generator import (
    create_questions,
    save_questions,
    display_questions
)

from question.view_question import view_questions
from question.update_question import update_question
from question.delete_question import delete_question



def question_management():


    while True:


        print("\n" + "=" * 50)
        print("        QUESTION MANAGEMENT")
        print("=" * 50)


        print("1. Generate Questions Using AI 🤖")
        print("2. View Questions")
        print("3. Update Question")
        print("4. Delete Question")
        print("5. Back")


        print("=" * 50)



        choice = input(
            "Enter your choice: "
        )



        # ==============================
        # GENERATE QUESTIONS
        # ==============================

        if choice == "1":



            subject = input(
                "\nEnter Subject: "
            ).lower()



            print(
                "\nSelect Question Type"
            )

            print(
                "1. MCQ"
            )

            print(
                "2. True / False"
            )

            print(
                "3. Fill in the Blanks"
            )



            type_choice = input(
                "\nEnter Question Type: "
            )



            if type_choice == "1":

                question_type = "MCQ"



            elif type_choice == "2":

                question_type = "True/False"



            elif type_choice == "3":

                question_type = "Fill in the Blanks"



            else:

                print(
                    "\nInvalid Question Type!"
                )

                continue





            difficulty = input(
                "\nEnter Difficulty (Easy/Medium/Hard): "
            )



            number = int(
                input(
                    "Enter Number of Questions: "
                )
            )



            # Generate Questions

            questions = create_questions(
                subject,
                difficulty,
                number,
                question_type
            )



            if questions:


                save_questions(
                    questions,
                    subject,
                    difficulty,
                    question_type,
                    exam_id=1
                )


                display_questions(
                    questions
                )


            else:


                print(
                    "\nNo Questions Generated ❌"
                )





        # ==============================
        # VIEW QUESTIONS
        # ==============================

        elif choice == "2":


            view_questions()





        # ==============================
        # UPDATE QUESTION
        # ==============================

        elif choice == "3":


            update_question()





        # ==============================
        # DELETE QUESTION
        # ==============================

        elif choice == "4":


            delete_question()





        # ==============================
        # BACK
        # ==============================

        elif choice == "5":


            print(
                "\nReturning..."
            )

            break





        else:


            print(
                "\nInvalid Choice!"
            )





if __name__ == "__main__":


    question_management()