#Easy
#Задача 1
def infdata(name, age, city):
	print ('{}, {} год(а), проживает в городе {}'.format(name, age, city))

#Задача 2
def max3(num1, num2, num3):
	return (max (num1, num2, num3))

#Задача 3
def lenmax (*args):
	x = max(*args, key = len)
	return x

#Normal
#Задача 1
names = ['Антон', 'Игорь', 'Анна', 'Степан', 'Наталия']
salaries = [35000, 53000, 74000, 62000, 550000]
namesalaries = dict(zip(names, salaries))

infdata = 'salary.txt'
with open (infdata, 'w', encoding = 'UTF-8') as f:
	for key, value in namesalaries.items():
		#filter(lambda value: value < 500000, namesalaries.items())
		f.write('{} - {}\n'.format(key, value)) 

dct = {}
with open (infdata, 'r', encoding = 'UTF-8') as f:
	readf = f.readlines()
	for line in readf:
		del_new_line = line.replace('\n', '')
		i = del_new_line.split(' - ')
		dct[i[0]] = int(i[1])

def tax(slr):
	taxslr = slr * 0.87
	return taxslr

for key, value in dct.items():
	if value < 500000:
		print (key.upper(), int(tax(value)))

