# importing Numpy package
import numpy as np

# Creating a 2X2 Numpy matrix
array = np.ones((2, 2))
# array = np.zeros((3, 3))

print("Original array")
print(array)

print("\n0 on the border and 1 inside the array")

# constructing border of 0 around 2D identity matrix
# using np.pad()

array = np.pad(array, pad_width=1, mode='constant',
			constant_values=0)

# array = np.pad(array, pad_width=1, mode='constant',
# 			constant_values=1)

print(array)
