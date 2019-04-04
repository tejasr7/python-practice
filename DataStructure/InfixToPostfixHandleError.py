from Stack import Stack

def infix_to_postfix(infix_expr):
    prec = {"^": 4, "*": 3, "/": 3, "+": 2, "-": 2, "(": 1}
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
        postfix_list.append(op.stack.pop())
    return ''.join(postfix_list)

def pren_checker(paren):
    """ This method checks if the parenthesis is balanced or not."""
    S = Stack()
    balanced = True
    index = 0
    while index < len(paren):
        if paren[index] == '(':
            S.push(paren[index])
        else:
            if S.is_empty():
                balanced = False
                break
            else:
                S.pop()
        index += 1
    if not S.is_empty():
        balanced = False
    return balanced
