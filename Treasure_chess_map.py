'''
You are going to write a program that will mark a spot with an X.

In the starting code, you will find a variable called map.

This map contains a nested list. When map is printed this is what the nested list looks like:

[['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️']]

This is a bit hard to work with. So on lines 6 and 23, we've used this line of code print(f"{row1}\n{row2}\n{row3}" 
to format the 3 lists to be printed as a 3 by 3 square, each on a new line. 

['⬜️', '⬜️', '⬜️']

['⬜️', '⬜️', '⬜️']

['⬜️', '⬜️', '⬜️']

Now it looks a bit more like the 'coordinates' of a real map.

Your job is to write a program that allows you to mark a square on the map using a two-digit system:

The first digit in the input will specify the column (the position on the horizontal axis).
The second digit in the input will specify the row number (the position on the vertical axis). 

First, your program must take the user input and convert it to a usable format.
Next, you need to use that input to update your nested list with an "X". 
Remember that your nested list map actually looks like this: [['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️']]
'''

# 🚨 Don't change the code below 👇
row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

#Since the focus is for our output to display as a 3x3 square box using the print() given above; in that case
#we won't bother start indexing the positions from 'map' variable, we can just go straight inside the nested list and use the
#'rows'(i.e, row1, row2 and row30 directly to index them.

   #First row
if position == '11':    #column 1, row 1
    row1[0] = 'X'
elif position == '21':   #column2 , row 1
    row1[1] = 'X'
elif position == '31':   #column 3, row 1
    row1[2] = 'X'

    #Second row
elif position == '12':   #column 1, row 2
    row2[0] = 'X'
elif position == '22':   #column 2, row 2
    row2[1] = 'X'
elif position == '32':   #column 3, row 2
    row2[2] = 'X'

    #Third row
elif position == '13':   #column 1, row 3
    row3[0] = 'X'
elif position == '23':   #column 2, row 3
    row3[1] = 'X'
else:   #elif position == '33':    #column 2, row 3
    row3[2] = 'X'

#map = [row1, row2, row3] if placed here, the map variable will be updated but it won't display in a 3x3
#square box if printed with the variable name 'map'.

#Write your code above this row 👆
# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")
