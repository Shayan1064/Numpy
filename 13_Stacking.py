import numpy as np
arr1=np.arange(6).reshape(2,3)
arr2=np.arange(7,13).reshape(2,3)

arr3=np.hstack((arr1,arr2))
print("The Hstake is: ",arr3)

arr4=np.vstack((arr1,arr2))
print("The Vstake is: ",arr4)