import numpy as np

arr1 = np.array([[1, 2, 7, 7],
    [6, 2, 4, 1],
    [7, 7, 8, 9],
    [5, 1, 0, 3]]
)

# counting sequence
res = repr(arr1).count("7, 7")

# printing result
print(res)