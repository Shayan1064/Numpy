import numpy as np

arr = np.arange(15)   # Creates an array [0, 1, 2, ..., 14]
print("Original Array:", arr)

reshaped = arr.reshape(5, 3)   # Convert into 5 rows × 3 columns
print("\nReshaped Array:\n", reshaped)
