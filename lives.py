from header import *
import string

class Lives:
	def __init__(self):
		self.value = 15
		self.x = 0
		self.y = 0

	def display(self, arr):
		y = self.y
		x = self.x
		for i in range(y, y+1):
			arr[i] = arr[i][:x] + "Lives: "+ str(self.value) + arr[i][x+8:]
		return arr