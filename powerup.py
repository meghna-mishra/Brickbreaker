from header import *

class Powerup:
	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.active = 0

	def drop(self):
		if(self.y == 39):
			return False
		self.y += 1
		return True

	def display(self, arr):
		x = self.x
		y = self.y
		for i in range(y, y+1):
			arr[i] = arr[i][:x] + 'P' + arr[i][x+1:]
		return arr

class Expand(Powerup):
	def __init__(self, x, y):
		super().__init__(x, y)
		self.id = 1
		self.time = 200

	def display(self, arr):
		x = self.x
		y = self.y
		for i in range(y, y+1):
			arr[i] = arr[i][:x] + '💙' + arr[i][x+1:]
		return arr

class Shrink(Powerup):
	def __init__(self, x, y):
		super().__init__(x, y)
		self.id = 2
		self.time = 200

	def display(self, arr):
		x = self.x
		y = self.y
		for i in range(y, y+1):
			arr[i] = arr[i][:x] + '🧡' + arr[i][x+1:]
		return arr

class Fast(Powerup):
	def __init__(self, x, y):
		super().__init__(x, y)
		self.id = 3
		self.time = 200

	def display(self, arr):
		x = self.x
		y = self.y
		for i in range(y, y+1):
			arr[i] = arr[i][:x] + '💜' + arr[i][x+1:]
		return arr

class Double(Powerup):
	def __init__(self, x, y):
		super().__init__(x, y)
		self.id = 4
		self.time = 200

	def display(self, arr):
		x = self.x
		y = self.y
		for i in range(y, y+1):
			arr[i] = arr[i][:x] + '💚' + arr[i][x+1:]
		return arr

class Thru(Powerup):
	def __init__(self, x, y):
		super().__init__(x, y)
		self.id = 5
		self.time = 200

	def display(self, arr):
		x = self.x
		y = self.y
		for i in range(y, y+1):
			arr[i] = arr[i][:x] + '💛' + arr[i][x+1:]
		return arr

class Grab(Powerup):
	def __init__(self, x, y):
		super().__init__(x, y)
		self.id = 6
		self.time = 200

	def display(self, arr):
		x = self.x
		y = self.y
		for i in range(y, y+1):
			arr[i] = arr[i][:x] + '🖤' + arr[i][x+1:]
		return arr