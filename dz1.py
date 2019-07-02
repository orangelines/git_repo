#Easy
# Задача 1:
a = 12
b = 'abc'
c = (1, 'adventures', [2, 13])
print (b)
cat = input ('Name of your cat: ')
print(cat, ', hello!')

# Задача 2:
number1 = int(input('Введите число: '))
print(number1 + 2)

# Задача 3:
age = int(input ('Ваш возраст: '))
if age >= 18:
	print('Доступ разрешен')
else:
	print('Извините, пользование данным ресурсом только с 18 лет')

#Normal
#Задача 1:
while True:
	try:
		number2 = int(input('Введите число: '))
		if 0 < number2 < 10:
			print(number2 ** 2)
		# elif 0 >= number2 or number2>= 10:
		else:
			print ('Число неверное. Диапазон допустимых значений: (0;10)')
	except ValueError:
		print('Это не число. До свидания!')
		break
			
#Задача 2:
a = int(input('Введите число №1: '))
b = int(input('Введите число №2: '))
a, b = b, a
print('Число №1?: ', a)
print('Число №2?: ', b)

#Hard
#Задача 1:
print('Медицинская анкета')
name = input('Ваше имя: ')
surname = input('Ваша фамилию: ')
age = int(input('Ваш возраст: '))
weight = int(input('Ваш вес: '))

if age <= 30 and 50 < weight < 120:
	print(name, surname, ",", age, 'год', ',', 'вес', weight, '-', 'хорошее состояние')
elif age > 60 and 50 < weight < 120:
	print(name, surname, ",", age, 'год', ',', 'вес', weight, '-', 'следите за своим здоровьем')	
elif age > 60 and (50 > weight or weight > 120):
	print(name, surname, ",", age, 'год', ',', 'вес', weight, '-', 'срочно! срочно к врачу!!')	
elif age > 40 and (50 > weight or weight > 120):
	print(name, surname, ",", age, 'год', ',', 'вес', weight, '-', 'требуется врачебный осмотр!')	
elif age > 30 and (50 > weight or weight > 120):
	print(name, surname, ",", age, 'год', ',', 'вес', weight, '-', 'следует начать вести правильный образ жизни')	
elif age > 30 and 50 < weight < 120:
	print(name, surname, ",", age, 'год', ',', 'вес', weight, '-', 'хорошее состояние')
else:
	print(name, surname, ",", age, 'год', ',', 'вес', weight, '-', 'следует начать вести правильный образ жизни')
	