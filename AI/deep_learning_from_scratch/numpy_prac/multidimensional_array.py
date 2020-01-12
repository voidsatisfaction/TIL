import numpy as np

B = np.array([[1, 2], [3, 4], [5, 6]])

B
np.ndim(B) # 2
B.shape # (3,2) 3x2 행렬

A = np.array([[1,2,3], [4,5,6]])
B = np.array([[1,2], [3,4], [5,6]])

np.dot(A, B)
