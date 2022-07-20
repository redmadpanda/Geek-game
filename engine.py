from map import *

class Engine(object):

	def __init__(self, scene_map, lev, kol_i):
		self.scene_map = scene_map
		self.lev = int(lev)
		self.kol_i = int(kol_i)

	def play(self):
		current_scene = self.scene_map.opening_karta()
		last_scene = self.scene_map.next_karta('finished')

		while current_scene != last_scene:
			next_scene_name = current_scene.enter(self.lev, self.kol_i)
			current_scene = self.scene_map.next_karta(next_scene_name)

		current_scene.enter()