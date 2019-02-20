from logic import Arena
import pygame
from pygame.locals import *
from sys import exit
import random


if __name__ == '__main__':
	RED = (0xff,0,0)
	BLUE = (0,0,0xff)
	pygame.init()
	screen = pygame.display.set_mode((640, 480), 0, 32)
	pygame.display.set_caption("Game of life!")
	x = [[random.randint(1,95) % 10 != 0 for i in range(5)] for j in range(5)]
	a = Arena(1,4,3,x)
	val = None
	counter = 0
	while True:
		for event in pygame.event.get():
			if event.type == QUIT:
				exit()	
		
		if val == a:
			print (counter)
			break
		val = a.run(1)
		counter += 1
		for i in  range(a.x):
			for j in range(a.y):
				if val[i][j]:
					pygame.draw.rect(screen, BLUE, (i + 10 ,j + 10, i+ 290, j+290))
				else:
					pygame.draw.rect(screen, RED, (i + 10 ,j + 10, i+ 290, j + 290))
		pygame.display.update()
