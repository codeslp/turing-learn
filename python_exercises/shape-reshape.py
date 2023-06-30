import numpy as np

array = np.array(list(map(int,input().split())))
reshaped_array = np.reshape(array, (3, 3))
print(reshaped_array)