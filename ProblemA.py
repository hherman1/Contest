import fileinput

string = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_."
sourceFile = fileinput.input()
def shift(n,ins):
	val = ""
	s = ins.strip('\n')
	for c in s:
		ind = string.find(c)
		out = string[(ind + n) % len(string)]
		val = out + val
	return val
for line in sourceFile:
	inputs = line.split(" ")
	if line == "0\n" or line == "0":
		pass
	else:
		print(shift(int(inputs[0]),inputs[1]))
