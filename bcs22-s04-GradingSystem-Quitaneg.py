def student_data():
    students = []

    num_students = int(input("Enter the number of students: "))

    for _ in range(num_students):
        student = {}

        student['Name'] = input("Name: ")
        student['Q1 Grade'] = int(input("Q1 Grade: "))
        student['Q2 Grade'] = int(input("Q2 Grade: "))
        student['Q3 Grade'] = int(input("Q3 Grade: "))
        student['Final Exam Grade'] = int(input("Final Exam Grade: "))
        student['Class Participation Grade'] = int(input("Class Participation Grade: "))

        students.append(student)

    format_spec = '{:<10}{:<10}{:<10}{:<25}{:<25}{:<30}{}'

    print(format_spec.format("Name", "Q1", "Q2", "Q3", "Final Exam Grade", "Class Participation Grade", "Status"))
    print("="*115)

    for student in students:
        total_grade = (student['Q1 Grade'] + student['Q2 Grade'] + student['Q3 Grade']) / 3
        average_grade = (total_grade * 0.4) + (student['Class Participation Grade'] * 0.2) + (student['Final Exam Grade'] * 0.4)

        student['Result'] = "Passed" if average_grade >= 75 else "Failed"

        print(format_spec.format(student['Name'], student['Q1 Grade'], student['Q2 Grade'], student['Q3 Grade'], student['Final Exam Grade'], student['Class Participation Grade'], student['Result']))

student_data()
