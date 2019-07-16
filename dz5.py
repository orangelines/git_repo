#Easy
#Задача-1
import os
import shutil
x = 1 
name = 'dir_' 

while x <=9: 
	dir_path = os.path.join(os.getcwd(), name + str(x)) 
	try: 
		os.mkdir(dir_path) 
	except FileExistsError: 
		print('Такая директория уже существует') 
	x += 1

while x >= 1:
	try:
		os.rmdir(name + str(x))
	except FileNotFoundError:
		pass
	x = x - 1

print(os.listdir())


#Задача-2
import os

inside1 = list(os.listdir())
inside2 = []
for i in inside1:
	if os.path.isdir(i):
		inside2.append(i)
print(inside2)

#Задача-3
new_file = __file__ + '.py'
shutil.copy(__file__, new_file)
