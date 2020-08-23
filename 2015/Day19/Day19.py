import re

def main():

    replacements = []
    molecules = []

    with open("input.txt", "r") as input_file:
        for line in input_file:
            s = line.split()
            if len(s) == 3:
                replacements.append([s[0], s[2]])
            elif len(s) == 1:
                orig_molecule = s[0]

    for replacement in replacements:
        matches = re.finditer(replacement[0], orig_molecule)
        match_positions = [match.start() for match in matches]
        for pos in match_positions:
            new_molecule = orig_molecule[:pos] + replacement[1] + orig_molecule[pos+len(replacement[0]):len(orig_molecule)]
            molecules.append(new_molecule)

    print(len(set(molecules)))

main()