'''
You are going to write a program that calculates the sum of all the even numbers from 1 to 100.
Thus, the first even number would be 2 and the last one is 100:

i.e. 2 + 4 + 6 + 8 +10 ... + 98 + 100

Important, there should only be 1 print statement in your console output. It should just print the final total and not every step of the calculation.
'''

#Write your code below this row 👇

add_even_no = 0
for even in range(0,101,2):  #2 steps
    add_even_no += even

print(add_even_no)


#####################################################################################

##Running Sum of numbers from 1-100##

add_num = 0
for num in range(0,101): #range(0,101,1) by default one step
  add_num += num
print(add_num)

#ORRR

#Creating a list of numbers from 1-100 using range() and list() constructor
numbers = list(range(1,101)) 
#Sum of numbers from 1-100
add_num = 0
for number in numbers:
  add_num ++ number
print(add_num)
