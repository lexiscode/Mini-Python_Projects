'''
Write a program that works out whether if a given year is a leap year. A normal year has
365 days, leap years have 366, with an extra day in February. The reason why we have leap 
years is really fascinating, this video does it more justice:

>> https://www.youtube.com/watch?v=xX96xng7sAE

This is how you work out whether if a particular year is a leap year:

on every year that is evenly divisible by 4

**except** every year that is evenly divisible by 100

**unless** the year is also evenly divisible by 400

e.g. The year 2000:

2000 ÷ 4 = 500 (Leap)

2000 ÷ 100 = 20 (Not Leap)

2000 ÷ 400 = 5 (Leap!)

So the year 2000 is a leap year.

But the year 2100 is not a leap year because:

2100 ÷ 4 = 525 (Leap)

2100 ÷ 100 = 21 (Not Leap)

2100 ÷ 400 = 5.25 (Not Leap)
'''
######################################################################################

#A year that is evenly divisible by 4 without remainder is a leap year
#except that year is also evenly divisible by 100, then it's no longer a leap year
#unless that same year is also evenly divisible by 400, then it is still a leap year


#Re-written:
#Leap year is TRUE: only when the year is evenly divisible by 4 and also 400 without a remainder

#Not leap year is TRUE: when the year is not evenly divisible by 4 AND/OR when the year is
#evenly divisible by 100 and not evenly divisible by 400


year_check = int(input("Which year do you want to check? "))

#All "leap year" MUST pass the first if condition;but not all "calendar year" must pass the
#first condition for it not to be a leap year.

if year_check % 4 == 0:
      #If both operands are TRUE, it is not a leap year. Look at the year 2100 example above.
      if year_check % 100 == 0 and year_check % 400 != 0:
              print("Not leap year.")
      #We need two if statements to be TRUE, and since the first if statement is TRUE, we will need one more True.
      #In bools, if at least one operand below is TRUE, then it is a leap year
      elif year_check % 100 !=0 or year_check % 400 == 0:
              print("Leap year.")
      #Below else prints out if neither of the above elif condition runs TRUE
      else:
              print("Not leap year.")
else:
#This happens when a year doesn't pass the first if condition
      print("Not leap year.")

#Test these years:
#Leap years: 2400, 2020. 1200
#Not leap years: 1989, 1999, 2100
##############################################################################3
#Alternatively, without using and operator

year = int(input("Which year do you want to check? "))

if year % 4 == 0:
      if year % 100 == 0:
            if year % 400 == 0:
                  print("Leap year.")
            else:
                  print("Not leap year.")
      else:
            print("Leap year.")
else:
      print("Not leap year.")
