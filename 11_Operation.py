import numpy as np

arr1=np.array([1,2,3,4,5])
arr2=np.array([6,7,8,9,0])

arr3=arr1+arr2  # addition

arr4=arr1-arr2  # subtraction

arr5=arr1*arr2   # Multiply

print(arr3)
print(arr4)
print(arr5)

arr6=np.arange(6).reshape(2,3)
arr7=np.arange(6,12).reshape(3,2)

print(arr6)
print(arr7)

arr8=arr6.dot(arr7)   # dot product of matrix
print(arr8)

maxi=arr6.max()
mini=arr6.min()

print(maxi)
print(mini)


