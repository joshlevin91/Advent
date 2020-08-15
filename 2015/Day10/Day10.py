def main():

	seq = "1113122113"

	for k in range(50):

		new_seq = ""

		dig = seq[0]
		occ = 1
		
		for i in range(1, len(seq)):

			if dig == seq[i]:
				occ += 1
			else:
				new_seq += str(occ) + dig
				dig = seq[i]
				occ = 1

		new_seq += str(occ) + dig
		seq = new_seq

	print (len(seq))

main()