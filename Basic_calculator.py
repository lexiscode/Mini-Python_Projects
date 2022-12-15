         _            _       _             
          | |          | |     | |            
  ___ __ _| | ___ _   _| | __ _| |_ ___  _ __ 
 / __/ _` | |/ __| | | | |/ _` | __/ _ \| '__|
| (_| (_| | | (__| |_| | | (_| | || (_) | |   
 \___\__,_|_|\___|\__,_|_|\__,_|\__\___/|_|   

from replit import clear
#from art import logo

def add(n1, n2):
  return n1 + n2

def subtract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1 / n2

operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
}

# we chose to create the calculator() function below for "recursion" purpose
# program can still run with or without it, it's only an added plus to the program - for starting afresh 
def calculator(): 
  #print(logo)

  num1 = float(input("What's the first number?: "))
  for symbol in operations:
    print(symbol)
      
  should_continue = True
  while should_continue:
    operation_symbol = input("Pick an operation: ")
    num2 = float(input("What's the next number?: "))
    # the values of the operations map are gotten below and stored in
    # the calculation_function variable
    calculation_function = operations[operation_symbol]
    # the above variable is stylishly converted to a function below, which is dependent on the values (i.e name) from the map
    # which the same name(s) were used as a function way above, then ( and ) were added to make it that function's replacement
    answer = calculation_function(num1, num2)
    print(f"{num1} {operation_symbol} {num2} = {answer}")

    if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ") == 'y':
      num1 = answer # updates the value of num1 to the last final result
    else:
      should_continue = False # stops the while loop
      clear() # replit function to clear the screen output
      calculator() # recursion, restarts the program

# the first call for all whole program to run
calculator() 
