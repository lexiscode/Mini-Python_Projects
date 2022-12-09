# THE HURDLE LOOP CHALLENGE
#URL: http://bit.ly/3VKuZ3S

'''
Reeborg has entered a hurdles race. Make him run the course, following the path shown.
What you need to know: The functions move() and turn_left().
You may have noticed that your solution has some repeated patterns. If you know how to define functions, 
define a function named robot_jump() and use it to simplify your program.
'''

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
    
    
############################################################################################


'''
Reeborg has entered a hurdle race, but he does not know in advance how long the race is. Make him run the course, 
following a path similar to the one shown, but stopping at the only flag that will be shown after the race has started.

What you need to know: The functions move() and turn_left().
                       The condition at_goal() and its negation.
                       How to use a while loop.
Your program should also be valid for world Hurdles 1 above.

The final required position of the robot will be chosen at random.
'''
while not at_goal():
    robot_jump()
    
#OR Alternatively
while at_goal() != True:
    robot_jump()









































