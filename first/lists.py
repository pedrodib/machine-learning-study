list = [2, ['pedro', 'joao', 'maria'], 5, 20]
print(list[-1]) # last element
print(list[1][0])

list_new = [1,2,3,4]
list_new.append(5)
list_new.pop(-1) # Remove by index
list_new.remove(4) # Remove by value
i = 0

while i < len(list_new):
	print("%d " % list_new[i])
	i += 1

list1 = [1,2,3,4,5]
list2 = list1
# apenas referencia o id do objeto
# ou seja, eles terão a mesma referencia

list3 =  [1,2,3,4,5]
list4 = list3[:]
# cria uma copia do objeto
# ou seja, eles terão referencias diferentes

