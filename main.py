import os
import time
import signal
import random
import copy
import string

from header import *
from input import *
from paddle import *
from ball import *
from brick import *
from lives import *
from score import *
from timer import *
from sound import *

ballvar = 0

blank_arr = []

for i in range(rows):
	blank_arr.append(' '*cols + '\n')

paddle = Paddle(31, 1)
ball = Ball(2, 1, 94, 37)
lives = Lives()
score = Score()
timer = Timer()

brickarr = []

movedown = False
gameover = False

#brickarr.append(RBrick(130, 9))
#brickarr.append(GBrick(120, 9))
brickarr.append(YBrick(110, 9))
brickarr.append(UBrick(100, 9))
brickarr.append(RBrick(90, 9))
brickarr.append(GBrick(80, 9))
brickarr.append(YBrick(70, 9))
#brickarr.append(UBrick(60, 9))
#brickarr.append(RBrick(50, 9))

#brickarr.append(YBrick(150, 13))
#brickarr.append(UBrick(140, 13))
brickarr.append(RBrick(130, 13))
brickarr.append(GBrick(120, 13))
brickarr.append(YBrick(110, 13))
brickarr.append(UBrick(100, 13))
brickarr.append(RBrick(90, 13))
brickarr.append(GBrick(80, 13))
brickarr.append(YBrick(70, 13))
brickarr.append(UBrick(60, 13))
brickarr.append(RBrick(50, 13))
#brickarr.append(GBrick(40, 13))
#brickarr.append(YBrick(30, 13))

#brickarr.append(RBrick(170, 17))
#brickarr.append(GBrick(160, 17))
brickarr.append(YBrick(150, 17))
brickarr.append(UBrick(140, 17))
brickarr.append(RBrick(130, 17))
brickarr.append(GBrick(120, 17))
brickarr.append(YBrick(110, 17))
brickarr.append(UBrick(100, 17))
brickarr.append(RBrick(90, 17))
brickarr.append(GBrick(80, 17))
brickarr.append(YBrick(70, 17))
brickarr.append(UBrick(60, 17))
brickarr.append(RBrick(50, 17))
brickarr.append(GBrick(40, 17))
brickarr.append(YBrick(30, 17))
#brickarr.append(UBrick(20, 17))
#brickarr.append(RBrick(10, 17))

#brickarr.append(YBrick(150, 21))
#brickarr.append(UBrick(140, 21))
brickarr.append(RBrick(130, 21))
brickarr.append(GBrick(120, 21))
brickarr.append(YBrick(110, 21))
brickarr.append(UBrick(100, 21))
brickarr.append(RBrick(90, 21))
brickarr.append(GBrick(80, 21))
brickarr.append(YBrick(70, 21))
brickarr.append(UBrick(60, 21))
brickarr.append(RBrick(50, 21))
#brickarr.append(GBrick(40, 21))
#brickarr.append(YBrick(30, 21))

#brickarr.append(RBrick(130, 25))
brickarr.append(XBrick(120, 25))
brickarr.append(YBrick(110, 25))
brickarr.append(UBrick(100, 25))
brickarr.append(RBrick(90, 25))
brickarr.append(GBrick(80, 25))
brickarr.append(YBrick(70, 25))
brickarr.append(XBrick(60, 25))
#brickarr.append(RBrick(50, 25))

initial_time = int(time.time())


colour_array = [Back.RED, Back.YELLOW, Back.GREEN]
strength_array = [3, 2, 1]
frame = -1

