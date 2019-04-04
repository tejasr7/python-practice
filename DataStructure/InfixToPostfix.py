from Stack import *

class Stack:
    
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)


def infix_to_postfix(infix_expr):
    prec = {}
    prec['^'] = 4
    prec['*'] = 3
    prec['/'] = 3
    prec['+'] = 2
    prec['-'] = 2
    prec['('] = 1
    op_stack = Stack()
    postfix_list = []
    token_list = infix_expr.split()

    for token in token_list:
      if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":
         postfix_list.append(token)
      elif token == '(':
         op_stack.push(token)
      elif token == ')':
         top_token = op_stack.pop()
 
         while top_token != '(':
             postfix_list.append(top_token)
             top_token = op_stack.pop()
    else:
         while (not op_stack.is_empty()) and \
           (prec[op_stack.peek()] >= prec[token]):
             postfix_list.append(op_stack.pop())
         op_stack.push(token)
    while not op_stack.is_empty():
      postfix_list.append(op_stack.pop())
    return " ".join(postfix_list)

print(infix_to_postfix("A * B + C * D"))
print(infix_to_postfix("(A + B) * C - ( D - E ) * ( F + G )"))


def postfix_eval(postfix_expr):
    operand_stack = Stack()
    token_list = postfix_expr.split()

    for token in token_list:
        if token in '0123456789':
            operand_stack.push(int(token))
        else:
            operand2 = operand_stack.pop()
            operand1 = operand_stack.pop()
            result = do_math(token, operand1, operand2)
            operand_stack.push(result)
    return operand_stack.pop()

def do_math(op, op1, op2):
    if op == '*':
        return op1 * op2
    elif op == '/':
        return op1 / op2
    elif op == '+':
        return op1 + op2
    else:
        return op1 - op2

print(postfix_eval('7 8 + 3 2 + /'))
