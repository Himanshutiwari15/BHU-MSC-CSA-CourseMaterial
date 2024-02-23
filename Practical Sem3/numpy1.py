import numpy as np

arr = np.array([1,2,3,4])
zeroD_arr = np.array(25)
threeD_arr = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[0,0,0]]])
tryArgs_arr = np.array([1,2,3,4], ndmin=3)
string_arr = np.array([1,2,3,4], dtype='S')
new_arr = arr.astype('i')
copy_arr = arr.copy()
copy_arr[0] = 30
view_arr = arr.view()
view_arr[0] = 20
#for i in arr:
	#print(i)

#for item in np.nditer(threeD_arr):
	#print(item)

combined_arr = np.concatenate((arr,copy_arr))
arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])
arr12 = np.concatenate((arr1, arr2), axis=1)
arrs12 = np.stack((arr1,arr2))
arrh12 = np.hstack((arr1,arr2))
arrv12 = np.vstack((arr1,arr2))

arr = np.array([41, 42, 43, 44])
x = [True, False, True, False]
newarr = arr[x]

# Create an empty list
filter_arr = []
# go through each element in arr
for element in arr:
  # if the element is higher than 42, set the value to True, otherwise False:
  if element > 42:
    filter_arr.append(True)
  else:
    filter_arr.append(False)

newarr = arr[filter_arr]
#print(filter_arr)
#print(newarr)

filter_arr = arr > 42
newarr = arr[filter_arr]
#print(filter_arr)
#print(newarr)

#print(arr)
#print(type(arr))
#print(zeroD_arr)
#print(threeD_arr)
#print(tryArgs_arr)
#print(arr.ndim)
#print(threeD_arr[1,0,0])
#print(arr[-1])
#print(arr[2:])
#print(arr[-3:-1])
#print(threeD_arr[0:2,1,0:3])
#print(arr.dtype)
#print(string_arr.dtype)
#print(new_arr.dtype)
#print(new_arr)
#print(copy_arr)
#print(view_arr)
#print(arr)
#print(threeD_arr.shape)
#print(threeD_arr.reshape(3,1,-1).shape)
#print(combined_arr)
#print(arr12)
#print(arrs12)
#print(arrh12)
#print(arrv12)
#print(np.array_split(threeD_arr,2))
#print(np.where(arr%2==0))
#print(np.searchsorted(new_arr,5))
#print(np.sort(arr))
#print(newarr)


