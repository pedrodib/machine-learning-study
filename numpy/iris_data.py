import numpy as np 
import matplotlib.pyplot as plt

data = np.genfromtxt('iris.data.txt', delimiter=',', usecols=[0,1,2,3])
print(data)

# Pegando as 50 primeiras
print(data[:50])
plt.plot(data[:50, 0], c="Red", ls=":", marker="s", ms=8, label="Comp. Sépala Iris-Setosa")
plt.plot(data[50:100, 0], c="Black", ls=":", marker="o", ms=8, label="Comp. Sépala Iris-Versicolor")
plt.legend()
plt.show()