floor = 0
position = 0
basementFound = False

inputFile = open("input.txt")
inputString = inputFile.read()

for i in range(len(inputString)):
	if inputString[i] == '(':
		floor += 1
	elif inputString[i] == ')':
		floor -= 1

	position += 1

	if floor < 0 and not basementFound:
		print("position =", position)
		basementFound = True

print("floor =", floor)