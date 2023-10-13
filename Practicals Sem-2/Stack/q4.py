# Function to return precedence of operators
def precedence(op):
    if op == '+' or op == '-':
        return 1
    if op == '*' or op == '/':
        return 2
    return 0

# Function to convert infix to postfix


def infixToPostfix(exp):

    stack = []
    output = ''

    for ch in exp:

        # If operand, add to output
        if ch.isalpha() or ch.isdigit():
            output += ch

        # If opening bracket, push to stack
        elif ch == '(':
            stack.append(ch)

        # If closing bracket, pop stack until opening bracket
        elif ch == ')':
            while stack and stack[-1] != '(':
                output += stack.pop()
            stack.pop()  # Pop opening bracket

        # If operator
        else:
            while stack and precedence(ch) <= precedence(stack[-1]):
                output += stack.pop()
            stack.append(ch)

    # Pop remaining operators from stack
    while stack:
        output += stack.pop()

    return output


exp = "(a+b)*(c+d)"
print(infixToPostfix(exp))
