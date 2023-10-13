def evaluate_postfix(exp):
  
  stack = []
  
  for ch in exp:
    if ch.isdigit():
      stack.append(int(ch))
    else:
      op2 = stack.pop()
      op1 = stack.pop()
      if ch == '+':
        stack.append(op1+op2)
      elif ch == '-':
        stack.append(op1-op2)
      elif ch == '*':
        stack.append(op1*op2)
      elif ch == '/':
        stack.append(op1/op2)
        
  return stack.pop()

exp = "35*62/+4-"
print(evaluate_postfix(exp))