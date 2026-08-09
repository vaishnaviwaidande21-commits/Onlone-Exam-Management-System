import sys
import os


sys.path.append(
    os.path.dirname(os.path.abspath(__file__))
)



def main_menu():


    while True:


        print("\n")
        print("="*60)
        print("       ONLINE EXAM MANAGEMENT SYSTEM")
        print("="*60)


        print("1. Admin Login")
        print("2. Teacher Login")
        print("3. Student Login")
        print("4. Exit")


        print("="*60)



        choice = input(
            "Enter Your Choice: "
        )



        # ================= ADMIN LOGIN =================


        if choice == "1":


            try:

                from admin.admin_login import admin_login

                admin_login()


            except Exception as e:

                print(
                    "Admin Login Error:",
                    e
                )






        # ================= TEACHER LOGIN =================


        elif choice == "2":


            try:


                from teacher.teacher_login import teacher_login


                login_status = teacher_login()



                if login_status:


                    from teacher.teacher_dashboard import teacher_dashboard


                    teacher_dashboard()



            except Exception as e:


                print(
                    "Teacher Login Error:",
                    e
                )








        # ================= STUDENT LOGIN =================


        elif choice == "3":


            try:


                from student.student_login import student_login


                login_status = student_login()



                if login_status:


                    from student.student_dashboard import student_dashboard


                    student_dashboard()



            except Exception as e:


                print(
                    "Student Login Error:",
                    e
                )








        # ================= EXIT =================


        elif choice == "4":


            print(
                "\nThank You For Using Online Exam Management System!"
            )


            break







        else:


            print(
                "\nInvalid Choice! Please Try Again."
            )







if __name__ == "__main__":


    main_menu()