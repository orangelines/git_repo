#Easy
#Задача 1
lst1 = [56, 983, -5, 1, -657, 4, 10]
lst2 = [i ** 2 for i in lst1]
print (lst2)

#Задача 2
fruits1 = ['Яблоко', 'Груша', 'Апельсин', 'Банан']
fruits2 = ['Абрикос', 'Персик', 'Апельсин', 'Яблоко'] 
fruits3 = [fruit for fruit in fruits1 if fruit in fruits2] 
print(fruits3) 

#Задача 3
lst = [2, 9, -5, 0, 16, 256] 
new_list = [i for i in lst if (i % 3 == 0) and (i > 0) and (i % 4 != 0)] 
print(new_list)


#Normal
#Задача 1
import re
name = input('Ваше имя: ')
surname = input('Ваша фамилия: ')
e_mail = input('Ваш e-mail: ')
name_pattern = re.match(r'\b[А-ЯA-Z]\w+', name)
surname_pattern = re.match(r'\b[А-ЯA-Z]\w+', surname)
e_mail_pattern = re.match(r'\b[a-z0-9_]+@[a-z0-9]+.[ru, org, com]+', e_mail)

checkresult = (name_pattern, surname_pattern, e_mail_pattern) 
for i in checkresult: 
	if bool(i) is True: 
		print('Супер!') 
	else: 
		print('Некорректные данные!')

#Задача 2
some_str = '''
Мороз и солнце; день чудесный!
Еще ты дремлешь, друг прелестный —
Пора, красавица, проснись:
Открой сомкнуты негой взоры
Навстречу северной Авроры,
Звездою севера явись!
Вечор, ты помнишь, вьюга злилась,
На мутном небе мгла носилась;
Луна, как бледное пятно,
Сквозь тучи мрачные желтела,
И ты печальная сидела —
А нынче... погляди в окно:
Под голубыми небесами
Великолепными коврами,
Блестя на солнце, снег лежит;
Прозрачный лес один чернеет,
И ель сквозь иней зеленеет,
И речка подо льдом блестит.
Вся комната янтарным блеском
Озарена. Веселым треском
Трещит затопленная печь.
Приятно думать у лежанки.
Но знаешь: не велеть ли в санки
Кобылку бурую запречь?
Скользя по утреннему снегу,
Друг милый, предадимся бегу
Нетерпеливого коня
И навестим поля пустые,
Леса, недавно столь густые,
И берег, милый для меня.'''

result_of_search = re.findall(r'\.\.+', some_str) 
print('В тексте найдено (значения более одной "."): ', result_of_search)