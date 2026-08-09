import sys
import os
from datetime import datetime

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


from db_connection import get_connection
from notification.email_service import send_email



def submit_exam(student_id, exam_id, answers):

    conn = get_connection()
    cursor = conn.cursor()


    try:


        cursor.execute("""
        SELECT
        COALESCE(correct_answer, answer)
        FROM question
        WHERE exam_id = ?
        """,
        (exam_id,))


        correct_answers = cursor.fetchall()



        total_questions = len(correct_answers)

        score = 0



        for index, answer in enumerate(answers):


            correct = correct_answers[index][0]


            if correct and answer.upper() == correct.upper():

                score += 1





        if total_questions > 0:

            percentage = (score / total_questions) * 100

        else:

            percentage = 0





        exam_date = datetime.now().strftime("%Y-%m-%d")




        cursor.execute("""
        INSERT INTO result
        (
        student_id,
        exam_id,
        score,
        total_questions,
        percentage,
        exam_date
        )
        VALUES (?, ?, ?, ?, ?, ?)
        """,
        (
            student_id,
            exam_id,
            score,
            total_questions,
            percentage,
            exam_date
        ))



        conn.commit()



        print("\n===== Exam Submitted Successfully =====")
        print("--------------------------------------")
        print("Total Questions :", total_questions)
        print("Correct Answers :", score)
        print("Score           :", f"{score}/{total_questions}")
        print("Percentage      :", f"{percentage:.2f}%")
        print("--------------------------------------")




        cursor.execute("""
        SELECT name,email
        FROM student
        WHERE student_id=?
        """,
        (student_id,))


        student = cursor.fetchone()



        if student:


            send_email(
                student[1],
                "Exam Completed Successfully",
                f"""
Hello {student[0]},

Your exam successfully ended.

Your result has been generated.

Score : {score}/{total_questions}
Percentage : {percentage:.2f}%

Thank you.
"""
            )



    except Exception as e:

        print("Error:", e)



    finally:

        conn.close()