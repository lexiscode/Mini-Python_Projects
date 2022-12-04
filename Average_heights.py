You are going to write a program that calculates the average student height from a List of heights. Remember to use the round() function to round the average height before you print it.

Important: You should not use the sum() or len() functions in your answer. You should try to replicate their functionality using what you have learnt about for loops.

# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()

#Converts each values on the "str list" to int list
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
'''
print(student_heights) to confirm the int list, notice no indentation is present which means the student_heights global variable value has been updated
'''
# 🚨 Don't change the code above 👆


#Without using the running sum() function, below is how it works
total_height = 0
for height in student_heights:
  total_height = total_height + height
'''
print(total_height)
'''

#Without using the len() function, below is how it works
no_of_students = 0
for student in student_heights:
  no_of_students = no_of_students + 1
'''
print(no_of_students)
'''

average_students = round(total_height/no_of_students)
print(average_students)


#########################
#ALTERNATIVELY, using sum() and len()

total_height = sum(student_heights)
no_of_students = len(student_heights)
average_students = round(total_height/no_of_students)
print(average_students)
