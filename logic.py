import numpy as np

class Arena:
	def __init__(self,under_pop,over_pop,reproduce,grid):
		self.under = underpop
		self.over = overpop
		self.reproduce = reproduce
		self.grid
	
	def __liveMates__(self):
		pass
	def __deadMates__(self):
		pass	

	def run(self, iterations):
		max_x,max_y = np.shape(self.grid)
		for i in range(iterations):
			for j in range(max_x):
				for k in range(max_y):
					 
