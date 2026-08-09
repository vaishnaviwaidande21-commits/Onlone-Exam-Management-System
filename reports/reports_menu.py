from reports.exam_report import exam_report
from reports.student_report import student_report
from reports.performance_report import performance_report


def reports_menu():

    while True:

        print("\n" + "=" * 50)
        print("             REPORTS")
        print("=" * 50)

        print("1. Exam Report")
        print("2. Student Report")
        print("3. Performance Report")
        print("4. Back")

        print("=" * 50)

        choice = input("Enter your choice: ")

        if choice == "1":
            exam_report()

        elif choice == "2":
            student_report()

        elif choice == "3":
            performance_report()

        elif choice == "4":
            break

        else:
            print("Invalid Choice!")