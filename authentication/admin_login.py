import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


from db_connection import get_connection
from admin.admin_menu import admin_menu



def admin_login():

    conn = get_connection()
    cursor = conn.cursor()


    try:

        print("\n========== ADMIN LOGIN ==========")

        username = input("Enter Username : ")
        password = input("Enter Password : ")


        cursor.execute("""
        SELECT admin_id, username
        FROM admin
        WHERE username = ? AND password = ?
        """,
        (
            username,
            password
        ))


        admin = cursor.fetchone()


        if admin:

            print("\nLogin Successful! ✅")
            print("Welcome,", admin[1])

            admin_menu()


        else:

            print("\nInvalid Username or Password!")


    except Exception as e:

        print("Error:", e)


    finally:

        conn.close()



if __name__ == "__main__":

    admin_login()