# https://www.youtube.com/watch?v=DHr-Mn_vzs0

def printMaxActivities(arr):
  
  arr.sort(key = lambda x: x[1])

  i = 0
  print(arr[i][0], arr[i][1])

  for j in range(len(arr)):
    if arr[j][0] >= arr[i][1]:
      print(arr[j][0], arr[j][1])
      i = j

arr = [[5, 9], [1, 2], [3, 4], [0, 6], [5, 7], [8, 9]]
printMaxActivities(arr)