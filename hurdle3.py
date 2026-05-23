def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
    
number_of_jump=6
while number_of_jump>0:
    jump()
    number_of_jump-=1
    print(number_of_jump)
