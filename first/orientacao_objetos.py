class Pessoa:

	def __init__(self, nome, idade):
		self.nome = nome
		self.idade = idade

	def imprimir_nome(self):
		print(self.nome)
		
p = Pessoa('Pedro', 21)
p.imprimir_nome()

class Conta:
	def __init__(self, cliente, numero):
		self.cliente = cliente
		self.numero = numero

class ContaEspecial(Conta):
	def __init__(self, cliente, numero, limite = 0):
		Conta.__init__(self, cliente, numero)
		self.limite = limite

conta = ContaEspecial("Pedro", "1234-5", 4000)
print(conta.limite)
print(conta.cliente)
print(conta.numero)
