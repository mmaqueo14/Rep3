from turtle import *
from random import randrange, randint
from freegames import square, vector

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)
aim2 = vector(0,10)

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
    return -200 < head.x < 190 and -200 < head.y < 190

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
        square(body.x, body.y, 9, 'black')

    square(food.x, food.y, 9, 'green')
    food.move(change2())
    update()
    ontimer(move, 100)

setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
done()
