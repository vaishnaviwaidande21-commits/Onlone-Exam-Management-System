import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


from db_connection import get_connection



def performance_report():

    conn = get_connection()
    cursor = conn.cursor()


    try:

        cursor.execute("""
        SELECT

        student.name,
        AVG(result.percentage)

        FROM result

        JOIN student

        ON result.student_id = student.student_id


        GROUP BY student.student_id

        """)


        data = cursor.fetchall()


        if not data:

            print("\nNo Performance Data Found!")
            return



        print("\n" + "="*70)
        print("             AI PERFORMANCE REPORT")
        print("="*70)


        print(
            f"{'Student':<20}{'Average Score':<20}{'Performance':<20}"
        )


        print("-"*70)



        for row in data:


            average = row[1]


            if average >= 80:

                level = "Excellent ⭐⭐⭐⭐⭐"


            elif average >= 60:

                level = "Good ⭐⭐⭐⭐"


            elif average >= 40:

                level = "Average ⭐⭐⭐"


            else:

                level = "Need Improvement ⭐⭐"



            print(
                f"{row[0]:<20}{average:.2f}%{'':<12}{level}"
            )


        print("\nAI Suggestions:")
        print("✔ Practice Advanced Questions")
        print("✔ Attempt More Mock Tests")


        print("="*70)



    except Exception as e:

        print("Error:", e)



    finally:

        conn.close()



if __name__ == "__main__":

    performance_report()