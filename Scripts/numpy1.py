import numpy as np

arreglo = np.array([["a", "b"], ["a", "b"]])

print(arreglo)

arreglo = np.array([(1.5, 2.0, 8), (4, 55, 2.5)], dtype = float)

print(arreglo)
#print(np.info(np.ndarray.dtype))

arreglo = np.array([(1.5, 2.0, 8), (4, 55, 2.5), (0, 55, 2.5)], dtype = float)

print(arreglo)

vector = np.arange(50)
print(vector)
print(vector[::-1])
print(vector[-10:-17:-1])
print(vector[40:33:-1])

print(np.arange(0, 6).reshape(2, 3))
print(vector.reshape(5,10))
print(np.arange(0, 9).reshape(3, 3))

print(np.random.random((3,3,3)))
tresd = (np.arange(0,81).reshape((3,3,3,3)))
print(tresd)

#Matriz identidad

print(np.identity(6))
print(np.eye(6))
print(np.ones([6, 6]))