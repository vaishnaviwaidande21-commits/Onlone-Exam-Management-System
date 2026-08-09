from flask import Flask, render_template, request, redirect, url_for, session
import sqlite3
import os


app = Flask(__name__)

app.secret_key = "online_exam_secret_key"

app.config['TEMPLATES_AUTO_RELOAD'] = True


# ==========================
# DATABASE CONNECTION
# ==========================

def get_connection():

    base_path = os.path.dirname(
        os.path.dirname(os.path.abspath(__file__))
    )

    db_path = os.path.join(
        base_path,
        "database",
        "online_exam.db"
    )

    conn = sqlite3.connect(db_path)

    conn.row_factory = sqlite3.Row

    return conn



# ==========================
# HOME
# ==========================

@app.route("/")
def home():

    return render_template("login.html")



# ==========================
# LOGIN PAGES
# ==========================

@app.route("/admin_login")
def admin_login():

    return render_template("admin_login.html")



@app.route("/teacher_login")
def teacher_login():

    return render_template("teacher_login.html")



@app.route("/student_login")
def student_login():

    return render_template("student_login.html")





# ==========================
# ADMIN LOGIN
# ==========================

@app.route("/admin_login", methods=["POST"])
def admin_login_process():


    username = request.form["username"]

    password = request.form["password"]


    conn = get_connection()

    cursor = conn.cursor()


    cursor.execute(
        """
        SELECT *
        FROM admin
        WHERE username=?
        AND password=?
        """,
        (
            username,
            password
        )
    )


    admin = cursor.fetchone()

    conn.close()



    if admin:

        return redirect(
            url_for("admin")
        )


    return "Invalid Admin Username or Password"





# ==========================
# MANAGE TEACHERS
# ==========================

@app.route("/manage_teachers")
def manage_teachers():

    return render_template(
        "manage_teachers.html"
    )





# ==========================
# ADD TEACHER
# ==========================

@app.route("/add_teacher", methods=["GET","POST"])
def add_teacher():


    if request.method == "POST":


        name = request.form["name"]

        email = request.form["email"]

        password = request.form["password"]

        subject = request.form["subject"]



        conn = get_connection()

        cursor = conn.cursor()



        cursor.execute(
            """
            SELECT *
            FROM teacher
            WHERE email=?
            """,
            (email,)
        )


        exists = cursor.fetchone()



        if exists:

            conn.close()

            return "Teacher with this email already exists"




        cursor.execute(
            """
            INSERT INTO teacher
            (name,email,password,subject)

            VALUES(?,?,?,?)
            """,
            (
                name,
                email,
                password,
                subject
            )
        )


        conn.commit()

        conn.close()



        return redirect(
            url_for("view_teachers")
        )



    return render_template(
        "add_teacher.html"
    )





# ==========================
# VIEW TEACHERS
# ==========================

@app.route("/view_teachers")
def view_teachers():


    conn = get_connection()

    cursor = conn.cursor()


    cursor.execute(
        """
        SELECT *
        FROM teacher
        """
    )


    teachers = cursor.fetchall()


    conn.close()



    return render_template(
        "view_teachers.html",
        teachers=teachers
    )






# ==========================
# UPDATE TEACHER
# ==========================

@app.route("/update_teacher", methods=["GET","POST"])
def update_teacher():


    if request.method == "POST":


        teacher_id = request.form["teacher_id"]

        name = request.form["name"]

        email = request.form["email"]

        password = request.form["password"]

        subject = request.form["subject"]



        conn = get_connection()

        cursor = conn.cursor()



        cursor.execute(
            """
            UPDATE teacher
            SET name=?,
                email=?,
                password=?,
                subject=?

            WHERE teacher_id=?
            """,
            (
                name,
                email,
                password,
                subject,
                teacher_id
            )
        )


        conn.commit()

        conn.close()



        return redirect(
            url_for("view_teachers")
        )


    return render_template(
        "update_teacher.html"
    )






# ==========================
# DELETE TEACHER
# ==========================

@app.route("/delete_teacher", methods=["GET","POST"])
def delete_teacher():


    if request.method == "POST":


        teacher_id = request.form["teacher_id"]



        conn = get_connection()

        cursor = conn.cursor()



        cursor.execute(
            """
            DELETE FROM teacher
            WHERE teacher_id=?
            """,
            (teacher_id,)
        )


        conn.commit()

        conn.close()



        return redirect(
            url_for("view_teachers")
        )



    return render_template(
        "delete_teacher.html"
    )






# ==========================
# TEACHER LOGIN
# ==========================

