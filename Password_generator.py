'''
Welcome to the PyPassword Generator!

How many letters would you like in your password?

How many numbers would you like?

How many symbols would you like?
'''

#MY FIRST METHOD TRY
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 
'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 
'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!\n")
random.shuffle(letters)
random.shuffle(numbers)
random.shuffle(symbols)
#print(letters), print(numbers) and print(symbols) values are updated in a frequent shuffled manner
user_letters = int(input("How many letters would you like in your password?\n"))
user_numbers = int(input("How many numbers would you like?\n"))
user_symbols = int(input("How many symbols would you like?\n"))

print("\nGenerated Password:")

for letter in range(user_letters): #range default is [0 to (user_letters - 1)], that is not including the user_letters.
  print(letters[letter], end="") #A way to print out for loop in a single (horizontal) line, an alternative way is used in method 2 below
#print() This takes the position of the cursor to the nextline

for number in range(user_numbers):
  print(numbers[number], end="")
#print()

for symbol in range(user_symbols):
  print(symbols[symbol], end="")
print()

#Now the above method only works when don't intend to randomize combined printted outputs. That means it's a bit limited.




#METHOD 2:

import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 
'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 
'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!\n")
random.shuffle(letters)
random.shuffle(numbers)
random.shuffle(symbols)
#print(letters), print(numbers) and print(symbols) values are updated in a frequent shuffled manner
user_letters = int(input("How many letters would you like in your password?\n"))
user_numbers = int(input("How many numbers would you like?\n"))
user_symbols = int(input("How many symbols would you like?\n"))

print("\nGenerated Password:")

password_letters = "" #we can use [] instead of "" if we want the outputs to be in list format rather than strings format, jsyk
for letter in range(user_letters): #range default is [0 to (user_letters - 1)], that is not including the user_letters
  password_letters += letters[letter]  
  #print(password_letters) this shows the for loop steps
#print(password_letters) this shows the full for loop output, also in single (horizontal) line

password_numbers = ""
for number in range(user_numbers):
  password_numbers += numbers[number]
#print(password_numbers)

password_symbol = ""
for symbol in range(user_symbols):
  password_symbol += symbols[symbol]
#print(password_symbol)
password = password_letters + password_numbers + password_symbol #strings addition
print(password)

#Now the above is an alternative way of still doing the same thing which Method 1 does, the difference is that we are about to 
#make the result of the for loop be stored in a global variable (password_numbers,_symbols,and _letters), which we then used to sum


################################################################################################################
'''
NOW, say, we want out password generator output to be in a scattered manner (rather than arranged order) between numbers, symbols and 
letters in order to make it harder to be guessed by hackers and increasing it's strongest/security.
'''

import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 
'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 
'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!\n")
random.shuffle(letters)
random.shuffle(numbers)
random.shuffle(symbols)
#print(letters), print(numbers) and print(symbols) values are updated in a frequent shuffled manner
user_letters = int(input("How many letters would you like in your password?\n"))
user_numbers = int(input("How many numbers would you like?\n"))
user_symbols = int(input("How many symbols would you like?\n"))

print("\nGenerated Password:")

password_letters = ""
for letter in range(user_letters): #range default is [0 to (user_letters - 1)], that is not including the user_letters
  password_letters += letters[letter]  
  #print(password_letters) this shows the for loop steps
#print(password_letters) this ptint the full for loop output, also in single (horizontal) line, an alternative method to the previous one above

password_numbers = ""
for number in range(user_numbers):
  password_numbers += numbers[number]
#print(password_numbers)

password_symbol = ""
for symbol in range(user_symbols):
  password_symbol += symbols[symbol]
#print(password_symbol)
password = password_letters + password_numbers + password_symbol   #strings addition

###Added features

#We will have to first convert our combinded strings into lists then shuffle it again
strings_to_list = [i for i in password]
#print(strings_to_list)
random.shuffle(strings_to_list)
#print(strings_to_list)
length_new_list = len(strings_to_list)

rand_strings = ''
for list in range(length_new_list):
  rand_strings += strings_to_list[list]
print(rand_strings)

