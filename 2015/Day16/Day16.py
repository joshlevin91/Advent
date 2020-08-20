import re

def main():

    Sues = {}
    tokens = []

    with open("input.txt", "r") as input_file:
        for line in input_file:

            tokens = re.split(': |, | ', line.rstrip('\n'))
            Sues[tokens[1]] = {tokens[2] : int(tokens[3]), tokens[4] : int(tokens[5]), tokens[6] : int(tokens[7])}
    
    i = 0
    for Sue in Sues.values():
        i += 1
        if "children" in Sue and Sue["children"] != 3:
            continue
        if "cats" in Sue and Sue["cats"] <= 7:
            continue
        if "samoyeds" in Sue and Sue["samoyeds"] != 2:
            continue
        if "pomeranians" in Sue and Sue["pomeranians"] >= 3:
            continue
        if "akitas" in Sue and Sue["akitas"] != 0:
            continue
        if "vizslas" in Sue and Sue["vizslas"] != 0:
            continue
        if "goldfish" in Sue and Sue["goldfish"] >= 5:
            continue
        if "trees" in Sue and Sue["trees"] <= 3:
            continue
        if "cars" in Sue and Sue["cars"] != 2:
            continue
        if "perfumes" in Sue and Sue["perfumes"] != 1:
            continue
        else:
            break

    print("Sue", i, "got me the gift")

main()