lines = open("Day06.txt", 'r').read().split('\n')

any_yes = 0
all_yes = 0
group = []

for line in lines:

	if not line:
		any_yes += len(set([ans for person in group for ans in person]))
		all_yes += len(set(group[0]).intersection(*group))
		group.clear()
		continue

	person = [c for c in line]
	group.append(person)

print(any_yes, all_yes)