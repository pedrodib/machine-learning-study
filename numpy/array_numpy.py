import numpy as np 

arr = np.array([1,2,3])
arr = np.insert(arr, 1, 10)
print(arr)

a = np.array([[1, 2], [3, 4]])
# Soma dos eixos
# [ 1, 3] -> Eixo 1
# [ 2, 4]
# 	|
#  \ /
# Eixo 0 
print(a.sum(axis=0))
print(a.sum(axis=1))

print("\nInsert in axis 1")
print(np.insert(a, 1, 5, axis=1))

print("\nInsert in axis 0")
print(np.insert(a, 0, 5, axis=0))

print("\nAppend")
b = np.array([1, 2, 3])
print(np.append(a, [4, 5, 6]))

print("\nAppend Multidimensional")
b = np.array([[1, 2], [3,4]])
print(np.append(b, [[5, 6]], axis=0))

print("\nDelete from array")
c = np.array([[1,2], [2,3], [3,4]])
print("Axis 0")
print(np.delete(c, 1, 0))
print("Axis 1")
print(np.delete(c, 0, 1))

c2 = np.array([[1,2,3], [4,5,6], [7,8.9], [10,11,12]]) 
print(np.delete(c2, np.s_[::2], 0))

print("\nRepeat")
d = np.array([[1,2], [3,4]])
print(np.repeat(d, 2))
print("Axis 0")
print(np.repeat(a, 2, axis=0))
print("Axis 1")
print(np.repeat(a, 2, axis=1))

print("\nTile")
e = np.array([1,2,3])
print(np.tile(e, 2))

e2 = np.array([[1,2], [3,4]])
print(np.tile(e2, 2))

print("\nSplit")
f = np.array([[1,2,3], [4,5,6]])
print(np.array_split(f, 2, axis=0))

print("\nBinary Array")
print(np.zeros(4))
print(np.zeros([2, 2]))
print(np.ones(5))
print(np.ones([2, 2]))

print("\nMatriz identidade")
print(np.eye(2))

print("\nIndexação Boleana")
g = np.array([[1,2], [3,4], [5,6]])
print(g[g>3])
idx = [g > 2]
print(idx)

print("\nJunção de arrays")
h = np.array([[1,2], [3,4]])
h1 = np.array([[5,6]])
print("Axis 0")
print(np.concatenate([h, h1], axis=0))
print("Axis 1")
print(np.concatenate([h, h1.T], axis=1))

print("\nEmbaralhando")
i = np.arange(10)
np.random.shuffle(i)
print(i)

print("\nNumeros Imaginários/Complexos")
j = np.array([1, 10 + 2j, 20 + 5j], dtype=complex)
print(j)
print(j[1] + j[2])

print("\nLinspace")
print(np.linspace(2.0, 3.0, 10))

print("\nUnicos")
k = np.array([[1,2], [2,3], [3,3], [4,4]])
print(np.unique(k))
