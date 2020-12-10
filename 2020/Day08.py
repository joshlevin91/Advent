import re

def get_acc(instructions):
	nset = set()
	n, acc = 0, 0

	while n not in nset and n < len(instructions):

		nset.add(n)
		op = instructions[n][0]
		arg = instructions[n][1]

		if op == 'acc':
			acc += arg
			n += 1
		elif op == 'jmp':
			n += arg
		else:
			n += 1

	if n == len(instructions):
		return True, acc
	else:
		return False, acc

lines = open('Day08.txt', 'r').read().split('\n')

instructions = []
for line in lines:
	instruction = re.split(' ', line)
	op = instruction[0]
	arg = int(instruction[1].replace('+', ''))
	instructions.append([op, arg])

print(get_acc(instructions)[1])

for i in range(len(instructions)):

	if instructions[i][0] == 'jmp':
		instructions[i][0] = 'nop'
		acc = get_acc(instructions)
		if acc[0]:
			print(acc[1])
			break
		else:
			instructions[i][0] = 'jmp'

	elif instructions[i][0] == 'nop':
		instructions[i][0] = 'jmp'
		acc = get_acc(instructions)
		if acc[0]:
			print(acc[1])
			break
		else:
			instructions[i][0] = 'nop'