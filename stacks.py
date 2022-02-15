
# Evaluate Reverse Polish Notation
def eval_rpn(tokens):
    stack = []
    operators = {'+', '-', '*', '/'}
    for token in tokens:
        if token in operators:
            b, a = stack.pop(), stack.pop()
            if token == '+':
                stack.append(a + b)
            elif token == '-':
                stack.append(a - b)
            elif token == '*':
                stack.append(a * b)
            else:
                stack.append(int(a / b))
        else:
            stack.append(int(token))
    return stack[0]

