import numpy as np

arr1 = np.zeros((1,2,3,4))
# arr1 = np.array([1,2,3,4])
ax = np.moveaxis(arr1, 0, -1).shape

print(ax)