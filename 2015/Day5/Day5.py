import re

def main():

	n_nice_strings = 0;

	with open("input.txt", 'r') as input_file:

		for line in input_file:
			
			# Contains at least three vowels
			if len(re.findall("[aeiouAEIOU]", line)) < 3:
				continue

			# Contains at least one letter that appears twice in a row
			if not re.search("(.)\\1", line):
				continue	

			# Does not contain the strings: ab, cd, pq, or xy
			if re.search("ab|cd|pq|xy", line):
				continue

			n_nice_strings += 1

	print("Number of nice strings:", n_nice_strings)

main()