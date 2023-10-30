import numpy as np

arr1 = np.array([1, 2])
arr2 = np.array([3, 4])
arr3 = np.array([5, 6, 7])

arr3 = np.array(np.meshgrid(arr1, arr2, arr3)).T.reshape(-1, 3)
print(arr3)