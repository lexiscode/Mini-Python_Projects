''' A group of friends or colleagues went out to a resturant, and when they are done they went to
the cashier to make their payments. Write a program which requests for their total bill, an optional
percentage tip (10, 12 or 15), and the actual number of individual group of friends/colleagues.
Then the program prints out the bill each person should pay.

Extra: The format of the result should be strictly in 2 decimal place
'''


print("Welcome to the Tip Calculator.\n")

total_bill = input("What was the total bill? $")
tip_percent = input("What percentage tip would you like to give? 10, 12 or 15? ")
bill_split = input("How many people to split the bill? ")

#Calculate the tip amount
tip_amount = (float(tip_percent)/100) * float(total_bill)

#Cummulate the total bill and tip amount
cummulative_bill = float(total_bill) + tip_amount

#Each person pays this charge below
charge_per_person = cummulative_bill/float(bill_split)

#The round() isn't used here because it won't always print the result in exact 2 d.p when there's a leading zero
#Inserting floats within a string is the best option and forces it to print in exact 2 d.p
bill = "%.2f" % (charge_per_person)
#OR bill = "{:.2f}".format(charge_per_person) 

print("\nEach person should pay: $" + bill)

#OR print(f"Each person should pay: ${bill}")
