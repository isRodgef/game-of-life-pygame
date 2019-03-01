from logic import Arena
import pygame
from pygame.locals import *
from sys import exit
import random
from time import sleep

if __name__ == '__main__':
	RED = (0xff,0,0)
	BLUE = (0,0,0xff)
	BLACK = (0,0,0)
	pygame.init()
	screen = pygame.display.set_mode((200, 200), 0, 32)
	pygame.display.set_caption("Game of life!")
	x = [[random.choice((True,False)) for i in range(10)] for j in range(10)]
	a = Arena(0,4,3,x)
	val = None
	counter = 0
	while True:
		for event in pygame.event.get():
			if event.type == QUIT:
				exit()	
		
		val = a.run(1)
		a.grid = val
		counter += 1
		for i in  range(a.x):
			for j in range(a.y):
				if val[i][j]:
					pygame.draw.rect(screen, BLUE, (i * 10 ,j * 10,  (i +1) * 10, (j+1) * 10))
				else:
					pygame.draw.rect(screen, BLACK, (i * 10 ,j * 10, (i+1) * 10, (j +1) *10))
				sleep(0.1)
				pygame.display.update()
