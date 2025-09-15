import numpy as np
arr=np.arange(15).reshape(5,3)

print(arr)
# Ist Method....
for i in arr:
    print(i)

for i in np.nditer(arr):
    print(i)
