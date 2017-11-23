def sum_a(n1, n2):
	return n1 + n2

def print_():
	print("Eu sou uma funcao")
	print("Aprendendo python")

def is_par(number):
	return number % 2 == 0

def fatorial(number):
	if number == 0 or number == 1:
		return 1
	return number * fatorial(number - 1)

def print_name(name = "Descon"):
	print(name)

def sum_b(x, y, z, function):
	return x + function(y,z)

def sum_c(n1, n2):
	return n1 + n2

def foo(*args):
	return sum(*args)

a = lambda x: x*2

print(sum_a(1,2))
print(is_par(10))
print(fatorial(5))
print_name()
print(sum_b(10, 20, 30, sum_c))
print(a(4))
print(foo([1,2,3,4,5]))