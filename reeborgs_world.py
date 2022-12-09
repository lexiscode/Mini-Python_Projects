# THE HURDLE LOOP CHALLENGE
#URL: http://bit.ly/3VKuZ3S

def turn_around():
    turn_left()
    turn_left()

def turn_right():
    turn_around()
    turn_left()
    
def robot_path():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
    
for i in range(6): #range(0,6) and #range(0,6,1)
    robot_path()
