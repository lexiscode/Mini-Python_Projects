'''
Welcome to the PyPassword Generator!

How many letters would you like in your password?

How many numbers would you like?

How many symbols would you like?
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

for letter in range(user_letters): #range default is [0 - (user_letters - 1)], that is not including the user_letters.
  print(letters[letter], end="")
#print()

for number in range(user_numbers):
  print(numbers[number], end="")
#print()

for symbol in range(user_symbols):
  print(symbols[symbol], end="")
print() #This takes the cursor to a newline


#METHOD 2:

password_letters = ""
for letter in range(user_letters): #range default is [0 to (user_letters - 1)], that is not including the user_letters
  password_letters += letters[letter]
  #print(password_letters) this shows the for loop steps
#print(password_letters) this shows the full for loop output 

password_numbers = ""
for number in range(user_numbers):
  password_numbers += numbers[number]
#print(password_numbers)

password_symbol = ""
for symbol in range(user_symbols):
  password_symbol += symbols[symbol]
#print(password_symbol)
password = password_letters + password_numbers + password_symbol
print(password)
