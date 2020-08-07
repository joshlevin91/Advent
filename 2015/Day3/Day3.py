santa_location = [0,0]
houses_visited = {tuple(santa_location)}

with open("input.txt", 'r') as input_file:
	while True:
		line = input_file.readline()

		if not line:
			break

		for char in line:
			if char == '^':
				santa_location[0] += 1
			elif char == 'v':
				santa_location[0] -= 1
			elif char == '>':
				santa_location[1] += 1
			elif char == '<':
				santa_location[1] -= 1

			houses_visited.add(tuple(santa_location))

print('Number of houses visited:', len(houses_visited))