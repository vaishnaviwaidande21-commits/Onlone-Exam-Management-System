import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from db_connection import get_connection


def ai_analysis(student_id):

    conn = get_connection()
    cursor = conn.cursor()

    try:

        cursor.execute("""
        SELECT 
            exam.subject,
            result.percentage
        FROM result

        JOIN exam
        ON result.exam_id = exam.exam_id

        WHERE result.student_id = ?

        """, (student_id,))


        data = cursor.fetchall()


        if not data:
            print("\nNo Performance Data Found!")
            conn.close()
            return


        total = 0
        subjects = []


        for row in data:
            subjects.append((row[0], row[1]))
            total += row[1]


        average = total / len(data)


        print("\n" + "="*45)
        print("       AI PERFORMANCE ANALYSIS")
        print("="*45)

        print("\nStudent ID :", student_id)

        print("\nAverage Score :", f"{average:.2f}%")


        if average >= 80:

            level = "Excellent ⭐⭐⭐⭐⭐"

        elif average >= 60:

            level = "Good ⭐⭐⭐⭐"

        elif average >= 40:

            level = "Average ⭐⭐⭐"

        else:

            level = "Need Improvement ⭐⭐"


        print("Performance Level :", level)


        print("\nSubject Analysis:")
        

        for subject, percentage in subjects:

            print(
                f"✔ {subject} : {percentage:.2f}%"
            )


        print("\nAI Suggestions:")


        if average >= 80:

            print("• Keep practicing advanced topics")
            print("• Try more mock exams")


        elif average >= 60:

            print("• Practice difficult questions")
            print("• Improve weak concepts")


        else:

            print("• Revise basic concepts")
            print("• Practice daily MCQs")


        print("\n" + "="*45)


    except Exception as e:

        print("Error:", e)


    finally:

        conn.close()



if __name__ == "__main__":

    student_id = input("Enter Student ID: ")

    ai_analysis(student_id)