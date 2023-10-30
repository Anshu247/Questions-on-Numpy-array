import numpy as np

arr1 = ([[1, 2, 3, 4,], [5, 6, 7, 8]])
res1 = np.size(arr1)

res2 = np.size(arr1, 0)
res3 = np.size(arr1, 1)

print(res1)
print(res2)
print(res3)