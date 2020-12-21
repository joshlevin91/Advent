import re

with open('Day21.txt') as file:
    lines = [line.strip() for line in file if line.strip()]

ingredients = [] # List of ingredients (includes duplicates for different foods)
allergens = {} # Key -> allergen, Value -> ingredients that possibly contain allergen
for line in lines:
    ingredients_list = re.search('(.*) \(', line).group(1).split(' ')
    allergens_list = re.search('contains (.*)\)', line).group(1).split(', ')

    for i in ingredients_list:
        ingredients.append(i)

    for a in allergens_list:
        if a not in allergens:
            allergens[a] = ingredients_list
        else:
            allergens[a] = [existing_a for existing_a in allergens[a] if existing_a in ingredients_list]

# Remove ingredients that could contain allergens
for ilist in allergens.values():
    for i in ilist:
        ingredients = list(filter((i).__ne__, ingredients))
print(len(ingredients)) #p1

# Determine mapping between allergens and ingredients
taken_allergens = set()
while any(len(ilist) != 1 for ilist in allergens.values()):
    for a, ilist in allergens.items():
        if len(ilist) == 1:
            taken_allergens.add(ilist[0])
        else:
            for ta in taken_allergens:
                allergens[a] = list(filter((ta).__ne__, allergens[a]))

# Determine canonical dangerous ingredients list
cdil = ''
for a in sorted(allergens):
    if cdil:
        cdil = cdil + ',' + allergens[a][0]
    else:
        cdil = allergens[a][0]
print(cdil)