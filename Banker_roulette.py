'''
You are going to write a program that will select a random name from a list of names. The person selected will have to pay for everybody's food bill.

Important: You are not allowed to use the choice() function.

Line 8 splits the string names_string into individual names and puts them inside a List called names. For this to work, you must enter all the names as names followed by comma then space. e.g. name, name, name

Example Input: Angela, Ben, Jenny, Michael, Chloe
Also notice that there is a space between the comma and the next name
Example Output: Michael is going to buy the mean today!

Hint: You might need the help of the len() function. Remember that Lists start at index 0!
'''

# Import the random module here
import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#print(names) == prints inputted lists

x = len(names) - 1
rand_name = names[random.randint(0,x)]
print(f"{rand_name} is going to buy the meal today!")

'''This method below won't work, so lesson learnt is that - place the randint() directly inside the names variable, dont create a separate variable to hold randint(), which u then now want to place that variable inside the names index

#rand_index = random.randint(0,x) 
#rand_name = names[rand_index])
#print(f"{rand_name}")
'''
