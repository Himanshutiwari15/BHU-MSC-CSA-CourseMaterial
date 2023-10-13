def intervalSchedule(intervals):
  
  intervals.sort(key = lambda x: x[1])

  count = 1
  end = intervals[0][1]
  print(intervals[0])
  
  for i in range(1, len(intervals)):
    if intervals[i][0] >= end:
      print(intervals[i]) 
      end = intervals[i][1]
      count += 1

  print("Number of non-conflicting intervals =", count)

intervals = [[6,8], [1,9], [2,4], [4,7]]
intervalSchedule(intervals)