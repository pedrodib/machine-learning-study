import numpy as np

joao_pts 	= [20, 30, 40, 15]
pedro_pts	= [100, 24, 48, 23]
maria_pts	= [92, 22, 34, 12]
marocs_pts 	= [12, 34, 12, 43]

pontos = np.array([joao_pts, pedro_pts, maria_pts, marocs_pts])
print(pontos)
my_data = np.arange(0, 20) # Cria um array
print(my_data)
mat1 = np.reshape(my_data, (5, 4)) # Cria uma matrix por um array
print(mat1)
print(mat1[2][2])

print(pontos.item(5)) #Pega o 5º item da matriz ou array
