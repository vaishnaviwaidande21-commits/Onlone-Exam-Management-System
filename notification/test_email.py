import sys
import os

sys.path.append(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
)


from notification.email_service import send_email



def test_email():

    send_email(
        "purva@gmail.com",
        "Exam Completed Successfully",
        "Hello Student, Your exam successfully ended."
    )



if __name__ == "__main__":

    test_email()