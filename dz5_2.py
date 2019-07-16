#Normal
##Задача-1
import easy

print('Привет! Давай поработаем!')
decision = ''
while decision != 'q':
	print('''Возможные действия:
	1. Перейти в папку
	2. Просмотреть содержимое текущей папки
	3. Удалить папку
	4. Создать папку''')
	decision = input('Введите номер действия (для выхода введите "q": ')
	if decision == '1':
		dir_name = input('Введите имя папки: ')
		easy.change_dir(dir_name)
	elif decision == '2':
		print(easy.in_dir())
	elif decision == '3':
		dir_name = input('Введите имя папки: ')
		easy.del_dir(dir_name)
	elif decision == '4':
		dir_name = input('Введите имя папки: ')
		easy.create_dir(dir_name)
	else:
		print('Некорректный ввод! Попробуйте еще раз!')
