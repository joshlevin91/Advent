import re

def main():

    replacements = []
    molecule_found = False
    new_molecules = [[]]
    molecules_tried = []

    with open("input.txt", "r") as input_file:
        for line in input_file:
            s = line.split()
            if len(s) == 3:
                replacements.append([s[0], s[2]])
            elif len(s) == 1:
                med_molecule = s[0]

    replacements.sort(key=lambda t: len(t[1]), reverse = True)

    new_molecule = med_molecule
    new_molecules.append([new_molecule, 0])
    s = 0
    for i in range(100):
        i = 0
        for replacement in replacements[s:]:
            i += 1
            matches = re.finditer(replacement[1], new_molecule)
            match_positions = [match.start() for match in matches]
            if len(match_positions) >= 1:
                pos = match_positions[0]
                new_molecule = new_molecule[:pos] + replacement[0] + new_molecule[pos+len(replacement[1]):len(new_molecule)]
                if new_molecule in molecules_tried:
                    continue
                new_molecules.append([new_molecule, i])
                molecules_tried.append(new_molecule)
                s = 0
                print("\nmolecule:", new_molecules[-2][0])
                print("replacement:", replacement[1])
                break
            if replacement == replacements[-1]:
                s = new_molecules[-1][1]
                new_molecules.pop()
                new_molecule = new_molecules[-1][0] 
                break
    print("\n", new_molecule)

main()