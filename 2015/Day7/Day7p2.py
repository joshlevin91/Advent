from shutil import copyfile

def get_value_of_token(s, d):
	if s.isnumeric():
		return int(s)
	else:
		return d.get(s)

def main():
	with open("input.txt", "r") as input_file:

		lines = input_file.readlines()
		wire_dict = {}
		i = 0
		found_a = False
		first_a = 0

		# Iterate through lines of file, assigning signals to wires if their inputs are known
		# Remove line once wire has been assigned and keep iterating until no lines remain
		while lines:
			line = lines[i]
			tokens = line.rstrip().split(' ')

			if tokens[1] == "->" and (tokens[0].isnumeric() or tokens[0] in wire_dict):

				if found_a and tokens[2] == 'b':
					x = first_a
				else:
					x = get_value_of_token(tokens[0], wire_dict)

				wire_dict.update({tokens[2] : x})
				lines.remove(line)

			elif tokens[1] == "AND" and (tokens[0].isnumeric() or tokens[0] in wire_dict) \
			and (tokens[2].isnumeric() or tokens[2] in wire_dict):

				x = get_value_of_token(tokens[0], wire_dict)
				y = get_value_of_token(tokens[2], wire_dict)

				wire_dict.update({tokens[4] : x & y})
				lines.remove(line)

			elif tokens[1] == "OR"  and (tokens[0].isnumeric() or tokens[0] in wire_dict) \
			and (tokens[2].isnumeric() or tokens[2] in wire_dict):

				x = get_value_of_token(tokens[0], wire_dict)
				y = get_value_of_token(tokens[2], wire_dict)

				wire_dict.update({tokens[4] : x | y})
				lines.remove(line)

			elif tokens[0] == "NOT" and (tokens[1].isnumeric() or tokens[1] in wire_dict):

				x = get_value_of_token(tokens[1], wire_dict)

				wire_dict.update({tokens[3] : ~x})
				lines.remove(line)

			elif tokens[1] == "LSHIFT" and (tokens[0].isnumeric() or tokens[0] in wire_dict):

				x = get_value_of_token(tokens[0], wire_dict)

				wire_dict.update({tokens[4] : x << int(tokens[2])})
				lines.remove(line)

			elif tokens[1] == "RSHIFT" and (tokens[0].isnumeric() or tokens[0] in wire_dict):

				x = get_value_of_token(tokens[0], wire_dict)

				wire_dict.update({tokens[4] : x >> int(tokens[2])})
				lines.remove(line)

			# Go to next line
			# If at end of lines, go to first line
			i += 1
			if i >= len(lines):
				i = 0

			# Once a is found for first time, reset lines and wire dictionary
			if not lines and not found_a:

				input_file.seek(0)
				lines = input_file.readlines()

				first_a = wire_dict.get('a')
				wire_dict.clear()
				found_a = True

	print(wire_dict.get('a'))
main()