from notification.test_email import test_email
from notification.missed_exam_notification import missed_exam_notification


def notification_menu():

    while True:

        print("\n" + "=" * 50)
        print("          NOTIFICATION")
        print("=" * 50)

        print("1. Send Test Email")
        print("2. Missed Exam Notification")
        print("3. Back")

        print("=" * 50)

        choice = input("Enter your choice: ")

        if choice == "1":
            test_email()

        elif choice == "2":
            missed_exam_notification()

        elif choice == "3":
            break

        else:
            print("Invalid Choice!")