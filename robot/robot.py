# Robos
# 
# A matriz vai de 0x0 ate 10x10
from random import randint

class Point(object):
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def __str__(self):
		return "<%s, %s>" % (self.x, self.y)

class Robot(Point):
	def __init__(self, x, y):
		super(Robot, self).__init__(x, y)

	def move_up(self):
		if self.y < 10:
			self.y += 1
		else:
			print("Movimento Proibido")

	def move_down(self):
		if self.y > 0:
			self.y -= 1
		else:
			print("Movimento Proibido")

	def move_left(self):
		if self.x > 0:
			self.x -= 1
		else:
			print("Movimento Proibido")

	def move_right(self):
		if self.x < 10:
			self.x += 1
		else:
			print("Movimento Proibido")

class Reward(Point):
	def __init__(self, x, y, name):
		super(Reward, self).__init__(x, y)
		self.name = name

	def __str__(self):
		return "<%s, %s>: %s" % (self.x, self.y, self.name)

	def __repr__(self):
		return "<Reward> %s" % str(self)

def check_reward(robot, rewards):
	ok = False
	for reward in rewards:
		if reward.x == robot.x and reward.y == robot.y:
			print("O Robo achou a recompensa: %s" % reward.name)
			ok = True
	return ok

		
reward1 = Reward(randint(0, 10), randint(0, 10), 'Moeda')
reward2 = Reward(randint(0, 10), randint(0, 10), 'Gasolina')
reward3 = Reward(randint(0, 10), randint(0, 10), 'Arma')
reward3 = Reward(randint(0, 10), randint(0, 10), 'Shotgun')
reward4 = Reward(randint(0, 10), randint(0, 10), 'Mingun')
reward5 = Reward(randint(0, 10), randint(0, 10), 'LaserGun')
reward6 = Reward(randint(0, 10), randint(0, 10), 'Municao')
reward7 = Reward(randint(0, 10), randint(0, 10), 'Life')
reward8 = Reward(randint(0, 10), randint(0, 10), 'Life')
reward9 = Reward(randint(0, 10), randint(0, 10), 'Moeda')
rewards = [reward1, reward2, reward3, reward4, reward5, reward6, reward7, reward8, reward9]

robot = Robot(randint(0, 10), randint(0, 10))

for i in range(10):
	movement = input("Digite up, down, left ou right para o movimento: ")
	
	if movement == "up":
		robot.move_up()
	elif movement == "down":
		robot.move_down()
	elif movement == "left":
		robot.move_left()
	elif movement == "right":
		robot.move_right()
	else:
		print("Movimento invalido")
		continue

	print(robot)
	check_reward(robot, rewars)
