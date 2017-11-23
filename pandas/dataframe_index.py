import pandas as pd 

df = pd.DataFrame(
	[
		['PE', 'Pernambuco', 'Recife'], ['RJ', 'Rio de Janeiro', 'Rio de Janeiro'],
		['SP', 'São Paulo', 'São Paulo'], ['AC', 'Acre', 'Rio Branco']
	],
	columns=['Sigla', 'Estado', 'Capital']
)

print("\nPega o Indice")
print(df.ix[0])
print("\nPega a Posição")
print(df.iloc[0])
print("\nPega o indice de 0 à 2")
print(df.ix[:2])
print("\nPega a posição de 0 à 1")
print(df.iloc[:2])

df.index = pd.Index(df['Sigla'])
del df['Sigla']
print("\nIndice mudado")
print(df)
