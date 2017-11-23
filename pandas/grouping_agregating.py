import pandas as pd 
import numpy as np 

df = pd.read_csv('primary-results.csv')

df.groupby('candidate').aggregate({'votes': [min, np.mean, max]})