while True:
	frame += 1
	if(frame > 2):
		frame = 0
	letter = input_to()

	display_arr = copy.deepcopy(blank_arr)
	print("\033[H\033[J", end="")
	display_arr = lives.display(display_arr)
	display_arr = paddle.display(Back.BLUE, ' ', display_arr)
	display_arr = ball.display('⚪', display_arr)
	display_arr = timer.display(((int(time.time())) - initial_time), display_arr)
	scoreval = 0
	if(((int(time.time())) - initial_time) > 10):
		movedown = True
	for i in range(43):
		if(i == 36 or i == 42):
			if(brickarr[i].hit == 0):
				brickarr[i].color = colour_array[frame]
				brickarr[i].strength = strength_array[frame]
		if(brickarr[i].strength != 0):
			if(brickarr[i].y + brickarr[i].height == 38):
				gameover = True
			display_arr = brickarr[i].display(display_arr)
		else:
			scoreval += 1
	display_arr = score.display(scoreval, display_arr)
	if(scoreval == 43):
		print("You win!")
		break
	for i in range(6):
		#check if powerup is falling
		if(powarr[i].active == 1):
			display_arr = powarr[i].display(display_arr)
			#check if it can fall any further, if yes then continue
			if(powarr[i].drop() == False):
				powarr[i].active = 0
			#check if it has hit paddle, then check id and apply powerup
			if(((powarr[i].y + 1) == paddle.y) and (powarr[i].x >= paddle.x) and ((powarr[i].x + 1) <= (paddle.x+paddle.width))):
				if(powarr[i].id == 1):
					paddle.width += 10
					powarr[i].active = 2
				elif(powarr[i].id == 2):
					paddle.width -= 10
					powarr[i].active = 2
				elif(powarr[i].id == 3):
					ball.fast = 1
					if(ball.vx < 0):
						ball.vx -= 1
					else:
						ball.vx += 1
					if(ball.vy < 0):
						ball.vy -= 1
					else:
						ball.vy += 1
					powarr[i].active = 2
				elif(powarr[i].id == 4):
					ball2 = Ball(2, 1, ball.x, ball.y)
					ball2.vy = -(ball.vy)
					ball2.vx = -(ball.vx)
					ball2.moving = 1
					ballvar = 1
					powarr[i].active = 2
				elif(powarr[i].id == 5):
					ball.thru = 1
					powarr[i].active = 2
				elif(powarr[i].id == 6):
					ball.stick = 1
					powarr[i].active = 2
				#add remaining powerups here
		#check if powerup is applied, if yes then decrease time
		if(powarr[i].active == 2):
			powarr[i].time -= 1
			#check if time is up, if yes then de-apply powerup
			if(powarr[i].time == 0):
				if(powarr[i].id == 1):
					paddle.width -= 10
					powarr[i].active = 0
				elif(powarr[i].id == 2):
					paddle.width += 10
					powarr[i].active = 0
				elif(powarr[i].id == 3):
					ball.fast = 0
					if(ball.moving == 1 and ball.first == 0):
						if(ball.vx < 0):
							ball.vx += 1
						else:
							ball.vx -= 1
						if(ball.vy < 0):
							ball.vy += 1
						else:
							ball.vy -= 1
					else:
						ball.vx = 1
						ball.vy = 1
					powarr[i].active = 0
				elif(powarr[i].id == 4):
					ballvar = 0
					powarr[i].active = 0
				elif(powarr[i].id == 5):
					ball.thru = 0
					powarr[i].active = 0
				elif(powarr[i].id == 6):
					ball.stick = 0
					powarr[i].active = 0
				#add remaining powerups here
	
	if(ballvar == 1):
		display_arr = ball2.display('⚪', display_arr)

	display_arr = ''.join(display_arr)
	print(display_arr)

	if(lives.value == 0 or gameover == True):
		print("Game Over")
		break

	if(letter == 'd'):
		if(paddle.move(1)):
			if(ball.moving == 0 and ball.first == 1):
				ball.x += 1
	elif(letter == 'a'):
		if(paddle.move(-1)):
			if(ball.moving == 0 and ball.first == 1):
				ball.x -= 1
	elif(letter == 's'):
		ball.moving = 1
		ball.fail = 0
	elif(letter == 'q'):
		break

	if(ball.moving == 1):
		brickarr = ball.move(paddle, brickarr, movedown)
	if(ballvar == 1):
		if(ball2.moving == 1):
			brickarr = ball2.move(paddle, brickarr, movedown)
		if(ball2.fail == 1):
			ballvar = 0
	if(ball.fail == 1):
		lives.value -= 1
		paddle.x = 79
		paddle.y = 38
		ball.fail = 0

	time.sleep(t)