"""Semana Tec
Maria, Karin, Jesus
30 oct. 2020"""

from turtle import *
from random import randrange, randint, choice
from freegames import square, vector

# Vectors for the food and the snake
food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)
aim2 = vector(0,10)

# Added five new colors. Snake and food changes every round.
colors = ['lightcoral', 'lightsalmon', 'crimson', 'lightseagreen', 'darkslategrey']
color_snake = choice(colors)
color_food = choice(colors)
while color_food == color_snake:
    color_food = choice(colors)

# Creates state for snake to continue moving at all times
state = {'vel': 100}

def change(x, y):
    "Change snake direction."
    aim.x = x
    aim.y = y

def change2():
    ss=randint(1,4)

    if ss==1:
        aim2.x=0
        aim2.y=10
        return aim2

    elif ss==2:
        aim2.x=-10
        aim2.y=0
        return aim2

    elif ss==3:
        aim2.x=0
        aim2.y=-10
        return aim2

    elif ss==4:
        aim2.x=10
        aim2.y=0
        return aim2

def inside(head):
    "Return True if head inside boundaries."
    return -395 < head.x < 380 and -390 < head.y < 390

def move():
    "Move snake forward one segment."
    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)
    
    # Adds more body if the snakes eats food
    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)

    clear()

    # Changed color to a variable so it can change between rounds
    for body in snake:
        square(body.x, body.y, 9, color_snake)

    # Changed color to a variable so it can change between rounds
    square(food.x, food.y, 9, color_food)
    food.move(change2())
    update()
    
    # Change speed
    speed(state)

def speed(s):
    # When a certain key is clicked the snake can go faster
    ontimer(move, 100)
    if s == 1:
        ontimer(move, 0.5)
    elif s == 2:
        ontimer(move, 2)
    elif s == 3:
        ontimer(move, 4)

setup(800, 800, 370, 0)
hideturtle()
tracer(False)
listen()
# Arrows to move
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
# Keys to change speed
onkey(lambda: speed(1), '1')
onkey(lambda: speed(2), '2')
onkey(lambda: speed(3), '3')
move()
done()
