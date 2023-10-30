import numpy as np

# Create a one-dimensional array
array1d = np.array([1, 2, 3])

# Create a two-dimensional array
array2d = np.array([[4, 5, 6],
                     [7, 8, 9]])

# Combine them by stacking array1d on top of array2d as a new row
combined_array = np.vstack((array1d, array2d))

print("Combined Array:")
print(combined_array)

# Alternate method

array1d = np.array([1, 2, 3])
array2d = np.array([[4, 5, 6], [7, 8, 9]])

# Insert the one-dimensional array as the first row of the two-dimensional array
combined_array = np.insert(array2d, 0, array1d, axis=0)

print("Combined Array:")
print(combined_array)
