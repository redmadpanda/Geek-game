from random import randint

class Death():

	text = [
		"You're dead",
		"Ты провалился в ваакум",
		"Что ты наделал?!"
	]

	# тут вводим n и m потомучто для других функций в других классах это
	# уровень и количество задач, тут же они не требуются
	def enter(self, n, m):
		print(Death.text[randint(0,len(self.text) - 1)])
		exit(1)