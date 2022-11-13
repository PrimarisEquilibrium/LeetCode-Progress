import numpy as np

def snail(snail_map):
    dimensions = np.shape(snail_map)
    return dimensions

array = [[1,2,3],
         [4,5,6],
         [7,8,9]]
print(snail(array))