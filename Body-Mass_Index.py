'''Write a program that calculates the Body Mass Index (BMI) from a user's weight and height.

The BMI is a measure of someone's weight taking into account their height. e.g. If a tall person and a
short person both weigh the same amount, the short person is usually more overweight.

BMI = weight(kg)/height^2(m^2)

Warning you should convert the result to a whole number. '''


# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

#Lets type-cast both variables height and weight from the default str data type to float data type
user_weight = float(weight)
user_height = (float(height) ** 2) #float(height x height)

body_mass_index = (user_weight/user_height)

#the result must be in a whole number, hence int type-casting
print(int(body_mass_index))