@app.route("/teacher_login", methods=["POST"])
def teacher_login_process():


    email = request.form["username"]

    password = request.form["password"]



    conn = get_connection()

    cursor = conn.cursor()



    cursor.execute(
        """
        SELECT *
        FROM teacher
        WHERE email=?
        AND password=?
        """,
        (
            email,
            password
        )
    )



    teacher = cursor.fetchone()



    conn.close()



    if teacher:

        return redirect(
            url_for("teacher")
        )


    return "Invalid Teacher Username or Password"







# ==========================
# STUDENT LOGIN
# ==========================

@app.route("/student_login", methods=["POST"])
def student_login_process():

    email = request.form["username"]

    password = request.form["password"]

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT *
        FROM student
        WHERE email=?
        AND password=?
        """,
        (
            email,
            password
        )
    )

    student = cursor.fetchone()

    conn.close()

    if student:

        session["student_id"] = student["student_id"]

        session["student_name"] = student["name"]

        return redirect(
            url_for("student")
        )

    return "Invalid Student Username or Password"




# ==========================
# VIEW PROFILE
# ==========================

@app.route("/view_profile")
def view_profile():

    student_id = session.get("student_id")

    if not student_id:
        return redirect(url_for("student_login"))

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            student_id,
            name,
            email,
            registration_date
        FROM student
        WHERE student_id = ?
    """, (student_id,))

    student = cursor.fetchone()

    conn.close()

    if not student:
        return "Student profile not found"

    return render_template(
        "view_profile.html",
        student=student
    )





# ==========================
# TEACHER MODULE PAGES
# ==========================


@app.route("/create_exam", methods=["GET", "POST"])
def create_exam():

    if request.method == "POST":

        exam_name = request.form["exam_name"]
        subject = request.form["subject"]
        question_type = request.form["question_type"]
        number_of_questions = request.form["number_of_questions"]
        duration = request.form["duration"]
        total_marks = request.form["total_marks"]

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            """
            INSERT INTO exam
            (
                exam_name,
                subject,
                question_type,
                number_of_questions,
                duration,
                total_marks
            )
            VALUES (?, ?, ?, ?, ?, ?)
            """,
            (
                exam_name,
                subject,
                question_type,
                number_of_questions,
                duration,
                total_marks
            )
        )

        conn.commit()
        conn.close()

        return redirect(url_for("view_exams"))

    return render_template("create_exam.html")

@app.route("/manage_questions")
def manage_questions():

    return render_template(
        "manage_questions.html"
    )



@app.route("/ai_generator")
def ai_generator():

    return render_template(
        "ai_generator.html"
    )



@app.route("/student_results")
def student_results():

    return render_template(
        "student_results.html"
    )

# ==========================
# ADMIN MODULE PAGES
# ==========================

@app.route("/manage_students")
def manage_students():

    return render_template(
        "manage_students.html"
    )



@app.route("/manage_exams")
def manage_exams():

    return render_template(
        "manage_exams.html"
    )



@app.route("/manage_reports")
def manage_reports():

    return render_template(
        "manage_reports.html"
    )



@app.route("/student_report")
def student_report():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            student_id,
            name,
            email,
            course,
            year
        FROM student
        ORDER BY student_id
    """)

    students = cursor.fetchall()

    conn.close()

    return render_template(
        "student_report.html",
        students=students
    )


@app.route("/exam_report")
def exam_report():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            exam_id,
            exam_name,
            subject,
            question_type,
            number_of_questions,
            duration,
            total_marks
        FROM exam
        ORDER BY exam_id
    """)

    exams = cursor.fetchall()

    conn.close()

    return render_template(
        "exam_report.html",
        exams=exams
    )


