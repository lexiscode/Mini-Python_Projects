'''
You are going to write a program that tests the compatibility between two people.

To work out the love score between two people:

Take both people's names and check for the number of times the letters in the word T R U E occurs. 

Then check for the number of times the letters in the word L O V E occurs. 

Then combine these numbers to make a 2 digit number.

For Love Scores less than 10 or greater than 90, the message should be:
"Your score is **x**, you go together like coke and mentos."

For Love Scores between 40 and 50, the message should be:
"Your score is **y**, you are alright together."

Otherwise, the message will just be their score. e.g.:
"Your score is **z**."

'''

print("Welcome to the Love Calculator!\n")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Force strings to be capitalized
name1 = name1.upper()
name2 = name2.upper()

#FIRST COLUMN
letter_T = name1.count('T') + name2.count('T')
letter_R = name1.count('R') + name2.count('R')
letter_U = name1.count('U') + name2.count('U')
letter_E1 = name1.count('E') + name2.count('E')
#Total Sum in First Column
first_cols_total = letter_T + letter_R + letter_U + letter_E1

#SECOND COLUMN
letter_L = name1.count('L') + name2.count('L')
letter_O = name1.count('O') + name2.count('O')
letter_V = name1.count('V') + name2.count('V')
letter_E2 = name1.count('E') + name2.count('E')
#Total Sum in Second Column
second_cols_total = letter_L + letter_O + letter_V + letter_E2

#The 'int' type casting below enables the if statements to run successfully without errors, because 'str' and 'int' can't be compared
love_score = int(str(first_cols_total) + str(second_cols_total))

if love_score < 10 or love_score > 90:
      print(f"\nYour score is {love_score}, you go together like coke and mentos.")
elif love_score >= 40 and love_score <= 50:
      print(f"\nYour score is {love_score}, you are alright together.")
else:
      print(f"\nYour score is {love_score}.")
