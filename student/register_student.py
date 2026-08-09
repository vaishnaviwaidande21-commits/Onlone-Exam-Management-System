import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


from db_connection import get_connection



def register_student():

    conn = get_connection()
    cursor = conn.cursor()


    try:

        print("\n========== STUDENT REGISTRATION ==========")

        name = input("Enter Name     : ")
        email = input("Enter Email    : ")
        password = input("Enter Password : ")


        cursor.execute("""
        INSERT INTO student
        (
        name,
        email,
        password
        )
        VALUES (?, ?, ?)
        """,
        (
            name,
            email,
            password
        ))


        conn.commit()


        print("\nRegistration Successful! ✅")
        print("Now you can login.")


    except Exception as e:

        print("Error:", e)


    finally:

        conn.close()



if __name__ == "__main__":

    register_student()