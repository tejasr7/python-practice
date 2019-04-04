import turtle
from random import randrange
##
##def tree(branch_len, t):
##    if branch_len > 5:
##        t.forward(branch_len)
##        t.right(20)
##        tree(branch_len - 15, t)
##        t.left(40)
##        tree(branch_len - 15, t)
##        t.right(20)
##        t.backward(branch_len)
##
##
##def main():
##    t = turtle.Turtle()
##    wn = turtle.Screen()
##    wn.bgcolor('lightgreen')
##    t.left(90)
##    t.up()
##    t.backward(100)
##    t.down()
##    t.color('black')
##    tree(75, t)
##    wn.exitonclick()
##main()




def tree(branchLen,t, width=5, color="brown"):
    if branchLen > 5:
        t.width(width)
        t.color(color)
        t.forward(branchLen)
        t.right(20)
        tree(branchLen-15, t, width-1, "green")
        t.left(50)
        tree(branchLen-15, t, width-1)
        t.right(30)
        t.backward(branchLen)
            
t = turtle.Turtle()
myWin = turtle.Screen()
t.left(90)
t.up()
t.backward(300)
t.down()
tree(75,t)
myWin.exitonclick()
