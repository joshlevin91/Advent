import re

def main():

	n_nice_strings = 0;

	with open("input.txt", 'r') as input_file:

		for line in input_file:
			
			# Contains a pair of any two letters that appear at least twice in the string without overlapping
			pair = False
			for i in range(len(line)-1):
				for j in range(len(line)-1):
					if abs(i-j) > 1 and line[i] == line[j] and line[i+1] == line[j+1]:
						pair = True
						break

			if not pair:
				continue

			# Contains at least one letter which repeats with exactly one letter between them
			repeat = False
			for i in range(len(line)-2):
				if line[i] == line[i+2]:
					repeat = True
					break
					
			if not repeat:
				continue

			n_nice_strings += 1

	print("Number of nice strings:", n_nice_strings)

main()