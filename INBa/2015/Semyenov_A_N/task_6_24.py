#Задача 6. Вариант 24
#Создайте игру, в которой компьютер загадывает название одной из четырех основных мастей лошадей, а игрок должен его угадать.

#Semyenov A.N.
#30.03.2016
print('Угадайте название одной из четырех основных мастей лошадей, которую загадал компьютер')
import random
a = random.choice(['гнедая', 'рыжая', 'серая', 'вороная'])
b = input('Ваш ответ: ')

b=''
while a !=b : 
	print ('Вы не угадали')
	b = input('Ваш ответ: ')

print ('Вы угадали: ' + a + ' - ' + b)
input('\nНажмите Enter для выхода')