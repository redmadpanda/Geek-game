from random import randint

class Death():

	text = [
		"You're dead",
		"Ты провалился в ваакум",
		"Что ты наделал?!"
	]

	def enter(self):
		print(Death.text[randint(0,len(self.text) - 1)])
		exit(1)