#  REEBORG'S WORLD HURDLES and MAZE
# link:https://reeborg.ca/world.html

def move_around():
    turn_left()
    turn_left()


def turn_right():
    turn_left()
    move_around()


def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()


# CODE LOGIC FOR HURDLE 1
for i in range(6):
    jump()

# CODE LOGIC FOR HURDLE 2
while not at_goal():
    jump()


# CODE LOGIC FOR HURDLE 3
def wall_in_front_jump():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()


while not at_goal():
    if wall_in_front():
        wall_in_front_jump()
    elif front_is_clear():
        while not wall_in_front() and not at_goal():
            move()

# CODE LOGIC FOR HURDLE 4
while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif wall_in_front():
        turn_left()
    else:
        move()

# CODE LOGIC FOR MAZE
while not at_goal():
    if wall_in_front() and not right_is_clear():
        turn_left()

    elif wall_in_front() and right_is_clear():
        turn_right()

    # elif not wall_on_right():
    # turn_right()
    # move()
    else:
        move()







