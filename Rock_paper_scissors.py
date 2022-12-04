import random

print("#ROCK, PAPER AND SCISSORS GAME#\n")
pick = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors:\n")
pick = int(pick)

option_list = ["Rock", "Paper", "Scissors"]
len_option_list = len(option_list)
######
if pick == 0:
  print(
    '''
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)
    '''
  )
  print("Computer chose:")
  #option_list = ["Rock", "Paper", "Scissors"]
  #len_option_list = len(option_list)
  pc_pick = random.randint(0, len_option_list - 1)
  if pc_pick == 0:
    print(
    '''
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)
    '''
    )
    print("It's a draw!")
  elif pc_pick == 1:
    print(
    '''
        _______
    ---'   ____)____
              ______)
              _______)
             _______)
    ---.__________)
    '''
    )
    print("You lose!")
  else:
    print(
    '''
        _______
    ---'   ____)____
              ______)
           __________)
          (____)
    ---.__(___)
    '''
    )
    print("You win!")
    
########
elif pick == 1:
  print(
    '''
        _______
    ---'   ____)____
              ______)
              _______)
             _______)
    ---.__________)
    '''
    )
  print("Computer chose:")
  pc_pick = random.randint(0, len_option_list - 1)
  if pc_pick == 0:
    print(
    '''
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)
    '''
    )
    print("You win!")
  elif pc_pick == 1:
    print(
    '''
        _______
    ---'   ____)____
              ______)
              _______)
             _______)
    ---.__________)
    '''
    )
    print("It's a draw!")
  else:
    print(
    '''
        _______
    ---'   ____)____
              ______)
           __________)
          (____)
    ---.__(___)
    '''
    )
    print("You lose!")

##########
else:
  print(
    '''
        _______
    ---'   ____)____
              ______)
           __________)
          (____)
    ---.__(___)
    '''
  )
  print("Computer chose:")
  pc_pick = random.randint(0, len_option_list - 1)
  if pc_pick == 0:
    print(
    '''
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)
    '''
    )
    print("You lose!")
  elif pc_pick == 1:
    print(
    '''
        _______
    ---'   ____)____
              ______)
              _______)
             _______)
    ---.__________)
    '''
    )
    print("You win!")
  else:
    print(
    '''
        _______
    ---'   ____)____
              ______)
           __________)
          (____)
    ---.__(___)
    '''
    )
    print("It's a draw!")
