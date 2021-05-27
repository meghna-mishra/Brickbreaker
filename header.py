import os
from colorama import Fore, init, Back, Style
from powerup import *
init()

DEBUG = 'a'

rows = 40
cols = 190
fps = 20
t = 1/fps

score = 0

powarr = []

powarr.append(Expand(115, 27))
powarr.append(Shrink(95, 27))
powarr.append(Thru(85, 27))
powarr.append(Double(45, 19))
powarr.append(Grab(35, 19))
powarr.append(Fast(155, 19))
