import turtle

screen = turtle.Screen()
screen.bgcolor("lightblue")


p = turtle.Turtle()
p.color("black")  
p.pensize(4)    
p.speed(10)


def f(num):
    p.forward(num)

def r(num):
    p.right(num)

def l(num):
    p.left(num)

def g(num1,num2):
    p.penup()
    p.goto(num1,num2)
    p.pendown()

g(-420,-50)

#S
f(40)
for i in range(180):
    f(1)
    l(1)
for i in range(180):
    f(1)
    r(1)
f(40)

#Space
g(-270, -50)

#A
l(60)
f(265)
r(120)
f(265)
l(180)
f(132.5)
l(60)
f(135)
l(180)
f(135)
r(60)
f(132.5)
l(60)

#Space 
g(60,-50)
#R
l(90)
f(230)
r(90)
for i in range(225):
    f(0.875)
    r(0.8)
l(130)
f(135)

#Space
g(200,-50)
l(50)

#A
l(60)
f(265)
r(120)
f(265)
l(180)
f(132.5)
l(60)
f(135)
l(180)
f(135)
r(60)
f(132.5)
l(60)

turtle.update()
turtle.done()