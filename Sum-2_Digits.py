# 🚨 Don't change the code below 👇
two_digit_number = input("Type a two digit number: ")
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇

#Convert the integer user-input by type-casting to a str data type
str_convert = str(two_digit_number)

#Assign different variables to index the above string
str_index1 = str(str_convert[0])
str_index2 = str(str_convert[1])

#Sum the two different variables while type-casting them back to int data type
sum_two_integers = int(str_index1) + int(str_index2)

print(sum_two_integers)
