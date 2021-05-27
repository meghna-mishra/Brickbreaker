from header import *
import string

class Brick:
	def __init__(self, x, y):
		super().__init__()
		self.width = 10
		self.height = 2
		self.x = x
		self.y = y
		self.initialx = x
		self.initialy = y
		self.hit = 0

class RBrick(Brick):
	def __init__(self, x, y):
		super().__init__(x, y)
		self.strength = 3

	def display(self, arr):
		x = self.x
		y = self.y
		width = self.width
		height = self.height
		if(self.strength == 3):
			color = Back.RED
		elif(self.strength == 2):
			color = Back.YELLOW
		elif(self.strength == 1):
			color = Back.GREEN
		for i in range(y, y+height):
			arr[i] = arr[i][:x] + color + (' ')*width + Back.RESET + arr[i][x+width:]
		return arr

class YBrick(Brick):
	def __init__(self, x, y):
		super().__init__(x, y)
		self.strength = 2

	def display(self, arr):
		x = self.x
		y = self.y
		width = self.width
		height = self.height
		if(self.strength == 3):
			color = Back.RED
		elif(self.strength == 2):
			color = Back.YELLOW
		elif(self.strength == 1):
			color = Back.GREEN
		for i in range(y, y+height):
			arr[i] = arr[i][:x] + color + (' ')*width + Back.RESET + arr[i][x+width:]
		return arr

class GBrick(Brick):
	def __init__(self, x, y):
		super().__init__(x, y)
		self.color = Back.GREEN
		self.strength = 1

	def display(self, arr):
		x = self.x
		y = self.y
		width = self.width
		height = self.height
		color = self.color
		for i in range(y, y+height):
			arr[i] = arr[i][:x] + color + (' ')*width + Back.RESET + arr[i][x+width:]
		return arr

class UBrick(Brick):
	def __init__(self, x, y):
		super().__init__(x, y)
		self.color = Back.MAGENTA
		self.strength = 4

	def display(self, arr):
		x = self.x
		y = self.y
		width = self.width
		height = self.height
		color = self.color
		for i in range(y, y+height):
			arr[i] = arr[i][:x] + color + (' ')*width + Back.RESET + arr[i][x+width:]
		return arr

class EBrick(Brick):
	def __init__(self, x, y):
		super().__init__(x, y)
		self.color = Back.CYAN
		self.strength = 5

	def display(self, arr):
		x = self.x
		y = self.y
		width = self.width
		height = self.height
		color = self.color
		for i in range(y, y+height):
			arr[i] = arr[i][:x] + color + (' ')*width + Back.RESET + arr[i][x+width:]
		return arr

class XBrick(Brick):
	def __init__(self, x, y):
		super().__init__(x, y)
		self.color = Back.RED
		self.strength = 3

	def display(self, arr):
		x = self.x
		y = self.y
		width = self.width
		height = self.height
		if(self.strength == 3):
			color = Back.RED
		elif(self.strength == 2):
			color = Back.YELLOW
		elif(self.strength == 1):
			color = Back.GREEN
		for i in range(y, y+height):
			arr[i] = arr[i][:x] + color + (' ')*width + Back.RESET + arr[i][x+width:]
		return arr