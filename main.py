import turtle
turtle.Screen().bgcolor("green")
turtle.Screen().setup(300,400)

t =turtle.Turtle() 

for c in range (3):
    t.forward(100)
    t.left(120)
t.penup()
t.left(90)
t.forward(50)
t.right(90)
t.pendown()
for c in range (3):
    t.forward(100)
    t.right(120)

turtle.done