@app.route("/question_bank_report")
def question_bank_report():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            question_id,
            subject,
            topic,
            question_text,
            option_a,
            option_b,
            option_c,
            option_d,
            correct_answer,
            question_type
        FROM question
        ORDER BY question_id
    """)

    questions = cursor.fetchall()

    print("========== EXAM DEBUG ==========")
    print("EXAM ID:", exam_id)
    print("TOTAL QUESTIONS:", len(questions))
    print("QUESTIONS:", [dict(q) for q in questions])
    print("================================")

    print("TOTAL QUESTIONS:", len(questions))

    conn.close()

    return render_template(
        "question_bank_report.html",
        questions=questions
    )



@app.route("/result_report")
def result_report():

    return render_template(
        "result_report.html"
    )



# ==========================
# STUDENT MANAGEMENT
# ==========================



@app.route("/add_student", methods=["GET", "POST"])
def add_student():

    if request.method == "POST":

        name = request.form["name"]
        email = request.form["email"]
        password = request.form["password"]
        year = request.form["year"]

        # Registration date = Student added date
        from datetime import datetime
        registration_date = datetime.now().strftime("%Y-%m-%d")

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            """
            INSERT INTO student
            (name, email, password, year, registration_date)
            VALUES (?, ?, ?, ?, ?)
            """,
            (
                name,
                email,
                password,
                year,
                registration_date
            )
        )

        conn.commit()
        conn.close()

        return redirect(url_for("view_students"))

    return render_template("add_student.html")





@app.route("/view_students")
def view_students():

    conn = get_connection()
    cursor = conn.cursor()


    cursor.execute(
        """
        SELECT *
        FROM student
        """
    )


    students = cursor.fetchall()

    conn.close()


    return render_template(
        "view_students.html",
        students=students
    )





# ==========================
# UPDATE STUDENT
# ==========================

@app.route("/update_student", methods=["GET", "POST"])
def update_student():

    if request.method == "POST":

        student_id = request.form["student_id"]
        name = request.form["name"]
        email = request.form["email"]
        password = request.form["password"]
        year = request.form["year"]

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            """
            UPDATE student
            SET name=?,
                email=?,
                password=?,
                year=?
            WHERE student_id=?
            """,
            (
                name,
                email,
                password,
                year,
                student_id
            )
        )

        conn.commit()
        conn.close()

        return redirect(url_for("view_students"))

    return render_template("update_student.html")

@app.route("/delete_student", methods=["GET","POST"])
def delete_student():


    if request.method == "POST":


        student_id = request.form["student_id"]


        conn = get_connection()
        cursor = conn.cursor()


        cursor.execute(
            """
            DELETE FROM student
            WHERE student_id=?
            """,
            (student_id,)
        )


        conn.commit()
        conn.close()


        return redirect(url_for("view_students"))



    return render_template("delete_student.html")


# ==========================
# DASHBOARDS
# ==========================

@app.route("/admin")
def admin():

    return render_template(
        "admin_dashboard.html"
    )



@app.route("/teacher")
def teacher():

    return render_template(
        "teacher_dashboard.html"
    )



@app.route("/student")
def student():

    return render_template(
        "student_dashboard.html"
    )



@app.route("/start_exam_selection")
def start_exam_selection():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT exam_id,
               exam_name,
               subject,
               number_of_questions,
               duration,
               total_marks
        FROM exam
        ORDER BY exam_id
    """)

    exams = cursor.fetchall()

    conn.close()

    return render_template(
        "start_exam_selection.html",
        exams=exams
    )
@app.route("/start_exam/<int:exam_id>")
def start_exam(exam_id):

    conn = get_connection()
    cursor = conn.cursor()

    # Get exam details
    cursor.execute("""
        SELECT exam_id,
               exam_name,
               subject,
               number_of_questions,
               duration,
               total_marks
        FROM exam
        WHERE exam_id = ?
    """, (exam_id,))

    exam = cursor.fetchone()

    if not exam:
        conn.close()
        return "Exam not found"

    # Number of questions selected for this exam
    number_of_questions = int(exam["number_of_questions"])

    # Get ONLY the required number of questions
    cursor.execute("""
        SELECT question_id,
               question_text,
               option_a,
               option_b,
               option_c,
               option_d,
               correct_answer,
               question_type
        FROM question
        WHERE exam_id = ?
        ORDER BY question_id
        LIMIT ?
    """, (exam_id, number_of_questions))

    question_rows = cursor.fetchall()

    conn.close()

    if not question_rows:
        return "No questions available for this exam"

    # Convert sqlite Row objects into normal lists
    questions = [list(row) for row in question_rows]

    return render_template(
        "start_exam.html",
        exam=exam,
        questions=questions
    )




# ==========================
# SUBMIT EXAM
# ==========================

