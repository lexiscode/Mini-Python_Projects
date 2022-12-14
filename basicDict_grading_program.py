'''
You have access to a database of student_scores in the format of a dictionary. The keys in student_scores are the names 
of the students and the values are their exam scores.

Write a program that converts their scores to grades. By the end of your program, you should have a new dictionary called 
student_grades that should contain student names for keys and their grades for values. The final version of the student_grades dictionary will be checked.

This is the scoring criteria:

Scores 91 - 100: Grade = "Outstanding"
Scores 81 - 90: Grade = "Exceeds Expectations"
Scores 71 - 80: Grade = "Acceptable"
Scores 70 or lower: Grade = "Fail"

Expected Output:
'{'Harry': 'Exceeds Expectations', 'Ron': 'Acceptable', 'Hermione': 'Outstanding', 'Draco': 'Acceptable', 'Neville': 'Fail'}'
'''




student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}

student_grades = {}
# updating the values of student_scores dictionary
for values in student_scores:
    if student_scores[values] < 71:
        student_scores[values] = "Fail"
    elif student_scores[values] < 81:
        student_scores[values] = "Acceptable"
    elif student_scores[values] < 91:
        student_scores[values] = "Exceeds Expectations"
    elif student_scores[values] < 101:
        student_scores[values] = "Outstanding"

student_grades = student_scores

print(student_grades)
