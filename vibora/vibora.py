from turtle import *
from random import randrange
from freegames import square, vector

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)
colors = ['lightcoral', 'lightsalmon', 'crimson', 'lightseagreen', 'darkslategrey']
color_snake = random.choice(colors)
color_food = random.choice(colors)
while color_food == color_snake:
    color_food = random.choice(colors)

state = {'vel': 100}

def change(x, y):
    "Change snake direction."
    aim.x = x
    aim.y = y

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

    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)

    clear()

    for body in snake:
        square(body.x, body.y, 9, color_snake)

    square(food.x, food.y, 9, color_food)
    update()
    
    # Change speed
    speed(state)

def speed(s):
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
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
onkey(lambda: speed(1), '1')
onkey(lambda: speed(2), '2')
onkey(lambda: speed(3), '3')
move()
done()
