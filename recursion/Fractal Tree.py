import turtle

def tree(branch_len, t):
    if branch_len > 5:
        t.forward(branch_len)
        t.right(20)
        tree(branch_len - 15, t)
        t.left(40)
        tree(branch_len - 15, t)
        t.right(20)
        t.backward(branch_len)


def main():
    t = turtle.Turtle()
    wn = turtle.Screen()
    wn.bgcolor('lightgreen')
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    t.color('black')
    tree(75, t)
    wn.exitonclick()
main()
