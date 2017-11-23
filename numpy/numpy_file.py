import numpy as np 

val1, val2, val3 = np.loadtxt('dados.txt', skiprows=1, unpack=True)

my_array = np.genfromtxt('dados2.txt', skip_header=1, filling_values=1000)
print(my_array)

my_csv = np.genfromtxt("arquivo.csv", delimiter=";", skip_header=1)
print(my_csv)