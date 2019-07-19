#Normal
#Задача 1
class Person:
	def __init__(self, name, health, damage, armor, isDeath):
		self.name = name
		self.health = health
		self.damage = damage
		self.armor = armor
		self.isDeath = isDeath
	
	def attack(self):
		pass

	def damg(self):
		pass

class Player(Person):
	def __init__(self, name, health, damage, armor):
		Person.__init__(self, name, health, damage, armor)
		self.name = name
		self.health = health
		self.damage = damage
		self.armor = armor

	def attack(self):
		self.health = self.health - (Enemy(self.damage) - self.armor)
		return self.health

class Enemy(Person):
	def __init__(self, name, health, damage, armor):
		Enemy.__init__(self, name, health, damage, armor)
		self.name = name
		self.health = health
		self.damage = damage
		self.armor = armor

	def attack(self):
		self.health = self.health - (Player(self.damage) - self.armor)
		return self.health


class Play:
	def __init__(self)

	def bom (self, ):


