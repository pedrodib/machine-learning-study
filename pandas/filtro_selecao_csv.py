import pandas as pd 

copacabana = pd.read_csv("copacabana.csv", delimiter=";")
print(copacabana.columns)
print(copacabana['Quartos'].describe())
print(copacabana.loc[copacabana['Quartos'] == 6])

copacabana['Vl_Imovel'] = copacabana['AreaConstruida'] * copacabana['VAL_UNIT']
print(copacabana.head())