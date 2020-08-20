import re

# Find all combinations of n numbers that sum to total
def get_combinations(n, total, x, pre = []):
    if total == 0:
        x.append(pre + [0]*(n))
        return 

    if n == 1:
        x.append(pre + [total])
        return 

    for i in range(total+1):
        get_combinations(n-1, total-i, x, pre + [i])

def main():

	total = 100
	desired_calories = 500

	with open("input.txt", "r") as input_file:

		ingredients = {}
		tokens = []

		for line in input_file:

			tokens = re.split(': |, | ', line.rstrip('\n'))

			ingredients[tokens[0]] = {'capacity' : int(tokens[2]),
			                          'durability' : int(tokens[4]),
			                          'flavor' : int(tokens[6]),
			                          'texture' : int(tokens[8]),
			                          'calories' : int(tokens[10])}
		
	combinations = []
	get_combinations(len(ingredients), total, combinations)
	
	high_score = 0
	for comb in combinations:

		capacity = 0
		durability = 0
		flavor = 0
		texture = 0
		calories = 0

		i = 0
		for ingredient in ingredients.values():

			capacity += comb[i]*ingredient['capacity']
			durability += comb[i]*ingredient['durability']
			flavor += comb[i]*ingredient['flavor']
			texture += comb[i]*ingredient['texture']
			calories += comb[i]*ingredient['calories']

			i += 1

		score = 0
		if capacity >= 0 and durability >= 0 and flavor >= 0 and texture >= 0 and calories == desired_calories:
			score = capacity*durability*flavor*texture

		if score > high_score:
			high_score = score

	print("Highest score:", high_score)

main()