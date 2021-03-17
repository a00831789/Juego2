from turtle import *
from random import randrange
from freegames import square, vector

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)

#Possible colors for snake and fruit
colors = ['#0092fa', '#2ec742', '#000000', '#c72c79', '#f5814c']

#Random generation of colors for food and fruit
snake_color = colors[randrange(0, 5)]
food_color = colors[randrange(0,5)]

#Makes sure that the snake and the food have different color
while(snake_color == food_color):
    food_color = colors[randrange(0,5)]

def change(x, y):
    "Change snake direction."
    aim.x = x
    aim.y = y

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
        food.x = randrange(-18, 18) * 10
        food.y = randrange(-18, 18) * 10
    else:
        snake.pop(0)

    clear()

    for body in snake:

        square(body.x, body.y, 9, snake_color)

    square(food.x, food.y, 9, food_color)
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