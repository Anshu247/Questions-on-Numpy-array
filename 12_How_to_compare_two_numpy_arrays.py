import numpy as np

arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[1, 2], [3, 4]])

comp = arr1 == arr2
res = comp.all()

print(res)
print(comp)

