dobro = lambda x: x*2
soma = lambda x, y: x + y
print(dobro(3))
print(soma(10, 20))

lista = [1,2,3,4,5,6,7,8,9,10]
lista2 = list(filter(lambda x: x % 2 == 0, lista))

print(lista2)

lista2 = list(map(lambda x: x*2, lista))
print(lista2)