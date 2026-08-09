from db_connection import get_connection


def view_questions():

    subject = input("\nEnter Subject: ").strip().lower()


    conn = get_connection()
    cursor = conn.cursor()


    cursor.execute(
        """
        SELECT
        question_text,
        option_a,
        option_b,
        option_c,
        option_d,
        correct_answer,
        difficulty,
        question_type

        FROM question

        WHERE LOWER(subject)=?

        """,
        (subject,)
    )


    questions = cursor.fetchall()


    conn.close()



    if not questions:

        print("\nNo Questions Found ❌")
        return



    print("\n")

    print("="*80)

    print("                 QUESTION PAPER")

    print("="*80)



    print("\nSubject :", subject)

    print(
        "Total Questions :",
        len(questions)
    )


    print("="*80)



    count = 1


    for q in questions:


        print("\n")

        print("-"*80)


        print(
            f"Q{count}. {q[0]}"
        )



        # True / False Question

        if q[7] == "True/False":


            print("A)", q[1])

            print("B)", q[2])


        else:


            print("A)", q[1])

            print("B)", q[2])

            print("C)", q[3])

            print("D)", q[4])



        print(
            "\nCorrect Answer :",
            q[5]
        )


        print(
            "Difficulty :",
            q[6]
        )


        print(
            "Type :",
            q[7]
        )


        print("-"*80)


        count += 1