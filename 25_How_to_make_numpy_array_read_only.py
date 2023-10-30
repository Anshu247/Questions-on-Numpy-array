import numpy as np


a = np.zeros(11)
print("Before any change ")
print(a)

a[1] = 2
print("Before after first change ")
print(a)

a.setflags(write=False) # this will not change the value at index 2
# a.setflags(write=True) # this will change the value at index 2 
print("After making array immutable on attempting second change ")
a[1] = 7
