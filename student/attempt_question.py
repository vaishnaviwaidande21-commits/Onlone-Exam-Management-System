import sys
import os
import random
import time
from datetime import datetime


sys.path.append(
    os.path.dirname(
        os.path.dirname(
            os.path.abspath(__file__)
        )
    )
)


from db_connection import get_connection



# ============================================================
# GET EXAM DETAILS
# ============================================================

def get_exam_details(cursor, exam_id):

    cursor.execute(
        """
        SELECT exam_name, subject
        FROM exam
        WHERE exam_id=?
        """,
        (exam_id,)
    )

    return cursor.fetchone()



# ============================================================
# GET QUESTIONS
# ============================================================

def get_questions(cursor, subject):

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
        (subject.lower(),)
    )

    return cursor.fetchall()



# ============================================================
# CHECK ANSWER
# ============================================================

def check_answer(answer, correct_answer):

    correct = (
        correct_answer
        .split(")")[0]
        .strip()
        .upper()
    )

    return answer == correct



# ============================================================
# AI ANALYSIS
# ============================================================

def ai_analysis(percentage):

    print("\nAI Analysis 🤖")
    print("-"*40)


    if percentage >= 90:

        print(
            "Excellent performance!"
        )


    elif percentage >= 75:

        print(
            "Good performance! Keep practicing."
        )


    elif percentage >= 50:

        print(
            "Average performance. Need more practice."
        )


    else:

        print(
            "Need improvement. Revise topics."
        )



# ============================================================
# TIMER DISPLAY
# ============================================================

def display_time(seconds):

    minutes = seconds // 60
    sec = seconds % 60


    print(
        f"⏱ Time Left : {minutes:02d}:{sec:02d}"
    )
    # ============================================================
# ATTEMPT EXAM
# ============================================================

def attempt_question(student_id, exam_id):


    conn = get_connection()

    cursor = conn.cursor()



    try:


        exam = get_exam_details(
            cursor,
            exam_id
        )


        if not exam:

            print("Exam Not Found ❌")
            return



        exam_name = exam[0]

        subject = exam[1]



        questions = get_questions(
            cursor,
            subject
        )



        if not questions:

            print("No Questions Found ❌")
            return



        random.shuffle(
            questions
        )



        total_questions = len(questions)



        # 1 Question = 1 Minute

        total_seconds = total_questions * 60



        start_time = time.time()



        print("\n")
        print("="*60)
        print("              ONLINE EXAM")
        print("="*60)


        print(
            "Exam Name :",
            exam_name
        )


        print(
            "Subject :",
            subject
        )


        print(
            "Total Questions :",
            total_questions
        )


        print(
            "Exam Time :",
            total_questions,
            "Minutes"
        )


        print("="*60)



        score = 0



        for index, question in enumerate(
            questions,
            start=1
        ):



            remaining = (
                total_seconds -
                int(time.time() - start_time)
            )



            if remaining <= 0:

                print(
                    "\n⏰ Time Over! Exam Submitted Automatically"
                )

                break



            print("\n")


            print("-"*60)


            print(
                f"Q{index}. {question[0]}"
            )


            print()


            print(
                "A)",
                question[1]
            )


            print(
                "B)",
                question[2]
            )


            print(
                "C)",
                question[3]
            )


            print(
                "D)",
                question[4]
            )


            print()


            print("-"*60)



            display_time(
                remaining
            )


            print("-"*60)



            answer = input(
                "\nSelect Answer (A/B/C/D): "
            ).upper()



            if check_answer(
                answer,
                question[5]
            ):

                score += 1





        print("\n")
        print("="*60)
        print("EXAM COMPLETED")
        print("="*60)



        wrong = (
            total_questions - score
        )



        percentage = (
            score /
            total_questions
        ) * 100



        if percentage >= 90:

            grade="A+"


        elif percentage >=80:

            grade="A"


        elif percentage >=70:

            grade="B"


        elif percentage >=60:

            grade="C"


        elif percentage >=40:

            grade="D"


        else:

            grade="Fail"



        print(
            "Correct Answers :",
            score
        )


        print(
            "Wrong Answers :",
            wrong
        )


        print(
            "Percentage :",
            round(percentage,2)
        )


        print(
            "Grade :",
            grade
        )



        ai_analysis(
            percentage
        )



        # SAVE RESULT

        cursor.execute(
            """
            INSERT INTO result
            (
                student_id,
                exam_id,
                total_questions,
                correct_answers,
                percentage,
                grade,
                date
            )

            VALUES(?,?,?,?,?,?,?)

            """,
            (
                student_id,
                exam_id,
                total_questions,
                score,
                percentage,
                grade,
                datetime.now().strftime("%Y-%m-%d")
            )
        )


        conn.commit()



        print(
            "\nResult Saved Successfully ✅"
        )



    except Exception as e:

        print(
            "Error:",
            e
        )


    finally:

        conn.close()




if __name__ == "__main__":

    print(
        "Run from start_exam.py"
    )