from header import *
import string

class Timer:
	def __init__(self):
		self.x = 179
		self.y = 0

	def display(self, value, arr):
		y = self.y
		x = self.x
		if(value < 10):
			symbol = '000'+str(value)
		elif(value < 100):
			symbol = '00'+str(value)
		elif(value < 1000):
			symbol = '0'+str(value)
		else:
			symbol = str(value)
		for i in range(y, y+1):
			arr[i] = arr[i][:x] + "Time: "+ symbol + arr[i][x+10:]
		return arr