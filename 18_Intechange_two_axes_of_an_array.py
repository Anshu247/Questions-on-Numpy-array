import numpy as np

arr1 = np.array([[1, 2, 3, 4]])
ax = np.swapaxes(arr1, 0, 1)

print(ax)