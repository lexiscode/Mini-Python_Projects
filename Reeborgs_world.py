# THE HURDLE LOOP CHALLENGE
#URL: http://bit.ly/3VKuZ3S

def turn_around():
    turn_left()
    turn_left()

def turn_right():
    turn_around()
    turn_left()
    
def robot_jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
    
#Below we can either use the For loop or the While loop
#Using For loop
for i in range(6): #range(0,6) and #range(0,6,1)
    robot_path()

#Using While loop (1)
number_of_hurdles = 1
while number_of_hurdles <= 6:
    robot_path()
    number_of_hurdles += 1

#Using While loop (2)
number_of_hurdles = 6
while number_of_hurdles > 0:
    robot_path()
    number_of_hurdles -= 1
