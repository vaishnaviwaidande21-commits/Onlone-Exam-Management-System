import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


from db_connection import get_connection
from session.user_session import get_user



def view_my_exams():

    user = get_user()

    teacher_id = user["id"]

    conn = get_connection()
    cursor = conn.cursor()


    cursor.execute("""
    SELECT exam_id, exam_name, subject
    FROM exam
    WHERE teacher_id = ?
    """,(teacher_id,))


    exams = cursor.fetchall()


    print("\n========== MY EXAMS ==========")

    if exams:

        print("-" * 60)
        print(f"{'ID':<5}{'Exam Name':<25}{'Subject':<20}")
        print("-" * 60)


        for exam in exams:

            print(f"{exam[0]:<5}{exam[1]:<25}{exam[2]:<20}")


        print("-" * 60)

    else:

        print("No Exams Found!")


    conn.close()



def delete_exam():

    exam_id = input("Enter Exam ID to Delete: ")


    conn = get_connection()
    cursor = conn.cursor()


    cursor.execute(
        "DELETE FROM exam WHERE exam_id=?",
        (exam_id,)
    )


    conn.commit()


    if cursor.rowcount > 0:
        print("Exam Deleted Successfully! ✅")

    else:
        print("Exam Not Found!")


    conn.close()



def exam_management():

    while True:

        print("\n===== EXAM MANAGEMENT =====")
        print("1. View My Exams")
        print("2. Delete Exam")
        print("3. Back")


        choice = input("Enter your choice: ")


        if choice == "1":

            view_my_exams()


        elif choice == "2":

            delete_exam()


        elif choice == "3":

            break


        else:

            print("Invalid Choice!")



if __name__ == "__main__":

    exam_management()