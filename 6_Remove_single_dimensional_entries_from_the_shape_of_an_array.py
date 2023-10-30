import numpy as np

arr1 = np.array([[[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]]])
arr2 = np.squeeze(arr1)

print(arr1) # printing original array
print(arr2) # printing squeeze array