#Easy
#Задача 1
class TownCar:
	def __init__(self, name, speed, color, is_police):
		self.name = name
		self.speed = speed
		self.color = color
		self.is_police = is_police

	def go(self):
		print('Едем...')
	
	def stop(self):
		print('Стоп!')

	def turn(self, direction):
		if direction == 'направо':
			print('Повернул направо...')
		elif direction == 'налево':
			print('Повернул налево...')
		else:
			print('Никуда не повернул. Едем прямо...')

class SportCar:
	def __init__(self, name, speed, color, is_police):
		self.name = name
		self.speed = speed
		self.color = color
		self.is_police = is_police

	def go(self):
		print('Едем...')
	
	def stop(self):
		print('Стоп!')

	def turn(self, direction):
		if direction == 'направо':
			print('Повернул направо...')
		elif direction == 'налево':
			print('Повернул налево...')
		else:
			print('Никуда не повернул. Едем прямо...')

class WorkCar:
	def __init__(self, name, speed, color, is_police):
		self.name = name
		self.speed = speed
		self.color = color
		self.is_police = is_police

	def go(self):
		print('Едем...')
	
	def stop(self):
		print('Стоп!')

	def turn(self, direction):
		if direction == 'направо':
			print('Повернул направо...')
		elif direction == 'налево':
			print('Повернул налево...')
		else:
			print('Никуда не повернул. Едем прямо...')

class PoliceCar:
	def __init__(self, name, speed, color, is_police):
		self.name = name
		self.speed = speed
		self.color = color
		self.is_police = is_police

	def go(self):
		print('Едем...')
	
	def stop(self):
		print('Стоп!')

	def turn(self, direction):
		if direction == 'направо':
			print('Повернул направо...')
		elif direction == 'налево':
			print('Повернул налево...')
		else:
			print('Никуда не повернул. Едем прямо...')