@app.route("/submit_exam", methods=["POST"])
def submit_exam():

    student_id = session.get("student_id")

    if not student_id:
        return "Student login required"

    exam_id = request.form.get("exam_id")
    answers_json = request.form.get("answers")

    if not exam_id or not answers_json:
        return "Invalid exam submission"

    import json
    from datetime import datetime

    try:
        answers = json.loads(answers_json)
    except:
        return "Invalid answers data"

    conn = get_connection()
    cursor = conn.cursor()

    # ==========================
    # GET EXAM QUESTION LIMIT
    # ==========================

    cursor.execute(
        """
        SELECT number_of_questions
        FROM exam
        WHERE exam_id = ?
        """,
        (exam_id,)
    )

    exam_data = cursor.fetchone()

    if not exam_data:
        conn.close()
        return "Exam not found"

    number_of_questions = int(
        exam_data["number_of_questions"]
    )

    # ==========================
    # GET ONLY REQUIRED QUESTIONS
    # ==========================

    cursor.execute(
        """
        SELECT
            question_id,
            option_a,
            option_b,
            option_c,
            option_d,
            correct_answer
        FROM question
        WHERE exam_id = ?
        ORDER BY question_id
        LIMIT ?
        """,
        (
            exam_id,
            number_of_questions
        )
    )

    questions = cursor.fetchall()

    # ==========================
    # DELETE OLD ANSWERS
    # ==========================

    cursor.execute(
        """
        DELETE FROM student_answer
        WHERE student_id = ?
        AND exam_id = ?
        """,
        (
            student_id,
            exam_id
        )
    )

    # ==========================
    # CHECK ANSWERS
    # ==========================

    correct_count = 0

    total_questions = len(questions)

    for q in questions:

        question_id = q["question_id"]

        correct_answer = q["correct_answer"]

        selected_answer = answers.get(
            str(question_id),
            ""
        )

        # Convert A/B/C/D into actual option text

        if selected_answer == "A":

            selected_value = q["option_a"]

        elif selected_answer == "B":

            selected_value = q["option_b"]

        elif selected_answer == "C":

            selected_value = q["option_c"]

        elif selected_answer == "D":

            selected_value = q["option_d"]

        else:

            selected_value = ""

        # Compare actual option value

        if selected_value == correct_answer:

            correct_count += 1

        # ==========================
        # SAVE STUDENT ANSWER
        # ==========================

        cursor.execute(
            """
            INSERT INTO student_answer
            (
                student_id,
                exam_id,
                question_id,
                selected_answer,
                correct_answer
            )
            VALUES (?, ?, ?, ?, ?)
            """,
            (
                student_id,
                exam_id,
                question_id,
                selected_value,
                correct_answer
            )
        )

    # ==========================
    # WRONG ANSWERS
    # ==========================

    wrong_count = (
        total_questions - correct_count
    )

    # ==========================
    # PERCENTAGE
    # ==========================

    if total_questions > 0:

        percentage = (
            correct_count /
            total_questions
        ) * 100

    else:

        percentage = 0

    # ==========================
    # GRADE
    # ==========================

    if percentage >= 90:

        grade = "A+"

    elif percentage >= 80:

        grade = "A"

    elif percentage >= 70:

        grade = "B"

    elif percentage >= 60:

        grade = "C"

    elif percentage >= 50:

        grade = "D"

    else:

        grade = "F"

    # ==========================
    # ANALYSIS
    # ==========================

    analysis = (
        f"You answered {correct_count} "
        f"questions correctly and "
        f"{wrong_count} questions incorrectly."
    )

    # ==========================
    # DELETE OLD RESULT
    # ==========================

    cursor.execute(
        """
        DELETE FROM result
        WHERE student_id = ?
        AND exam_id = ?
        """,
        (
            student_id,
            exam_id
        )
    )

    # ==========================
    # SAVE RESULT
    # ==========================

    cursor.execute(
        """
        INSERT INTO result
        (
            student_id,
            exam_id,
            total_questions,
            correct_answers,
            wrong_answers,
            percentage,
            grade,
            analysis,
            date
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
        (
            student_id,
            exam_id,
            total_questions,
            correct_count,
            wrong_count,
            percentage,
            grade,
            analysis,
            datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S"
            )
        )
    )

    conn.commit()

    conn.close()

    return redirect(
        url_for("view_result")
    )


# ==========================
# VIEW ALL RESULTS
# ==========================

@app.route("/view_result")
def view_result():

    student_id = session.get("student_id")

    if not student_id:
        return "Student login required"

    conn = get_connection()
    cursor = conn.cursor()

    # ==========================
    # GET ALL RESULTS OF STUDENT
    # ==========================

    cursor.execute("""
        SELECT
            r.result_id,
            r.student_id,
            r.exam_id,
            r.total_questions,
            r.correct_answers,
            r.wrong_answers,
            r.percentage,
            r.grade,
            r.analysis,
            r.date,

            s.name AS student_name,

            e.exam_name,
            e.subject,
            e.total_marks

        FROM result r

        LEFT JOIN student s
            ON r.student_id = s.student_id

        LEFT JOIN exam e
            ON r.exam_id = e.exam_id

        WHERE r.student_id = ?

        ORDER BY r.result_id DESC
    """, (student_id,))

    results = cursor.fetchall()

    # ==========================
    # GET QUESTION-WISE ANSWERS
    # FOR EACH RESULT
    # ==========================

    result_data = []

    for result in results:

        cursor.execute("""
            SELECT
                sa.question_id,
                q.question_text,
                sa.selected_answer,
                sa.correct_answer

            FROM student_answer sa

            LEFT JOIN question q
                ON sa.question_id = q.question_id

            WHERE sa.student_id = ?
            AND sa.exam_id = ?

            ORDER BY sa.answer_id
        """, (
            result["student_id"],
            result["exam_id"]
        ))

        answers = cursor.fetchall()

        result_data.append({
            "result": result,
            "answers": answers
        })

    conn.close()

    return render_template(
        "view_result.html",
        results=result_data
    )



@app.route("/available_exams")
def available_exams():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT exam_id,
               exam_name,
               subject,
               number_of_questions,
               duration,
               total_marks
        FROM exam
        ORDER BY exam_id
    """)

    exams = cursor.fetchall()

    conn.close()

    return render_template(
        "available_exams.html",
        exams=exams
    )










