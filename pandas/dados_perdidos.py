import pandas as pd 
import numpy as np 

dados = {
	'nome': ['João', 'Maria', np.nan, np.nan, 'Pedro'],
	'sexo':  ['M', np.nan, 'F', np.nan, 'M'],
	'idade': [np.nan, 14, 13, np.nan, 21],
	'nota':  [np.nan, 7, 6, np.nan, 10]
}

df = pd.DataFrame(dados)
print(df)
print("\n Remover quando tem dado faltando")
print(df.dropna())

print("\n Remover se todos os dados estão faltando na linha")
print(df.dropna(how='all'))

df['serie'] = np.nan
print(df)
print("\n Remover se todos os dados estão faltando na coluna")
print(df.dropna(how='all', axis=1))

print("\n Remover se tiver mais de 3 dados faltando na coluna")
print(df.dropna(thresh=3))

print("\n Preencher se tiver dados faltando na coluna")
df['serie'].fillna(8, inplace=True)
print(df)

df['serie'] = np.nan

print("\n Preencher com a media se tiver dados faltando na coluna")
df['idade'].fillna(df['idade'].mean(), inplace=True)
print(df)

print("\n Filtrar onde nome e sexo nao for nulos")
print(df[df['nome'].notnull() & df['sexo'].notnull()])