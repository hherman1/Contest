import fileinput
import math 

def pretty(grid):
	tGrid = []
	for l in grid:
		tl = l.append('\n')
		tGrid.append("".join(l))
	return "".join(tGrid)

def getDigits(n):
	return len(str(n))
def getDim(n):
	return 5 + 4 * getDigits(n)


def genGrid(n,m):
	grid = []
	for i in range(0,getDim(m)):
		row = []
		for j in range(0,getDim(n)):
			row.append(' ')
		grid.append(row)
	return grid

def drawHorizontal(grid,row,x1,x2):
	for i in range(x1,x2):
		grid[row][i] = '-'
	grid[row][x1] = '+'
	grid[row][x2] = '+'

def drawVertical(grid,col,y1,y2):
	for i in range(y1,y2):
		grid[i][col] = '|'
	grid[y1][col] = '+'
	grid[y2][col] = '+'

def drawBorders(grid,x1,y1,x2,y2):
	drawHorizontal(grid,y1,x1,x2)
	drawHorizontal(grid,y2,x1,x2)
	drawVertical(grid,x1,y1,y2)
	drawVertical(grid,x2,y1,y2)

def placeMVertical(grid,col,m):
	sm = str(m)
	for i in range(0,len(sm)):
		grid[4 + i*4][col] = sm[i] 

def placeNHorizontal(grid,row,n):
	sn = str(n)
	for i in range(0,len(sn)):
		grid[row][4 + i*4] = sn[i] 
		

def drawSubGrids(grid,n,m):
	sn = str(n)
	sm = str(m)
	drawBorders(grid,2,2,getDim(n)-3,getDim(m)-3)
	for i in range(0,getDigits(n)):
		for j in range(0,getDigits(m)):
			drawDiagonal(grid,2+i*4,6+j*4,4)
			drawBorders(grid,2 + i * 4,2 + j * 4,6 + i * 4, 6 + j * 4)
			drawValue(grid,int(sn[i]),int(sm[j]),2+i*4,2+j*4)

def drawDiagonal(grid,x1,y1,l):
	for i in range(0,l):
		grid[y1 - i][x1 + i] = '/'

def drawValue(grid,i,j,x1,y1):
	sv = str(i*j)
	if (len(sv) == 2):
		grid[y1+1][x1+1] = sv[0]
		grid[y1+3][x1+3] = sv[1]
	else:
		grid[y1+1][x1+1] = str(0)
		grid[y1+3][x1+3] = sv[0]

def drawResultBottom(grid,n,m):
	res = n * m
	sres = str(res) 
	for i in range(0,getDigits(n)):
		grid[getDim(m)-2][i*4 + 3] = sres[i + len(sres) - getDigits(n)]
		grid[getDim(m)-2][i*4 + 1] = '/'

def drawResultLeft(grid,n,m):
	res = n * m
	sres = str(res) 
	remDigits = len(sres) - getDigits(n) - 1
	for i in range(remDigits,-1,-1):
		grid[getDim(m)-4*(remDigits - i)-4][1] = sres[i]
		grid[getDim(m)-4*(remDigits - i)-2][1] = '/'

def setupGrid(g,n,m):
	drawBorders(g,0,0,getDim(n)-1,getDim(m)-1)
	drawSubGrids(g,n,m)
	placeNHorizontal(g,1,n)
	placeMVertical(g,getDim(n)-2,m)
	drawResultBottom(g,n,m)
	drawResultLeft(g,n,m)

for line in  fileinput.input():
	ins = line.strip("\n").split(" ")
	n = int(ins[0])
	m = int(ins[1])
	if(n + m == 0):
		break
	g = genGrid(n,m)
	setupGrid(g,n,m)
	print(pretty(g))
