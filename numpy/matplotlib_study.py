import matplotlib.pyplot as plt 
import numpy as np 

salario_pedro 	= np.array([100, 200, 300, 500, 400, 150])
salario_marcos 	= np.array([200, 300, 400, 600, 700, 950])
salario_joao 	= np.array([400, 100, 800, 400, 700, 1700])

plt.plot(salario_pedro, c='Red', ls='--', marker='s', ms=7, label="Salários Pedro")
plt.plot(salario_marcos, c='Black', ls='--', marker='^', ms=7, label="Salários Marcos")
plt.plot(salario_joao, c='Green', ls='--', marker='o', ms=7, label="Salários João")
plt.legend()
plt.show()