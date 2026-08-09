````markdown
# 🎓 Online Exam Management System

A web-based **Online Exam Management System** developed using Python Flask, HTML, CSS, JavaScript, and SQLite.

The system provides separate modules for **Admin, Teacher, and Student**, making it easier to manage students, teachers, exams, questions, online examinations, and results.

---

## 📌 Project Description

The Online Exam Management System is designed to conduct examinations digitally and manage the complete examination process from one platform.

Students can log in, view available exams, start examinations, answer questions, submit exams, and view their results.

Administrators and teachers can manage students, exams, questions, and examination results.

---

# 🚀 Main Features

### 👨‍💼 Admin Module

- Admin Login
- Admin Dashboard
- Manage Students
- Add Student
- View Students
- Manage Teachers
- Manage Exams
- Manage Questions
- View Reports
- Examination Management

### 👨‍🏫 Teacher Module

- Teacher Login
- Teacher Dashboard
- Create Exam
- View Exams
- Manage Exams
- Generate Questions
- Manage Questions
- View Student Results

### 👨‍🎓 Student Module

- Student Login
- Student Dashboard
- View Available Exams
- Start Exam
- Online MCQ Examination
- Exam Timer
- Previous / Next Question Navigation
- Answer Tracking
- Submit Exam
- View Examination Results
- View Multiple Exam Results
- Question-wise Result
- Correct Answer
- Wrong Answer
- Percentage
- Grade
- Performance Analysis
- View Student Profile
- Student Registration Date

---

# 📝 Online Examination

The student can:

1. Login to the Student Portal.
2. View available examinations.
3. Select an examination.
4. Start the examination.
5. Answer MCQ questions.
6. Navigate between questions.
7. Track answered and remaining questions.
8. Complete the examination.
9. Submit the examination.
10. View the generated result.

---

# 📊 Result & Evaluation

After submitting an examination, the system provides:

- Total Questions
- Correct Answers
- Wrong Answers
- Percentage
- Grade
- Performance Analysis
- Question-wise Answers
- Student Selected Answer
- Correct Answer
- Correct / Wrong Status
- Attempt Date

Students can also view results from their previous examination attempts.

---

# 🤖 Smart Question Generation

The system includes a smart question-generation feature for creating examination questions.

It supports:

- Subject-based questions
- Topic-based questions
- Different question counts
- Question bank management
- MCQ-based examination questions

---

# 👤 Student Profile

The Student Profile displays important student information:

- Student Name
- Student ID
- Student Email
- Registration Date

The registration date is automatically stored when a new student is added.

---

# 🛠️ Technologies Used

| Technology | Purpose |
|------------|---------|
| Python | Backend Programming |
| Flask | Web Framework |
| HTML5 | Web Page Structure |
| CSS3 | User Interface Design |
| JavaScript | Frontend Interaction |
| SQLite | Database |
| Jinja2 | Flask Templates |

---

# 🗄️ Database

The project uses **SQLite** as the database.

The database stores information related to:

- Students
- Teachers
- Exams
- Questions
- Results
- Student Answers

Database file:

```text
database/online_exam.db
````

---

# 📂 Project Structure

```text
online_exam_management_system/
│
├── frontend/
│   │
│   ├── app.py
│   ├── requirements.txt
│   ├── README.md
│   │
│   ├── database/
│   │   └── online_exam.db
│   │
│   ├── templates/
│   │   ├── login.html
│   │   ├── student.html
│   │   ├── teacher.html
│   │   ├── admin.html
│   │   ├── available_exams.html
│   │   ├── start_exam.html
│   │   ├── view_result.html
│   │   ├── view_profile.html
│   │   └── ...
│   │
│   └── static/
│       ├── css/
│       ├── js/
│       └── images/
│
└── env/
```

---

# ⚙️ Installation

## 1. Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

## 2. Open the Project

```bash
cd online_exam_management_system
```

## 3. Create Virtual Environment

```bash
python -m venv env
```

## 4. Activate Virtual Environment

### Windows PowerShell

```powershell
.\env\Scripts\Activate.ps1
```

## 5. Install Required Packages

```bash
pip install -r requirements.txt
```

---

# ▶️ Run the Project

Go to the frontend directory:

```bash
cd frontend
```

Run Flask:

```bash
python app.py
```

The application will start at:

```text
http://127.0.0.1:5000
```

Open the address in your web browser.

---

# 🔐 User Modules

The system contains three main user roles:

```text
Admin
   │
   ├── Manage Students
   ├── Manage Teachers
   ├── Manage Exams
   ├── Manage Questions
   └── View Reports

Teacher
   │
   ├── Create Exam
   ├── Manage Exams
   ├── Generate Questions
   └── View Student Results

Student
   │
   ├── View Available Exams
   ├── Start Exam
   ├── Submit Exam
   ├── View Results
   └── View Profile
```

---

# 🎯 Project Objectives

* Digitize the examination process.
* Reduce manual examination work.
* Provide an easy-to-use examination interface.
* Automatically evaluate objective questions.
* Generate examination results.
* Store examination records digitally.
* Allow students to view previous results.
* Provide separate dashboards for different users.

---

# 🔮 Future Scope

The project can be further enhanced with:

* Online deployment
* Cloud database
* Email notifications
* Advanced analytics
* Improved AI-based question generation
* Password encryption
* Secure authentication
* PDF result generation
* Exam scheduling
* Automatic result notifications
* Mobile responsive improvements

---

# 📸 Screenshots

Screenshots of the following pages can be added here:

* Login Page
* Admin Dashboard
* Teacher Dashboard
* Student Dashboard
* Available Exams
* Start Exam
* Result Page
* Student Profile

Example:

```text
screenshots/
├── login.png
├── admin-dashboard.png
├── teacher-dashboard.png
├── student-dashboard.png
├── start-exam.png
├── result.png
└── profile.png
```

---

# 📚 Project Type

**Academic / Diploma Project**

### Project Name

**Online Exam Management System**

### Development Stack

**Python + Flask + SQLite + HTML + CSS + JavaScript**

---

# 👩‍💻 Author

**Vaishnavi Waidande**

Online Exam Management System
Diploma in Computer Engineering

---

# ⭐ Conclusion

The Online Exam Management System provides a complete digital platform for conducting and managing online examinations.

It simplifies examination management for administrators and teachers while providing students with an easy and user-friendly examination experience.

```
```
