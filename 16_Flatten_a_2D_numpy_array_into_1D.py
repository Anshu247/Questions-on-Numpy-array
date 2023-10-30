import numpy as np

arr1 = np.array([[1, 2, 3], [4, 5, 6]])
arr2 = np.array([[10, 11, 12], [13, 14, 15]])

fl = arr1.flatten() # flatten method
rav = arr2.ravel() # ravel method

print("Printing original 2D array\n", arr1)
print("\r")

print("Printing original 2D array\n", arr2)
print("\r")

print("With flatten method\n", fl)
print("\r")
print("With ravel method\n", rav)




