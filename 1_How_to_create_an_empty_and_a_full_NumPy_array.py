import numpy as np

# creating an simple array
arr1 = np.array([1,2,3,4,5])
print(arr1)

print("\r")

# creating an empty array
arr2 = np.empty(3) # this is dimensional
print(arr2)

print("\r")

arr3 = np.empty((3,4)) # this is dimensional
print(arr3)

print("\r")

# creating an full array
arr4 = np.full((3,4),7)
print(arr4)

print("\r")

# create empty and full array
emp = np.empty([2,3], dtype = int)
print("Empty Array")
print(emp)

print("\r")

full = np.full([2,3],7, dtype = int)
print("Full Array")
print(full)

