inputFile = open("input.txt", 'r')

surfaceArea = 0
ribbon = 0

while True:
	line = inputFile.readline()

	if not line:
		break

	dimStr= line.split('x')

	l = int(dimStr[0])
	w = int(dimStr[1])
	h = int(dimStr[2])

	s1 = l*w
	s2 = w*h
	s3 = l*h

	sides = [s1, s2, s3]

	# Surface Area
	smallestSide = min(sides)
	surfaceArea += 2*s1 + 2*s2 + 2*s3 + smallestSide

	# Ribbon
	dims = [l, w, h]
	dims.sort()

	ribbon += 2*dims[0] + 2*dims[1] + dims[0]*dims[1]*dims[2]

print('Total square feet of wrapping paper to order:', surfaceArea)
print('Total length of ribbon to order:', ribbon)

