import fileinput
houses = []
house = []
w = 0
l = 0
direction = (0,0)
position = (0,0)
houseNumber = 1
def sum_tuple(a,b):
	return (a[0] + b[0],a[1] + b[1])
def getHouse(h,t):
	return h[t[1]][t[0]]
def swap(t):
	return (t[1],t[0])
def multTuple(n,t):
	return (n * t[0],n * t[1])
def initStuff(h):
	rowN = 0
	colN = 0
	global direction
	global position
	global w
	global l
	for row in h:
		rowN += 1
		colN = 0
		for unit in row:
			colN+= 1
			position = (colN-1,rowN-1)
			if unit == '*':
				if rowN == 1:
					direction = (0,1)
				if rowN == l:
					direction = (0,-1)
				if colN == 1:
					direction = (1,0)
				if colN == w:
					direction = (-1,0)
				return

input = fileinput.input()
for line in input:
	curLine = line.strip("\n").split(" ")
	if(len(curLine) > 1):
		if w != 0:
			houses.append((houseNumber,w,l,house))
			house = []
			houseNumber += 1
		w = int(curLine[0])
		l = int(curLine[1])
		if w == 0:
			break
	else:
		house.append(curLine[0])
	
for h in houses:
	houseNumber = h[0]
	w = h[1]
	l = h[2]
	house = h[3]
	print("HOUSE " + str(houseNumber))
	initStuff(house)
	while(getHouse(house,position) != 'x'):
		if getHouse(house,position) == '/':
			direction = multTuple(-1,swap(direction))
		if getHouse(house,position) == '\\':
			direction = swap(direction)
		position = sum_tuple(position,direction)

	tempString = list(house[position[1]])
	tempString[position[0]] = '&'
	house[position[1]] = "".join(tempString)
	for l in house:
		print(l)
