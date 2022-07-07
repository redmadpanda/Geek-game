from random import randint

kol_zad = 3

class Summator():

	def enter(self, i):
		print(f'Вам будет предложено {i} задач')
		
		k = 0
		correct = 0
		wrong = 0

		while k < i:
			k += 1
			a = randint(0,100)
			b = randint(0,100)
			print(f'Сколько будет {str(a)} + {str(b)} = ?')
			action = input('>')

			if int(action) == a + b:
				print('Правильно')
				correct += 1
			else:
				print('Нет')
				wrong += 1

		if wrong == 0:		
			return print('minusator')
		else:
			print(f'Всего ошибок {wrong}')
			print('[1] Идем дальше')
			print('[2] Заново пройдем и улучшим результат')
			vibor = input('>')
			if vibor == '1':
				#Далее напишем без print
				return print('minusator')	
			elif vibor == '2':
				return Summator().enter(kol_zad)	
			else:
				print('Идем значит дальше')
				#Далее напишем без print
				return print('minusator')	



Summator().enter(kol_zad)