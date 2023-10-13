# https://www.youtube.com/watch?v=2i5pclQprGk

def fractionalKnapsack(W, arr):
  arr.sort(key = lambda x: x[0]/x[1], reverse = True)

  finalvalue = 0

  for item in arr:
    if item[1] <= W:
      W -= item[1]
      finalvalue += item[0]
    else:
      finalvalue += item[0] * (W/item[1])
      break

  return finalvalue
      
W = 50
arr = [[60, 10], [100, 20], [120, 30]]

print("Maximum value we can obtain = ", fractionalKnapsack(W, arr))