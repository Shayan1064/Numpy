import numpy as np

arr = np.arange(1, 17).reshape(4, 4)   # Numbers 1 to 16 in 4x4
# print("4x4 Array:\n", arr)

# ways to access rows
print("Row ",arr[0])

# ways to access column
print("Column ",arr[:,2])

# ways to access row and column both but specific index

print(arr[2,2])

