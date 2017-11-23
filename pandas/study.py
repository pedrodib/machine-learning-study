import pandas as pd 
s = pd.Series([1, 4, 6, 5, 7, 10, 6])
print(s)
print("\nDescribe")
print(s.describe())
print("\nMédia")
print(s.mean())
print("\nMediana")
print(s.median())
print("\nÉ duplicado")
print(s.duplicated())

print("\nAppend")
s2 = pd.Series([11, 5, 8])
s = s.append(s2)

print(s)