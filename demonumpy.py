import numpy as np
mat1 = np.array([[1,2],[3,4]])
print(mat1)
v1 = np.array([2.,4,6,8])
print(v1.shape)
print(mat1.shape)
mat2 = v1.reshape(2,2)
print(mat2)
print(np.linalg.inv(mat2))
print(mat1.dot(mat2))

print(np.real(1j**2))
