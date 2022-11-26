'''Create a program using maths and f-Strings that tells us how many days, weeks, months we have left
if we live until 90 years old.

It will take your current age as the input and output a message with our time left in this format:

You have x days, y weeks, and z months left.

Where x, y and z are replaced with the actual calculated numbers.

Warning your output should match the Example Output format exactly, even the positions of the commas
and full stops.'''


# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

#Seasons (Time) Conversion
#1 year = 12 months = 52 weeks = 365 days (recommended)

#Months calculation breakdown
year_in_months = 90 * 12
user_year_in_months = int(age) * 12
z = year_in_months - user_year_in_months

#Weeks calculation breakdown
year_in_weeks = 90 * 52
user_year_in_weeks = int(age) * 52
y = year_in_weeks - user_year_in_weeks

#Days calculation breakdown
year_in_days = 90 * 365
user_year_in_days = int(age) * 365
x = year_in_days - user_year_in_days

print(f"You have {x} days, {y} weeks, and {z} months left.")


####################################################################################################
#ANOTHER METHOD

# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

years_remaining = 90 - int(age)

z = years_remaining * 12
y = years_remaining * 52
x = years_remaining * 365

message = f"You have {x} days, {y} weeks, and {z} months left."
print(message)
