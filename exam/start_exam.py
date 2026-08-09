import sys
import os

sys.path.append(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
)

from db_connection import get_connection



def start_exam():

    print("\n" + "="*60)
    print("                 START EXAM")
    print("="*60)


    exam_id = input("Enter Exam ID: ")


    conn = get_connection()
    cursor = conn.cursor()



    # Exam Details

    cursor.execute(
        """
        SELECT exam_name, subject
        FROM exam
        WHERE exam_id=?
        """,
        (exam_id,)
    )


    exam = cursor.fetchone()



    if not exam:

        print("Exam Not Found ❌")
        conn.close()
        return



    exam_name = exam[0]
    subject = exam[1]



    print("\nExam Name :", exam_name)
    print("Subject   :", subject)



    # Questions using subject

    cursor.execute(
        """
        SELECT
        question_text,
        option_a,
        option_b,
        option_c,
        option_d,
        correct_answer,
        question_type

        FROM question

        WHERE LOWER(subject)=?

        """,
        (subject.lower(),)
    )



    questions = cursor.fetchall()



    print("\nDEBUG QUESTIONS :", len(questions))



    if len(questions)==0:

        print("\nNo Questions Found ❌")
        conn.close()
        return



    print("\nQuestion Type :", questions[0][6])
    print("Total Questions :", len(questions))


    score = 0
    count = 1



    for q in questions:


        print("\n--------------------------------")

        print(f"Q{count}. {q[0]}")


        if q[6].lower()=="true/false":


            print("A) True")
            print("B) False")

            ans=input(
                "Select Answer (A/B): "
            ).upper()



        else:


            print("A)",q[1])
            print("B)",q[2])
            print("C)",q[3])
            print("D)",q[4])


            ans=input(
                "Select Answer: "
            ).upper()



        correct=q[5].split(")")[0].upper()


        if ans==correct:
            score+=1


        count+=1



    print("\n================ RESULT ================")

    print("Exam Name :",exam_name)

    print("Subject :",subject)

    print("Total Questions :",len(questions))

    print("Correct Answers :",score)


    percentage=(score/len(questions))*100

    print("Percentage :",round(percentage,2),"%")



    conn.close()




if __name__=="__main__":

    start_exam()