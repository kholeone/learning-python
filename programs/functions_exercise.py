student_name = input("Name: ")
student_homework = int(input("Homework Score /25: "))
student_assessment = int(input("Assessment Score /50: "))
student_final_exam = int(input("Final Exam Score /100: "))

def grade_program(homework_score, assessment_score, final_exam_score):
    if homework_score > 25 or assessment_score > 50 or final_exam_score > 100:
        return "Invalid Entry"
    score_total = homework_score + assessment_score + final_exam_score
    grade = (score_total / 175) * 100
    return grade




def grade_boundaries(percent_score):
    final_letter_grade = ""
    if percent_score > 90:
        final_letter_grade = "A"
    elif percent_score > 80:
        final_letter_grade = "B"
    elif percent_score > 70:
        final_letter_grade = "C"
    elif percent_score > 60:
        final_letter_grade = "D"
    else:
        final_letter_grade = "FAIL"
    return final_letter_grade    

grade = grade_program(student_homework, student_assessment, student_final_exam)
letter_grade = grade_boundaries(grade)

print(f"{student_name} got {grade}% which is a {letter_grade}")
