import turtle
wn = turtle.Screen()
wn.bgcolor("red")
wn.title("richie Turtle Run")

richie = turtle.Turtle()
richie.color("aqua")
richie.pensize(10)

for f in [richie.forward(50), richie.left(90), richie.forward(50), richie.left(90), richie.forward(50), richie.left(90), richie.forward(50),richie.left(90)]:
    square = richie
    print(square)

wn.mainloop
