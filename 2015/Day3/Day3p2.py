def add_to_visited_houses(char, location, houses_visited):
	if char == '^':
		location[0] += 1
	elif char == 'v':
		location[0] -= 1
	elif char == '>':
		location[1] += 1
	elif char == '<':
		location[1] -= 1

	houses_visited.add(tuple(location))

def main():
	santa_location = [0,0]
	robo_santa_location = [0,0]
	houses_visited = {tuple(santa_location)}

	with open("input.txt", 'r') as input_file:

		counter = 0

		for line in input_file:
			for char in line:
				if (counter % 2 == 0):
					add_to_visited_houses(char, santa_location, houses_visited)
				else:
					add_to_visited_houses(char, robo_santa_location, houses_visited)

				counter += 1

	print('Number of houses visited:', len(houses_visited))

main()