
def student_data():
    names = []
    q1_grades = []
    q2_grades = []
    q3_grades = []
    final_exam_grades = []
    class_participation_grades = []

    num_students = int(input("Enter the number of students: "))

    for _ in range(num_students):
        name = input("Name: ")
        names.append(name)

        q1_grade = int(input("Q1 Grade: "))
        q1_grades.append(q1_grade)

        q2_grade = int(input("Q2 Grade: "))
        q2_grades.append(q2_grade)

        q3_grade = int(input("Q3 Grade: "))
        q3_grades.append(q3_grade)

        final_exam_grade = int(input("Final Exam Grade: "))
        final_exam_grades.append(final_exam_grade)

        class_participation_grade = int(input("Class Participation Grade: "))
        class_participation_grades.append(class_participation_grade)

    user_input = input("Do you want to enter data for another student? (yes/no): ")
    if user_input.lower() == 'yes':
        student_data()
    elif user_input.lower() == 'no':
        for i in range(num_students):
            total_grade = (q1_grades[i] + q2_grades[i] + q3_grades[i]) / 3
            average_grade = (total_grade * 0.4) + (class_participation_grades[i] * 0.2) + (final_exam_grades[i] * 0.4)

            if average_grade >= 75:
                print(names[i], "passed.")
                fmt = {'{0:30}{1:30}{2:30}'}.format()
            else:
                print(names[i], "failed.")

student_data()