# ==========================
# MANAGE EXAM
# ==========================



@app.route("/manage_exam")
def manage_exam():

    return render_template(
        "manage_exams.html"
    )



# ==========================
# ADD EXAM
# ==========================

@app.route("/add_exam", methods=["GET", "POST"])
def add_exam():

    if request.method == "POST":

        exam_name = request.form["exam_name"]
        subject = request.form["subject"]
        question_type = request.form["question_type"]
        number_of_questions = request.form["number_of_questions"]
        duration = request.form["duration"]
        total_marks = request.form["total_marks"]

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            """
            INSERT INTO exam
            (
                exam_name,
                subject,
                question_type,
                number_of_questions,
                duration,
                total_marks
            )
            VALUES (?, ?, ?, ?, ?, ?)
            """,
            (
                exam_name,
                subject,
                question_type,
                number_of_questions,
                duration,
                total_marks
            )
        )

        conn.commit()
        conn.close()

        return redirect(url_for("view_exams"))

    return render_template("add_exam.html")


# ==========================
# VIEW EXAMS
# ==========================
@app.route("/view_exams")
def view_exams():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            exam_id,
            exam_name,
            subject,
            teacher_id,
            duration,
            question_type,
            number_of_questions,
            total_marks
        FROM exam
        ORDER BY exam_id
    """)

    exams = cursor.fetchall()

    conn.close()

    return render_template(
        "view_exams.html",
        exams=exams
    )
# ==========================
# UPDATE EXAM
# ==========================

@app.route("/update_exam", methods=["GET", "POST"])
def update_exam():

    if request.method == "POST":

        exam_id = request.form["exam_id"]
        exam_name = request.form["exam_name"]
        subject = request.form["subject"]
        question_type = request.form["question_type"]
        number_of_questions = request.form["number_of_questions"]
        duration = request.form["duration"]
        total_marks = request.form["total_marks"]

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            """
            UPDATE exam
            SET
                exam_name = ?,
                subject = ?,
                question_type = ?,
                number_of_questions = ?,
                duration = ?,
                total_marks = ?
            WHERE exam_id = ?
            """,
            (
                exam_name,
                subject,
                question_type,
                number_of_questions,
                duration,
                total_marks,
                exam_id
            )
        )

        print("===== RESULT DEBUG =====")
        print("TOTAL:", total_questions)
        print("CORRECT:", correct_count)
        print("WRONG:", wrong_count)


        conn.commit()

        rows_updated = cursor.rowcount

        conn.close()

        if rows_updated == 0:
            return "Exam ID not found"

        return redirect(url_for("view_exams"))

    return render_template("update_exam.html")


# ==========================
# DELETE EXAM
# ==========================

@app.route("/delete_exam", methods=["GET", "POST"])
def delete_exam():

    if request.method == "POST":

        exam_id = request.form["exam_id"]

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            """
            DELETE FROM exam
            WHERE exam_id=?
            """,
            (exam_id,)
        )

        conn.commit()
        conn.close()

        return redirect(url_for("view_exams"))

    return render_template("delete_exam.html")



# ==========================
# RUN APP
# ==========================



# ==========================
# RUN APP
# ==========================

if __name__ == "__main__":

    app.run(debug=True)