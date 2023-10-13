def reverse_string(str):
  s = []
  
  for ch in str:
    s.append(ch)
    
  rev = ''
  while len(s) > 0:
    rev += s.pop()
    
  return rev

str = "Hello"
print(reverse_string(str))