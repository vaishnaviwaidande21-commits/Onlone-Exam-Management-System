import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


from db_connection import get_connection



def view_teachers():

    conn = get_connection()
    cursor = conn.cursor()


    try:

        cursor.execute("""
        SELECT 
            teacher_id,
            name,
            email,
            subject
        FROM teacher
        """)


        teachers = cursor.fetchall()



        if not teachers:

            print("\nNo Teachers Found!")
            return



        print("\n" + "="*75)
        print("                 TEACHER LIST")
        print("="*75)


        print(
            f"{'ID':<5}{'Name':<20}{'Email':<30}{'Subject':<15}"
        )


        print("-"*75)



        for teacher in teachers:

            print(
                f"{teacher[0]:<5}{teacher[1]:<20}{teacher[2]:<30}{teacher[3]:<15}"
            )


        print("="*75)



    except Exception as e:

        print("Error:", e)



    finally:

        conn.close()



if __name__ == "__main__":

    view_teachers()