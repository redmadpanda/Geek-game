from random import randint

class Minusator():

	def enter(self, lev, kol_i):
		print(f'Вам будет предложено {kol_i} задач')
		
		# для итерации
		k = 0
		# кол-во правильных и неправильных ответов
		correct = 0
		wrong = 0

		# учитываем сложность и увеличиваем диапазон чисел
		if lev == 0:
			t = 10
		elif lev == 1:
			t = 100
		else:
			t = 1000

		while k < kol_i:
			k += 1
			
			#  случайно генерируем два числа
			a = randint(0,t)
			b = randint(0,t)
			print(f'Сколько будет {str(a)} - {str(b)} = ?')
			action = input('>')

			# Введем подсчет правильных и неправильных ответов
			if int(action) == a - b:
				print('Правильно')
				correct += 1
			else:
				print('Не правильно')
				wrong += 1

		# Если все ответы правильные, то сразу переходим 
		# на следующий уровень
		if wrong == 0:		
			return print('division')

		# Если неправильных ответов больше 0
		else:
			print(f'Всего ошибок {wrong} из {kol_i}')
			print('[1] Идем дальше')
			print('[2] Заново пройдем и улучшим результат')
			vibor = input('>')
			if vibor == '1':
				#Далее напишем без print
				return print('division')	
			elif vibor == '2':
				return Minusator().enter(lev,kol_i)	
			else:
				print('Не любим зачит математику?!')
				#Далее напишем без print
				return print('death')	



