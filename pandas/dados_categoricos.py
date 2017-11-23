import pandas as pd 
import pydataset 

titanic = pydataset.data('titanic')

print(titanic['class'].nbytes) # Quantidade de Bytes: 10528

titanic['class'] = titanic['class'].astype('category')

print(titanic['class'].nbytes) # Quantidade de Bytes: 1340