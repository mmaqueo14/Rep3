"""Paint, for drawing shapes.
Maria, Jesús, Karin

Exercises

1. Add a color.
2. Complete circle.
3. Complete rectangle.
4. Complete triangle.
5. Add width parameter.

"""

from turtle import *
from freegames import vector
import math

def line(start, end):
    "Draw line from start to end."
    # Lifts pencil, goes to point and then place pencil down to go to next point
    up()
    goto(start.x, start.y)
    down()
    goto(end.x, end.y)

def square(start, end):
    "Draw square from start to end."
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    # Creates equal sides of square
    for count in range(4):
        forward(end.x - start.x)
        left(90)

    end_fill()

def circle_(start, end):
    "Draw circle from start to end."
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    # Creates and fills circle with a radius of the difference of x
    circle(end.x - start.x)

    end_fill()
    
def rectangle(start, end):
    "Draw rectangle from start to end."
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    # Creates sides of rectangle
    for count in range(2):
        forward(end.x - start.x)
        left(90)
        forward(end.y - start.y)
        left(90)

    end_fill()

def triangle(start, end):
    "Draw triangle from start to end."
    up()
    goto(start.x,start.y)
    down()
    begin_fill()
    
    # Creates an equilateral triangle
    forward(end.x - start.x)
    left(120)
    forward(end.x - start.x)
    left(120)
    forward(end.x - start.x)
    
    end_fill()

def tap(x, y):

    "Store starting point or draw shape."
    start = state['start']

    if start is None:
        state['start'] = vector(x, y)
    else:
        shape = state['shape']
        end = vector(x, y)
        shape(start, end)
        state['start'] = None

def store(key, value):
    "Store value in state at key."
    state[key] = value

# Dictionary to indicate state
state = {'start': None, 'shape': line}

# CAnvas where drawing takes place
setup(600, 600, 500, 0)

onscreenclick(tap)
listen()

# Keys where colors and types of shape will be specified
onkey(undo, 'u')
onkey(clear, 'e')
onkey(lambda: color('black'), 'K')
onkey(lambda: color('white'), 'W')
onkey(lambda: color('green'), 'G')
onkey(lambda: color('blue'), 'B')
onkey(lambda: color('red'), 'R')
onkey(lambda: color('turquoise'), 'T')
onkey(lambda: width(10), 'W')
onkey(lambda: width(1), 'w')
onkey(lambda: shape('classic'), 'C')
onkey(lambda: shape('turtle'), 'O')
onkey(lambda: color('hotpink'), 'P')
onkey(lambda: store('shape', line), 'l')
onkey(lambda: store('shape', square), 's')
onkey(lambda: store('shape', circle_), 'c')
onkey(lambda: store('shape', rectangle), 'r')
onkey(lambda: store('shape', triangle), 't')
done()
