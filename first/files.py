"""
texto = '''Aprendendo Python
Machine Learning
Python is cool
'''

with open('arquivo.txt', 'w') as f:
	f.write(texto)
"""

"""
with open('dataset.txt', 'r') as arq:
	for linha in arq.readlines():
		print(linha)
"""

with open('dataset.txt', 'r') as arq:
	lista = arq.read().splitlines()
	print(lista[0])

print(len(lista))