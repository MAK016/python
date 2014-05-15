#!/usr/bin/python
import random , sys
class board:
	grid = []
	def __init__(self,a,b):
		self.grid = []
		self.a = a
		self.b = b
		for i in range(a):
			self.grid.append([])
			for j in range(b):
				self.grid[i].append(-1)
	def printGrid(self):
		i = 0
		j = 0
		for row in self.grid:
			i += 1
			for val in row:
				j+=1
				if(val != -1):
					sys.stdout.write('\033[1m')
					sys.stdout.write('%4d' %val)
					sys.stdout.write('\033[0m')
				else:
					sys.stdout.write('%4d' %val)
				if (j % 3 == 0):
					sys.stdout.write("|")
			sys.stdout.write("\n")
			if ((i%3 == 0) and (i != 9)):
				sys.stdout.write("---------------------------------------\n")


	def populate(self,z):
		for i in range(z):
			a1 = random.randint(0 , self.a-1)
			#print(a1)
			b1 = random.randint(0 , self.b-1)
			#print(b1)
			c = random.randint(1 , 9)
			self.grid[a1][b1]=c

	def clear(self,a,b):
		self.grid[a][b] = -1

	def add(self,a,b,x):
		self.grid[a][b] = x

	def checkValid(self):
		ret = True
		for i in range(0,9):
			for j in range(0,9):
				if(self.checkRow(i)):
					print("tru")
				
				if(self.checkCol(j)):
					print("trucols")
				ret &= (self.checkRow(i) and self.checkCol(j))
		return ret

	def checkRow(self,x):
		array = []
		for i in range(1,10):
			array.append(i)
		for z in self.grid[x]:
			if(array.count(z)==1):
				#print(array)
				array.remove(z)
				#print(True)
			else:
				return False
		return True

	def checkCol(self,x):
		array = []
		for i in range(1,10):
			array.append(i)
		for t in range(0,9):
			z = self.grid[x][t]
			if(array.count(z)==1):
				#print(array)
				array.remove(z)
				#print(True)
			else:
				return False
		return True

	def validRow(self,a,c):
		for z in self.grid[a]:
			if(z == c):
				return False
		return True

	def validCol(self,b,c):
		for t in range(0,9):
			z = self.grid[t][b]
			if(z == c):
				return False
		return True

	def validBox(self,a,b,c):
		x = 3*((int)(a/3))
		y = 3*((int)(b/3))
		for i in range(x,x+3):
			for j in range(y,y+3):
				z = self.grid[j][i]
				if(z == c):
					return False
		return True

	def solve(self,a,b):
		print("solving",a,",",b)
		self.printGrid()
		for t in range(1,10):
			#print("added",t)
			#print(self.validRow(a,t))
			#print(self.validCol(b,t))
			#print(self.validBox(a,b,t))
			if(self.validRow(a,t) and self.validCol(b,t) and self.validBox(a,b,t)):
				self.add(a,b,t)
				if(a == 8 and b == 8):
					#print("solved")
					return True
				if(b == 8):
					#print("nextrow")
					if(self.solve(a+1,0)==False):
						continue
					else:
						return True
				else:
					#print(t,"in",a,",",b)
					if(self.solve(a,b+1)==False):
						continue
					else:
						return True
			else:
				self.clear(a,b)
		return False



print sys.version

'''x = board(9,9)
#x.populate(6)
print(x.validRow(0,1))
print(x.validCol(0,1))
x.solve(0,0)
x.checkValid()
x.printGrid()'''