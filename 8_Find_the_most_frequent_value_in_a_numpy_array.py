import numpy as np

# creating an array
arr1 = np.array([1, 2, 3, 7, 6, 7, 7, 3, 9, 1, 7, 9, 2, 2])

# count number of occurence of element
count = np.bincount(arr1)

# store most frequent element in freq
freq = np.argmax(count)

# printing result
print(freq)


# If the array has more than one element having maximum frequency

x = np.array([1, 1, 1, 2, 3, 4, 2, 4, 3, 3, ])
print("Original array:")
print(x)

print("Most frequent value in above array")
y = np.bincount(x)
maximum = max(y)

for i in range(len(y)):
	if y[i] == maximum:
		print(i, end=" ")
