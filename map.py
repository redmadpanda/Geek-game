from summator import *
from minusator import *
from division import *
from multiplication import *
from finished import *
from death import *

class Map():

	karti = {
		"summator": Summator(),
		"minusator": Minusator(),
		"division": Division(),
		"multiplication": Multiply(),
		"death": Death() ,
		"finished": Finished()
	}

	def __init__(self, start_karta):
		# запускается только один раз в начале, будет 'summator'
		self.start_karta = start_karta

	def next_karta(self, karta_name):
		val = Map.karti.get(karta_name)
		# возвращает из словаря по названию класс val = Summator()
		# при первой итерации
		return(val)

	def opening_karta(self):
		return self.next_karta(self.start_karta)

