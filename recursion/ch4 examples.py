from Stack import *

def to_str(n, base):
    """ Converting an string to an integer in any Base """
    convert_str = '0123456789ABCDEF'
    if n < base:
        return convert_str[n]
    else:
        return to_str(n // base, base) + convert_str[n % base]

##print(to_str(1454, 16))

############## Implementing recursion##########

r_stack = Stack()

def to_str(n, base):
    convert_str = '0123456789ABCDEF'
    while n > 0:
        if n < base:
            r_stack.push(convert_str[n])
        else:
            r_stack.push(convert_str[n % base])
        n = n // base
    res = ""
    while not r_stack.is_empty():
        res = res + str(r_stack.pop())
    return res

print(to_str(1453, 16))

###############################################



def reverse(s):
    """Write a function that takes a string as a parameter and returns a new
    string that is the reverse of the old string."""
    if len(s) == 1:
        return s
    return reverse(s[1:]) + s[0]

##
##print(reverse('hello'))
##print(reverse('tejas'))


def palindrome(s):
    """Write a function that takes a string as a parameter and returns True if
    the string is a palindrome, False otherwise. Remember that a string is a
    palindrome if it is spelled the same both forward and backward. For example:
    "radar" is a palindrome. for bonus points palindromes can also be phrases, but
    you need to remove the spaces and punctuation before checking. For example:
    "madam i’m adam" is a palindrome."""
    if len(s) <= 1:
        return True
    s = ''.join([i.lower() for i in s if i in letters])
    return s[0] == s[-1] and palindrome(s[1:-1])


### Fractal Tree###########
import turtle
from random import randrange

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
#####################################
