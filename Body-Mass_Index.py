'''
Write a program that interprets the Body Mass Index (BMI) based on a user's weight and height.

        BMI = weight(kg)/height^2(m^2)

It should tell them the interpretation of their BMI based on the BMI value.

* Under 18.5 they are underweight
* Over 18.5 but below 25 they have a normal weight
* Over 25 but below 30 they are slightly overweight
* Over 30 but below 35 they are obese
* Above 35 they are clinically obese.

Warning: You should round the result to the nearest whole number. The interpretation 
message needs to include the words in bold from the interpretations above. e.g. 
underweight, normal weight, overweight, obese, clinically obese.

The testing code will check for print output that is formatted like one of the lines below:
"Your BMI is 18, you are underweight."
"Your BMI is 22, you have a normal weight."
"Your BMI is 28, you are slightly overweight."
"Your BMI is 33, you are obese."
"Your BMI is 40, you are clinically obese." '''

height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")

#Lets type-cast both variables height and weight from the default str data type to float data type
user_weight = float(weight)
user_height = (float(height) ** 2) #float(height x height)

body_mass_index = (user_weight/user_height)

#the result must be rounded to an whole number
BMI = (round(body_mass_index))

#Result's interpretation
if BMI < 18.5:
      print(f"Your BMI is {BMI}, you are underweight.")
elif BMI > 18.5 and BMI < 25:
      print(f"Your BMI is {BMI}, you have a normal weight.")
elif BMI > 25 and BMI < 30:
      print(f"Your BMI is {BMI}, you are slightly overweight.")
elif BMI > 30 and BMI < 35:
      print(f"Your BMI is {BMI}, you are obese.")
else:
      print(f"Your BMI is {BMI}, you are clinically obese.")


######################################################
#Alternatively without needing the "and" operator
#Result's interpretation
if BMI < 18.5:
        print(f"Your BMI is {BMI}, you are underweight.")
elif BMI < 25:
        print(f"Your BMI is {BMI}, you have a normal weight.")
elif BMI < 30:
        print(f"Your BMI is {BMI}, you are slightly overweight.")
elif BMI < 35:
        print(f"Your BMI is {BMI}, you are obese.")
else:
        print(f"Your BMI is {BMI}, you are clinically obese.")

