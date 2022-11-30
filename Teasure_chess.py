# 🚨 Don't change the code below 👇
row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

#Since the focus is for our output to display as a 3x3 square box using the print() given above; in that case we won't bother start indexing the positions from 'map' variable, we can just go straight inside it and use the 'rows' directly to index them.

  #First row
  if position == '11':
        row1[0] = 'X'
  elif position == '21':
        row1[1] = 'X'
  elif position == '31':
        row1[2] = 'X'
          #Second row
  elif position == '12':
        row2[0] = 'X'
  elif position == '22':
        row2[1] = 'X'
  elif position == '32':
        row2[2] = 'X'
          #Third row
  elif position == '13':
        row3[0] = 'X'
  elif position == '23':
        row3[1] = 'X'
  else:   #elif position == '33':
        row3[2] = 'X'

        #map = [row1, row2, row3] if placed here, the map variable will be updated but it won't display in a 3x3 square box if printed with the variable name 'map'.

        #Write your code above this row 👆

        # 🚨 Don't change the code below 👇
        print(f"{row1}\n{row2}\n{row3}")
