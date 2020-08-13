def main():

	nCode = 0
	nMem = 0
	nNewCode = 0

	with open("input.txt", "r") as input_file:
		lines = input_file.read().splitlines()
		for line in lines:
			nCode += len(line)
			nMem += len(eval(line))
			nNewCode += len(line) + 2 + line.count('\\') + line.count('\'') + line.count('\"')

	print("Answer to part one =", nCode - nMem)
	print("Answer to part two =", nNewCode - nCode)

main()