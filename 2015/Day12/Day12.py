def main():

	num = ""
	total = 0
	with open("input.txt", "r") as input_file:
		for line in input_file:
			for char in line:
				if char == '-':
					num += char
				elif char.isnumeric():
					num += char
				elif num.lstrip('-').isnumeric():
					total += int(num)
					num = ""
				else:
					num = ""

	print(total)

main()