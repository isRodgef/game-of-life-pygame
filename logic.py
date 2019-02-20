import numpy as np

class Arena:
	def __init__(self,underpop,overpop,reproduce,grid):
		self.under = underpop
		self.over = overpop
		self.reproduce = reproduce
		self.grid = grid	

	def __mates__(self,x,y,alive):
		matches = 0
		max_x ,max_y = np.shape(self.grid)
		if x != 0:
			if self.grid[x - 1][y] == alive:
				matches+= 1
		if x != max_x - 1:
			if self.grid[x + 1][y] == alive:
				matches+= 1
		if y != 0:
			if self.grid[x][y - 1] == alive:
				matches+= 1
		if y != max_y - 1:
			if self.grid[x][y + 1] == alive:
				matches+= 1

		return matches 		  

	def run(self, iterations):
		max_x,max_y = np.shape(self.grid)
		for i in range(iterations):
			for j in range(max_x):
				for k in range(max_y):
					if self.__mates__(j,k,True) >= self.over:
						self.grid[j][k] = False
					elif self.__mates__(j,k,True) >= self.under:
						self.grid[j][k] = False 
					elif self.__mates__(j,k,False) == self.reproduce:
						self.grid[j][k] = True
		return self.grid



 		 
