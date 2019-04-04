import turtle

def drawSpiral(t, angle):
    ''' takes a turtle, t, and an angle in degrees '''
    length = 1
    for i in range(84):
        t.forward(length)
        t.right(angle)
        length = length + 2


wn = turtle.Screen()       # Set up the window and its attributes
wn.bgcolor("lightgreen")

guido = turtle.Turtle()    # create guido
guido.color('blue')

## draw the first spiral ##
# position guido
guido.penup()
guido.backward(110)
guido.pendown()

# draw the spiral using a 90 degree turn angle
drawSpiral(guido, 90)


## draw the second spiral ##
# position guido
guido.penup()
guido.home()
guido.forward(90)
guido.pendown()

drawSpiral(guido, 89)

wn.exitonclick()
