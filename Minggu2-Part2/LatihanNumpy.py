import numpy as np

weight = [66.5, 60.3, 64.7, 89.5, 69.8] 
np_weight = np.array(weight)
print(weight)
print(type(np_weight))

np_2d = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(np_2d)
print(np_2d.shape)

np_test = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15]])
print(np_test)
print(np_test.shape)
