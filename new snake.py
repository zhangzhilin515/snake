import turtle
import copy
from random import randrange
snake = [[0, 0],[0, 10], [0, 20]]
aim = [0,10]
food = [-10,0]
def change_direction(x,y):
    aim[0] = x
    aim[1] = y
def square(x,y,size,color):
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.color(color)
    turtle.begin_fill()
    for i in range(4):
        turtle.forward(size)
        turtle.left(90)
    turtle.end_fill()
def snake_move():
    head = copy.deepcopy(snake[-1])
    head = [head[0]+aim[0],head[1]+aim[1]]
    if head==food:
        food[0] = randrange(-15, 15)*10
        food[1] = randrange(-15, 15) * 10
    else:
        snake.pop(0)
    snake.append(head)
    turtle.clear()
    square(food[0],food[1],10,"red")
    for body in snake:
      square(body[0],body[1],10,"black")
    turtle.update()
    turtle.ontimer(snake_move,300)
turtle.tracer(False)
turtle.hideturtle()
turtle.listen()
turtle.onkey(lambda :change_direction(0,10),"Up")
turtle.onkey(lambda :change_direction(0,-10),"Down")
turtle.onkey(lambda :change_direction(-10,0),"Left")
turtle.onkey(lambda :change_direction(10,0),"Right")
snake_move()
turtle.done()