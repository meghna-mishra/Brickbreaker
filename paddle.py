from header import *

class Paddle:
	def __init__(self, width, height):
		super().__init__()
		self.width = width
		self.height = height
		self.x = 79
		self.y = 38
		self.v = 1

	def move(self, direction):
		if(self.x+self.width >= cols and direction == 1):
			return False
		elif(self.x <= 0 and direction == -1):
			return False
		else:
			self.x += (self.v * direction)
			return True

	def display(self, color, symbol, arr):
		y = self.y
		height = self.height
		width = self.width
		x = self.x
		for i in range(y, y+height):
			arr[i] = arr[i][:x] + color + symbol*width + Back.RESET + arr[i][x+width:]
		return arr