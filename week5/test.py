__author__ = 'Mies'

from math import sin
from time import sleep

for i in range(1, 100000):
    print(' '*(round(sin(i/40)*100)+100), 'x')
    sleep(0.01)