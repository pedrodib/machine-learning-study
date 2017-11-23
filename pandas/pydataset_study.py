import pydataset

#print(pydataset.data()) List os datasets

titanic = pydataset.data('titanic')
print("\n Pega os primeiros registros")
print(titanic.head())
print("\n Pega os ultimos registros")
print(titanic.tail())
print("\n Descreve a lista")
print(titanic.describe())
print("\n Contagem de Coluna")
print(titanic['class'].value_counts())