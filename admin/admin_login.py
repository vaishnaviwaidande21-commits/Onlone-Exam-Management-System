import sys
import os

sys.path.append(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
)


from db_connection import get_connection



def admin_login():

    print("\n" + "=" * 40)
    print("            ADMIN LOGIN")
    print("=" * 40)


    username = input("Enter Username: ")
    password = input("Enter Password: ")



    conn = get_connection()
    cursor = conn.cursor()


    cursor.execute(
        """
        SELECT * FROM admin 
        WHERE username=? AND password=?
        """,
        (username, password)
    )


    admin = cursor.fetchone()


    conn.close()



    if admin:

        print("\nLogin Successful! ✅")


        # Import after login success
        from admin.admin_menu import admin_menu

        admin_menu()


    else:

        print("\nInvalid Username or Password ❌")




if __name__ == "__main__":

    admin_login()