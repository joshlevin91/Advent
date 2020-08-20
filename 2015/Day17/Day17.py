import itertools

def main():

    containers = []
    with open("input.txt", "r") as input_file:
        for line in input_file:
            containers.append(int(line.rstrip('\n')))

    n = 0
    min_num_containers = 100
    min_combinations = 0

    for L in range(0, len(containers)+1):
        for subset in itertools.combinations(containers, L):
            if sum(subset) == 150:
                n += 1
                if len(subset) < min_num_containers:
                    min_num_containers = len(subset)
                    min_combinations = 1
                elif len(subset) == min_num_containers:
                    min_combinations += 1

    print("There are", n, "different combinations of containers")
    print("You can fill the minimum number of containers", min_combinations, "different ways")

main()