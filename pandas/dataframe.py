import pandas as pd 

df = pd.DataFrame(
	[
		['fchollet/keras', 11302],
		['openai/universe', 4350],
		['pandas-dev/pandas', 8168]
	],
	columns=['repository', 'stars']
)
print("\nMostrando a dimensão")
print(df.shape)
print("\nMostrando a tabela")
print(df)
print("\nAcessando as Colunas")
print(df['stars'])

print("\nMedia de Stars")
print(df['stars'].mean())
print("\nMediaana de Stars")
print(df['stars'].median())

print("\nAcessando as Linhas")
print(df.iloc[1])
print("\nAcessando Coluna das Linhas")
print(df.iloc[1]['stars'])