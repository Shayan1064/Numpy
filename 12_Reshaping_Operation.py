import numpy as np
arr=np.arange(15).reshape(5,3)
print("Array: ",arr)

# Revel (which convert n dimension array into 1 dimension)
arr2=arr.ravel()
print(arr2)

# Transpose
arr3=arr.transpose()
print(arr3)