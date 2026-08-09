import sys
import os

sys.path.append(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
)

from notification.email_service import send_email


def missed_exam_notification():

    print("\n" + "=" * 50)
    print("        MISSED EXAM NOTIFICATION")
    print("=" * 50)


    email = input("Enter Student Email: ")


    send_email(
        email,
        "Missed Exam Notification",
        "Hello Student, You missed your scheduled exam."
    )


    print("=" * 50)



if __name__ == "__main__":

    missed_exam_notification()