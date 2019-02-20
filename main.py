from logic import Arena

if __name__ == '__main__':
	x = [[True for i in range(10)] for j in range(10)]
	a = Arena(2,3,5,x)
	print(a.run(10))
