'''
Congratulations, you've got a job at Python Pizza. Your first job is to build an automatic pizza order program.

Based on a user's order, work out their final bill.

Small Pizza: $15

Medium Pizza: $20

Large Pizza: $25

Pepperoni for Small Pizza: +$2

Pepperoni for Medium or Large Pizza: +$3

Extra cheese for any size pizza: + $1
'''
########################################################################################

# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L: ")
add_pepperoni = input("Do you want pepperoni? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")
# 🚨 Don't change the code above 👆

#ALL CONDITIONS FOR A SMALL SIZED PIZZA
if size == 'S':
        bill = 15 #small pizza

        if add_pepperoni == 'Y': #He/She wants pepperoni
            bill += 2

            if extra_cheese == 'Y': #He/She wants extra cheese
                bill += 1
                print(f"Your final bill is: ${bill}")
            elif extra_cheese == 'N': #He/She doesn't want extra cheese
                print(f"Your final bill is: ${bill}")
            else:
                #Prints that if any input outside Y or N was mistakenly entered
                print("Incorrect input, try again!")

        elif add_pepperoni == 'N': #He/She doesn't want pepperoni

            if extra_cheese == 'Y': #He/She wants extra cheese
                bill += 1
                print(f"Your final bill is: ${bill}")
            elif extra_cheese == 'N': #He/She doesn't want extra cheese
                print(f"Your final bill is: ${bill}")
            else:
                #Prints that if any input outside Y or N was mistakenly entered
                print("Incorrect input, try again!")
        else:
            #Prints that if any input outside Y or N was mistakenly entered
            print("Incorrect input, try again!")

#ALL CONDITIONS FOR A MEDIUM SIZED PIZZA
elif size == 'M':
    bill = 20 #medium pizza
    if add_pepperoni == 'Y':
        bill += 3

        if extra_cheese == 'Y':
            bill += 1
            print(f"Your final bill is: ${bill}")
        elif extra_cheese == 'N':
            print(f"Your final bill is: ${bill}")
        else:
            print("Incorrect input, try again!")
    elif add_pepperoni == 'N':

        if extra_cheese == 'Y':
            bill += 1
            print(f"Your final bill is: ${bill}")
        elif extra_cheese == 'N':
            print(f"Your final bill is: ${bill}")
        else:
            print("Incorrect input, try again!")
    else:
        print("Incorrect input, try again!")

#ALL CONDITIONS FOR A LARGE SIZED PIZZA
elif size == 'L':
    bill = 25 #large pizza
    if add_pepperoni == 'Y':
        bill += 3

        if extra_cheese == 'Y':
            bill += 1
            print(f"Your final bill is: ${bill}")
        elif extra_cheese == 'N':
            print(f"Your final bill is: ${bill}")
        else:
            print("Incorrect input, try again!")
    elif add_pepperoni == 'N':

        if extra_cheese == 'Y':
            bill += 1
            print(f"Your final bill is: ${bill}")
        elif extra_cheese == 'N':
            print(f"Your final bill is: ${bill}")
        else:
            print("Incorrect input, try again!")
    else:
        print("Incorrect input, try again!")
else:
    #Prints that if input outside Y or N was inputted by mistake for the size of pizza
    print("Pizza size not available")
