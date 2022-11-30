print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')


print("WELCOME TO TREASURE HUNT ISLAND\n")
print("Your mission is to find the Treasure Box.\n")
start_game = input(">> Type START to begin: ")
start_game = start_game.upper()
if start_game == 'START':
  print("\nLET'S GOO!!!\n\nYou have a choice to pass either the Left or the Right roads. The left road is a smooth surface road, whereas the right road is muddy and rough.\n")
  road1 = input(">> Type Left to pass the left OR Right to pass the right: ")
  road1 = road1.upper()
  if road1 == 'LEFT':
    print("\nYou've passed the left road. Oh shit mehn!...It is raining heavily there!!\n")
    left_option1 = input(">> Take an Umbrella or Rain Coat: ")
    left_option1 = left_option1.upper()
    if left_option1 == 'UMBRELLA':
      print("\nArrgh!! An heavy wind has blew it away, you're now beaten by the rain and feeling sick.\n But now, there's a house facing you and also another road path.\nThere are horny girls/boys in the house and also some drugs in case of illness.\nMeanwhile on the road path, there's a very angry toothless lion waiting for you.\n")
      left_option2 = input(">> Type House to enter OR Road to pass: ")
      left_option2 = left_option2.upper()
      if left_option2 == 'HOUSE':
        print("\nHot Girl: 'Sweetie if you will love to enter our romantic/horny house there's a condition: you must sleep with at least 3 persons there, we will then also give you drugs for free.\n")
        left_option3 = input(">> If you love the proposal, type Yes, but if not, type No: ")
        left_option3 = left_option3.upper()
        if left_option3 == 'YES':
          print("\nOops! you're dead. They stabbed you while making love and used your head for money rituals! Lol\nEND!\n")
        else:
          print("\nOops! You're dead. Your illness killed you.\nEND!\n")
      else:
        print("\nYou passed the road. A toothless lion can't bite you.\nNow, you have a river to cross.\n")
        left_option4 = input(">> Type Swim to swim OR Boat to use a boat: ")
        left_option4 = left_option4.upper()
        if left_option4 == 'SWIM':
          print("\nArrgh, help!!!... You've been killed by a crocodile!\nEND!\n")
        else:
          #######################################
          #UPDATED INDENT-REAL BEGINNING PATH (skipped the crossing river part of the real beginning)
            print("\nYou've arrived at the other side of the river. Now there are two turns, on the left path there are money sprayed on the floor and also heads of goats around; on the right path there is an angry Python that hasn't eaten for 12 months.\n")
            right_option2 = input(">> Type Left to move left OR Right to move right: ")
            right_option2 = right_option2.upper()
            if right_option2 == 'LEFT':
              print("\nNow you're walking on the left path. Do you wish to pick some money on the floor?\n")
              right_option3 == input(">> Type Yes to pick or No to not pick: ")
              right_option3 = right_option3.upper()
              if right_option3 == 'YES':
                print("\nYou're dead, you've turned to goat head - just as the heads you've been seeing on the road. You've joined them.\nEND!\n")
              else:
                ###Copied
                print("\nNow, there are two tunnels facing you and you need to enter one. One is 'dark' and the other has lamps for 'light'\n")
              right_option4 == input(">> Type Dark to enter the dark tunnel OR Light to enter the light tunnel: ")
              right_option4 = right_option4.upper()
              if right_option4 == 'LIGHT':
                print("\nYou stormed across cultists having their meeting in that tunnel, then they gave you an option to either join them by force or that you should donate a small portion of your blood then they will let you go and show you the path to the Treasure box.\n")
                right_option5 == input(">> Type Join to be part of them OR Donate to be free from them and be informed about the Treasure box: ")
                right_option5 = right_option5.upper()
                if right_option5 == 'JOIN':
                  print("You are now a cultist and in a bondage being with them always in that tunnel.\nEND!\n")
                else:
                  print("\nYou've been shown where the Treasure Box lay!\nTo open it, you need to pass a riddle, if you fail the riddle the mystery treasure box will kill you right there: 'Who gives something good with a right hand and collects it back after with a left hand'\n")
                right_option6 == input(">> Enter your answer: ")
                right_option6 = right_option6.upper()
                if right_option6 == 'SATAN' or 'DEVIL':
                  print("\nWOW!!!! CONGRATULATIONS!! YOU NOW OWN THE TREASURES!!!\nBut sadly, you won't be able to live to enjoy it because you've been killed in the realm of the Spirit by those cultists when you donated your blood.\nEND!\n")
                else:
                  print("Wrong! You're dead.")
 
              else:
                print("\nYou are courageous. You've seen where the Treasure Box lay!\nTo open it, you need to pass a riddle, if you fail the riddle the mystery treasure box will kill you right there: 'When you have me more, you can see only less. What Am I?'\n")
                right_option7 == input(">> Enter your answer: ")
                right_option7 = right_option7.upper()
                if right_option7 == 'DARKNESS' or 'DARK':
                  print("\nWOW!!!! CONGRATULATIONS!! YOU NOW OWN THE TREASURES!!!\n")
                else:
                  print("Wrong! You're dead.")
                ###
            else:
              print("\nPython that hasn't eaten for 12 months is long dead. You are safe. But now, there are two tunnels facing you and you need to enter one. One is 'dark' and the other has lamps for 'light'\n")
              right_option8 == input(">> Type Dark to enter the dark tunnel OR Light to enter the light tunnel: ")
              right_option8 = right_option8.upper()
              if right_option8 == 'LIGHT':
                print("\nYou stormed across cultists having their meeting in that tunnel, then they gave you an option to either join them by force or that you should donate a small portion of your blood then they will let you go and show you the path to the treasure box\n")
                right_option9 == input(">> Type Join to be part of them OR Donate to be free from them and be informed about the Treasure box: ")
                right_option9 = right_option9.upper()
                if right_option9 == 'JOIN':
                  print("\nYou are now a cultist and in a bondage being with them always in that tunnel.\nEND!\n")
                else:
                  print("\nYou've been shown where the Treasure Box lay!\nTo open it, you need to pass a riddle, if you fail the riddle the mystery treasure box will kill you right there: 'Who gives something good with a right hand and collects it back after with a left hand'\n")
                right_option10 == input(">> Enter your answer: ")
                right_option10 = right_option10.upper()
                if right_option10 == 'SATAN' or 'DEVIL':
                  print("\nWOW!!!! CONGRATULATIONS!! YOU NOW OWN THE TREASURES!!!\nBut sadly, you won't be able to live to enjoy it because you've been killed in the realm of the Spirit by those cultists when you donated your blood.\nEND!\n")
                else:
                  print("Wrong! You're dead.")
 
              else:
                print("\nYou are courageous. You've seen where the Treasure Box lay!\nTo open it, you need to pass a riddle, if you fail the riddle the mystery treasure box will kill you right there: 'When you have me more, you can see only less. What Am I?'\n")
                right_option11 == input(">> Enter your answer: ")
                right_option11 = right_option7.upper()
                if right_option11 == 'DARKNESS' or 'DARK':
                   print("\nWOW!!!! CONGRATULATIONS!! YOU NOW OWN THE TREASURES!!!\n")
                else:
                  print("\nWrong! You're dead.\n")
          
          ######################################
   
    else:
      print("\nThere's a house facing you and also another road path.\nThere are horny girls/boys in the house.\nMeanwhile on the road path, there's a very angry toothless lion waiting for you.\n")
      left_option5 = input(">> Type House to enter OR Road to pass: ")
      left_option5 = left_option5.upper()
      if left_option5 == 'HOUSE':
        print("\nHot Girl: 'Hi Sweetie, you look sexy but if you will love to enter our horny house there's a condition: you must sleep with at least 3 persons there.\n")
        left_option6 = input(">> If you love the proposal, type Yes, but if not, type No: ")
        left_option6 = left_option6.upper()
        if left_option6 == 'YES':
          print("\nOops! you're dead. They stabbed you while making love and used your head for money rituals! Lol\nEND!\n")
        else:
          print("\nOops! You're dead - being stuck outside the house for weeks without making progress nor food for weeks.\nEND!\n")
      else:
        print("\nYou passed the road. A toothless lion can't bite you.\nNow, you have a river to cross.\n")
        left_option7 = input(">> Type Swim to swim OR Boat to use a boat: ")
        left_option7 = left_option7.upper()
        if left_option7 == 'SWIM':
          print("\nArrgh, help!!!... You've been killed by a crocodile!\nEND!\n")
        else:
          #copied-BEGINNINGRIGHT PATH
          print("\nYou've passed the right road. The weather is sunny.\nNow there's a river, how would you like to cross it?\n")
          right_option1 = input(">> Type Swim to swim OR Boat to use a boat: ")
          right_option1 = right_option1.upper()
          if right_option1 == 'SWIM':
            print("\nArrgh, help!!!... You've been killed by a crocodile!\nEND!\n")
          else:
            print("\nYou've arrived at the other side of the river. Now there are two turns, on the left path there are money sprayed on the floor and also heads of goats around; on the right path there is an angry Python that hasn't eaten for 12 months.\n")
            right_option2 = input(">> Type Left to move left OR Right to move right: ")
            right_option2 = right_option2.upper()
            if right_option2 == 'LEFT':
              print("\nNow you're walking on the left path. Do you wish to pick some money on the floor?\n")
              right_option3 == input(">> Type Yes to pick or No to not pick: ")
              right_option3 = right_option3.upper()
              if right_option3 == 'YES':
                print("\nYou're dead, you've turned to goat head - just as the heads you've been seeing on the road. You've joined them.\nEND!\n")
              else:
                ###Copied
                print("\nNow, there are two tunnels facing you and you need to enter one. One is 'dark' and the other has lamps for 'light'\n")
              right_option4 == input(">> Type Dark to enter the dark tunnel OR Light to enter the light tunnel: ")
              right_option4 = right_option4.upper()
              if right_option4 == 'LIGHT':
                print("\nYou stormed across cultists having their meeting in that tunnel, then they gave you an option to either join them by force or that you should donate a small portion of your blood then they will let you go and show you the path to the Treasure box.\n")
                right_option5 == input(">> Type Join to be part of them OR Donate to be free from them and be informed about the Treasure box: ")
                right_option5 = right_option5.upper()
                if right_option5 == 'JOIN':
                  print("\nYou are now a cultist and in a bondage being with them always in that tunnel.\nEND!\n")
                else:
                  print("\nYou've been shown where the Treasure Box lay!\nTo open it, you need to pass a riddle, if you fail the riddle the mystery treasure box will kill you right there: 'Who gives something good with a right hand and collects it back after with a left hand'\n")
                right_option6 == input(">> Enter your answer: ")
                right_option6 = right_option6.upper()
                if right_option6 == 'SATAN' or 'DEVIL':
                  print("\nWOW!!!! CONGRATULATIONS!! YOU NOW OWN THE TREASURES!!!\nBut sadly, you won't be able to live to enjoy it because you've been killed in the realm of the Spirit by those cultists when you donated your blood.\nEND!\n")
                else:
                  print("\nWrong! You're dead.\n")
 
              else:
                print("\nYou are courageous. You've seen where the Treasure Box lay!\nTo open it, you need to pass a riddle, if you fail the riddle the mystery treasure box will kill you right there: 'When you have me more, you can see only less. What Am I?'\n")
                right_option7 == input(">> Enter your answer: ")
                right_option7 = right_option7.upper()
                if right_option7 == 'DARKNESS' or 'DARK':
                  print("\nWOW!!!! CONGRATULATIONS!! YOU NOW OWN THE TREASURES!!!\n")
                else:
                  print("\nWrong! You're dead.\n")
                ###
            else:
              print("\nPython that hasn't eaten for 12 months is long dead. You are safe. But now, there are two tunnels facing you and you need to enter one. One is 'dark' and the other has lamps for 'light'\n")
              right_option8 == input(">> Type Dark to enter the dark tunnel OR Light to enter the light tunnel: ")
              right_option8 = right_option8.upper()
              if right_option8 == 'LIGHT':
                print("\nYou stormed across cultists having their meeting in that tunnel, then they gave you an option to either join them by force or that you should donate a small portion of your blood then they will let you go and show you the path to the treasure box\n")
                right_option9 == input(">> Type Join to be part of them OR Donate to be free from them and be informed about the Treasure box:")
                right_option9 = right_option9.upper()
                if right_option9 == 'JOIN':
                  print("\nYou are now a cultist and in a bondage being with them always in that tunnel.\nEND!\n")
                else:
                  print("\nYou've been shown where the Treasure Box lay!\nTo open it, you need to pass a riddle, if you fail the riddle the mystery treasure box will kill you right there: 'Who gives something good with a right hand and collects it back after with a left hand'\n")
                right_option10 == input(">> Enter your answer: ")
                right_option10 = right_option10.upper()
                if right_option10 == 'SATAN' or 'DEVIL':
                  print("\nWOW!!!! CONGRATULATIONS!! YOU NOW OWN THE TREASURES!!!\nBut sadly, you won't be able to live to enjoy it because you've been killed in the realm of the Spirit by those cultists when you donated your blood.\nEND!\n")
                else:
                  print("\nWrong! You're dead.\n")
 
              else:
                print("\nYou are courageous. You've seen where the Treasure Box lay!\nTo open it, you need to pass a riddle, if you fail the riddle the mystery treasure box will kill you right there: 'When you have me more, you can see only less. What Am I?'\n")
                right_option11 == input(">> Enter your answer: ")
                right_option11 = right_option7.upper()
                if right_option11 == 'DARKNESS' or 'DARK':
                   print("\nWOW!!!! CONGRATULATIONS!! YOU NOW OWN THE TREASURES!!!\n")
                else:
                  print("\nWrong! You're dead.\n")
                #####

  else:
    #UPDATED INDENT-REAL BEGINNING PATH
    print("\nYou've passed the right road. The weather is sunny.\nNow there's a river, how would you like to cross it?\n")
    right_option1 = input(">> Type Swim to swim OR Boat to use a boat: ")
    right_option1 = right_option1.upper()
    if right_option1 == 'SWIM':
      print("\nArrgh, help!!!... You've been killed by a crocodile!\nEND!\n")
    else:
      print("\nYou've arrived at the other side of the river. Now there are two turns, on the left path there are money sprayed on the floor and also heads of goats around; on the right path there is an angry Python that hasn't eaten for 12 months.\n")
      right_option2 = input(">> Type Left to move left OR Right to move right: ")
      right_option2 = right_option2.upper()
      if right_option2 == 'LEFT':
        print("\nNow you're walking on the left path. Do you wish to pick some money on the floor?\n")
        right_option3 == input(">> Type Yes to pick or No to not pick: ")
        right_option3 = right_option3.upper()
        if right_option3 == 'YES':
          print("\nYou're dead, you've turned to goat head - just as the heads you've been seeing on the road. You've joined them.\n END!\n")
        else:
          ###Copied
          print("\nNow, there are two tunnels facing you and you need to enter one. One is 'dark' and the other has lamps for 'light'\n")
          right_option4 == input(">> Type Dark to enter the dark tunnel OR Light to enter the light tunnel: ")
          right_option4 = right_option4.upper()
          if right_option4 == 'LIGHT':
            print("\nYou stormed across cultists having their meeting in that tunnel, then they gave you an option to either join them by force or that you should donate a small portion of your blood then they will let you go and show you the path to the Treasure box\n")
            right_option5 == input(">> Type Join to be part of them OR Donate to be free from them and be informed about the Treasure box: ")
            right_option5 = right_option5.upper()
            if right_option5 == 'JOIN':
              print("\nYou are now a cultist and in a bondage being with them always in that tunnel.\nEND!\n")
            else:
              print("\nYou've been shown where the Treasure Box lay!\nTo open it, you need to pass a riddle, if you fail the riddle the mystery treasure box will kill you right there: 'Who gives something good with a right hand and collects it back after with a left hand'\n")
              right_option6 == input(">> Enter your answer: ")
              right_option6 = right_option6.upper()
              if right_option6 == 'SATAN' or 'DEVIL':
                print("\nWOW!!!! CONGRATULATIONS!! YOU NOW OWN THE TREASURES!!!\nBut sadly, you won't be able to live to enjoy it because you've been killed in the realm of the Spirit by those cultists when you donated your blood.\nEND!\n")
              else:
                print("\nWrong! You're dead.\n")
              
          else:
            print("\nYou are courageous. You've seen where the Treasure Box lay!\nTo open it, you need to pass a riddle, if you fail the riddle the mystery treasure box will kill you right there: 'When you have me more, you can see only less. What Am I?'\n")
            right_option7 == input(">> Enter your answer: ")
            right_option7 = right_option7.upper()
            if right_option7 == 'DARKNESS' or 'DARK':
              print("\nWOW!!!! CONGRATULATIONS!! YOU NOW OWN THE TREASURES!!!\n")
            else:
              print("\nWrong! You're dead.\n")
            ###
          
      else:
        print("\nPython that hasn't eaten for 12 months is long dead. You are safe. But now, there are two tunnels facing you and you need to enter one. One is 'dark' and the other has lamps for 'light'\n")
        right_option8 == input(">> Type Dark to enter the dark tunnel OR Light to enter the light tunnel: ")
        right_option8 = right_option8.upper()
        if right_option8 == 'LIGHT':
          print("\nYou stormed across cultists having their meeting in that tunnel, then they gave you an option to either join them by force or that you should donate a small portion of your blood then they will let you go and show you the path to the Treasure box\n")
          right_option9 == input(">> Type Join to be part of them OR Donate to be free from them and be informed about the Treasure box: ")
          right_option9 = right_option9.upper()
          if right_option9 == 'JOIN':
            print("\nYou are now a cultist and in a bondage being with them always in that tunnel.\nEND!\n")
          else:
            print("\nYou've been shown where the Treasure Box lay!\nTo open it, you need to pass a riddle, if you fail the riddle the mystery treasure box will kill you right there: 'Who gives something good with a right hand and collects it back after with a left hand'\n")
            right_option10 == input(">> Enter your answer: ")
            right_option10 = right_option10.upper()
            if right_option10 == 'SATAN' or 'DEVIL':
              print("\nWOW!!!! CONGRATULATIONS!! YOU NOW OWN THE TREASURES!!!\nBut sadly, you won't be able to live to enjoy it because you've been killed in the realm of the Spirit by those cultists when you donated your blood.\nEND!\n")
            else:
              print("\nWrong! You're dead.\n")
        else:
          print("\nYou are courageous. You've seen where the Treasure Box lay!\nTo open it, you need to pass a riddle, if you fail the riddle the mystery treasure box will kill you right there: 'When you have me more, you can see only less. What Am I?'\n")
          right_option11 == input(">> Enter your answer: ")
          right_option11 = right_option7.upper()
          if right_option11 == 'DARKNESS' or 'DARK':
            print("\nWOW!!!! CONGRATULATIONS!! YOU NOW OWN THE TREASURES!!!\n")
          else:
            print("\nWrong! You're dead.\n")
