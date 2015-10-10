import fileinput
import math

def wordWidth(t,P):
	return int(math.ceil(t * P * 9 / 16))
def pointSize(wordCount,maxWordCount):
	return 8 + int(math.ceil(40 * (wordCount - 4)/(maxWordCount - 4)))

list = [('apple',10),('banana',5),('grape',20),('kiwi',18),('orange',12),('strawberry',10)]
pairs = []
remainingLines = 0
curList = []
curWidth = 0
for line in fileinput.input():
	curLine = line.strip("\n").split(" ")
	if remainingLines == 0:
		if curWidth != 0:
			pairs.append((curWidth,curList))
		curWidth = int(curLine[0])
		remainingLines = int(curLine[1]) + 1
		curList = []
		if(curWidth == 0):
			break
	else:
		curList.append((curLine[0],int(curLine[1])))
	remainingLines -= 1
if(curWidth != 0):
	pairs.append((curWidth,curList))	
cldNum = 0
for (maxWidth,cList) in pairs:
	cldNum += 1
	freqList = []
	for (word,number) in cList:
		freqList.append(number)
	maxWordCount = max(freqList)
	curCloud = 0
	curLinePs = []
	curWidth = 0
	curHeight = 0
	for (word,number) in cList:
		P = pointSize(number,maxWordCount)
		if(len(curLinePs) > 0):
			curWidth += 10
		width = wordWidth(len(word),P)
		curWidth += width
		if(curWidth > maxWidth):
			curHeight += max(curLinePs)
			curWidth = width
			curLinePs = [P]
		curLinePs.append(P)
	curHeight += max(curLinePs)
	outString = "CLOUD " + str(cldNum) + ": " + str(curHeight)
	print(outString.strip("\n"))
