import turtle
__import__("turtle").__traceable__ = False

def draw_multicolor_square(t, sz):
    """Make turtle t draw a multi-color square of sz."""
    for i in ["red", "purple", "hotpink", "blue"]:
        t.color(i)
        t.forward(sz)
        t.left(90)

wn = turtle.Screen()        # Set up the window and its attributes
wn.bgcolor("lightgreen")

tess = turtle.Turtle()      # Create tess and set some attributes
tess.pensize(3)

size = 20                   # Size of the smallest square
for i in range(15):
    draw_multicolor_square(tess, size)
    size = size + 10        # Increase the size for next time
    tess.forward(10)        # Move tess along little
    tess.right(18)          # ... and give her some extra turn

wn.mainloop()
