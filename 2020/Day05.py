import re

def ID(row, col):
	return 8*row + col

def binop(lowest, highest, ops):
	if len(ops) == 1:
		return int(lowest) if ops[0] == 'L' else int(highest)
	elif ops[0] == 'L':
		return binop(lowest, lowest + (highest - lowest - 1)/2, ops[1:])
	else:
		return binop(lowest + (highest - lowest + 1)/2, highest, ops[1:])

open_seat_IDs = [ID(row, col) for row in range(128) for col in range(8)]

highest_ID = 0
taken_seat_IDs = []

lines = open("Day05.txt", 'r').read().split('\n')
for line in lines:
	row = binop(0, 127, re.sub('F', 'L', line[:7]))
	col = binop(0, 7, line[7:])
	highest_ID = max(highest_ID, ID(row, col))
	open_seat_IDs.remove(ID(row,col))
	taken_seat_IDs.append(ID(row,col))

for ID in open_seat_IDs:
	if ID-1 in taken_seat_IDs and ID+1 in taken_seat_IDs:
		my_ID = ID
		break

print(highest_ID, my_ID)