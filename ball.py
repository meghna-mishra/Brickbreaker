from header import *
from sound import *

class Ball:
	def __init__(self, width, height, x, y):
		super().__init__()
		self.width = width
		self.height = height
		self.x = x
		self.y = y
		self.vx = 1
		self.vy = 1
		self.moving = 0
		self.first = 1
		self.fail = 0
		self.stick = 0
		self.thru = 0
		self.fast = 0

	def display(self, symbol, arr):
		y = self.y
		height = self.height
		width = self.width
		x = self.x
		for i in range(y, y+height):
			arr[i] = arr[i][:x] + symbol + arr[i][x+width:]
		return arr

	def move(self, paddle, brickarr, movedown):
		if(self.moving == 0):
			return brickarr

		if(self.x+self.width >= cols or self.x <= 0):
			self.vx = -(self.vx)
			wallbajao()

		if(self.y <= 1):
			self.vy = -(self.vy)
			wallbajao()

		if(self.y+self.height == paddle.y and self.x >= paddle.x and self.x+self.width <= paddle.x+paddle.width and self.first == 0):
			if(self.stick == 1):
				self.moving = 0
				self.first = 1
			if(self.x < (paddle.x+((paddle.width - 1)/3))):
				self.vx -= 1
				self.vy = -(self.vy)
			elif(self.x < (paddle.x+(2*(paddle.width - 1)/3))):
				self.vy = -(self.vy)
			else:
				self.vx += 1
				self.vy = -(self.vy)
			paddlebajao()
			if(movedown == True):
				for brick in brickarr:
					if(brick.strength != 0):
						brick.y += 1

		if(self.y >= rows-2):
			self.moving = 0
			self.x = 94
			self.y = 37
			if(self.fast == 1):
				self.vx = 2
				self.vy = 2
			else:
				self.vx = 1
				self.vy = 1
			self.first = 1
			self.fail = 1
			return brickarr

		for brick in brickarr:
			#brick bottom
			if(self.y == brick.y+brick.height and self.x+self.width > brick.x and self.x < brick.x+brick.width and brick.strength != 0):
				self.vy = -(self.vy)
				brickbajao()
				print("Bottom")
				print(brick.y)
				print(brick.x)
				if(self.thru == 1 and brick.strength != 0):
					brick.strength = 0
					for powup in powarr:
						if(powup.x == (brick.initialx + 5) and powup.y == (brick.initialy + 2)):
							powup.active = 1
				if(brick.strength != 4 and brick.strength!=0):
					brick.strength -= 1
					if(brick.hit == 0):
						brick.hit = 1
					if(brick.strength == 0):
						for powup in powarr:
							if(powup.x == (brick.initialx + 5) and powup.y == (brick.initialy + 2)):
								powup.active = 1
				break
			#brick top
			elif(self.y+self.height == brick.y and self.x+self.width > brick.x and self.x < brick.x+brick.width and brick.strength != 0):
				self.vy = -(self.vy)
				brickbajao()
				print("Top")
				print(brick.y)
				print(brick.x)
				if(self.thru == 1 and brick.strength != 0):
					brick.strength = 0
					for powup in powarr:
						if(powup.x == (brick.initialx + 5) and powup.y == (brick.initialy + 2)):
							powup.active = 1
				if(brick.strength != 4 and brick.strength!=0):
					brick.strength -= 1
					if(brick.hit == 0):
						brick.hit = 1
					if(brick.strength == 0):
						for powup in powarr:
							if(powup.x == (brick.initialx + 5) and powup.y == (brick.initialy + 2)):
								powup.active = 1
				break
			#brick right
			elif(self.x == brick.x+brick.width and self.y >= brick.y and self.y < brick.y+brick.height and brick.strength != 0):
				self.vx = -(self.vx)
				print("Right")
				brickbajao()
				print(brick.y)
				print(brick.x)
				if(self.thru == 1 and brick.strength != 0):
					brick.strength = 0
					for powup in powarr:
						if(powup.x == (brick.initialx + 5) and powup.y == (brick.initialy + 2)):
							powup.active = 1
				if(brick.strength != 4 and brick.strength!=0):
					brick.strength -= 1
					if(brick.hit == 0):
						brick.hit = 1
					if(brick.strength == 0):
						for powup in powarr:
							if(powup.x == (brick.initialx + 5) and powup.y == (brick.initialy + 2)):
								powup.active = 1
				break
			#brick left
			elif(self.x+self.width == brick.x and self.y >= brick.y and self.y < brick.y+brick.height and brick.strength != 0):
				self.vx = -(self.vx)
				print("Left")
				brickbajao()
				print(brick.y)
				print(brick.x)
				if(self.thru == 1 and brick.strength != 0):
					brick.strength = 0
					for powup in powarr:
						if(powup.x == (brick.initialx + 5) and powup.y == (brick.initialy + 2)):
							powup.active = 1
				if(brick.strength != 4 and brick.strength!=0):
					brick.strength -= 1
					if(brick.hit == 0):
						brick.hit = 1
					if(brick.strength == 0):
						for powup in powarr:
							if(powup.x == (brick.initialx + 5) and powup.y == (brick.initialy + 2)):
								powup.active = 1
				break
			#Bottom left
			elif(self.x+self.width == brick.x and self.y == brick.y+brick.height and self.vx>0 and self.vy>0 and brick.strength != 0):
				self.vy = -(self.vy)
				print("Bottom left edge")
				brickbajao()
				print(brick.y)
				print(brick.x)
				if(self.thru == 1 and brick.strength != 0):
					brick.strength = 0
					for powup in powarr:
						if(powup.x == (brick.initialx + 5) and powup.y == (brick.initialy + 2)):
							powup.active = 1
				if(brick.strength != 4 and brick.strength!=0):
					brick.strength -= 1
					if(brick.hit == 0):
						brick.hit = 1
					if(brick.strength == 0):
						for powup in powarr:
							if(powup.x == (brick.initialx + 5) and powup.y == (brick.initialy + 2)):
								powup.active = 1
				break
			#Bottom right
			elif(self.x == brick.x+brick.width and self.y == brick.y+brick.height and self.vx<0 and self.vy>0 and brick.strength != 0):
				self.vy = -(self.vy)
				print("Bottom right edge")
				brickbajao()
				print(brick.y)
				print(brick.x)
				if(self.thru == 1 and brick.strength != 0):
					brick.strength = 0
					for powup in powarr:
						if(powup.x == (brick.initialx + 5) and powup.y == (brick.initialy + 2)):
							powup.active = 1
				if(brick.strength != 4 and brick.strength!=0):
					brick.strength -= 1
					if(brick.hit == 0):
						brick.hit = 1
					if(brick.strength == 0):
						for powup in powarr:
							if(powup.x == (brick.initialx + 5) and powup.y == (brick.initialy + 2)):
								powup.active = 1
				break
			#Top left
			elif(self.y+self.height == brick.y and self.x+self.width == brick.x and self.vx>0 and self.vy<0 and brick.strength != 0):
				self.vy = -(self.vy)
				print("Top left edge")
				brickbajao()
				print(brick.y)
				print(brick.x)
				if(self.thru == 1 and brick.strength != 0):
					brick.strength = 0
					for powup in powarr:
						if(powup.x == (brick.initialx + 5) and powup.y == (brick.initialy + 2)):
							powup.active = 1
				if(brick.strength != 4 and brick.strength!=0):
					brick.strength -= 1
					if(brick.hit == 0):
						brick.hit = 1
					if(brick.strength == 0):
						for powup in powarr:
							if(powup.x == (brick.initialx + 5) and powup.y == (brick.initialy + 2)):
								powup.active = 1
				break
			#Top right
			elif(self.y+self.height == brick.y and self.x == brick.x+brick.width and self.vx<0 and self.vy<0 and brick.strength != 0):
				self.vy = -(self.vy)
				print("Top right edge")
				brickbajao()
				print(brick.y)
				print(brick.x)
				if(self.thru == 1 and brick.strength != 0):
					brick.strength = 0
					for powup in powarr:
						if(powup.x == (brick.initialx + 5) and powup.y == (brick.initialy + 2)):
							powup.active = 1
				if(brick.strength != 4 and brick.strength!=0):
					brick.strength -= 1
					if(brick.hit == 0):
						brick.hit = 1
					if(brick.strength == 0):
						for powup in powarr:
							if(powup.x == (brick.initialx + 5) and powup.y == (brick.initialy + 2)):
								powup.active = 1
				break
		if(self.moving == 1):
			self.x += self.vx
			self.y -= self.vy
			self.first = 0
		print(self.x)
		print(self.y)
		return brickarr
