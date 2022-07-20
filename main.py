from map import *
from engine import *


lev = input('Введите уровень сложности [0,1,2]: ')
kol_i = input('Ведите количество задач на уровнях: ')
Engine(Map('summator'), lev, kol_i).play()
