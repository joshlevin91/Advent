import numpy

def p1():

    pos = 0
    trees = 0

    with open("Day03.txt", "r") as input_file:

        for line in input_file:
            line = line.rstrip('\n')

            temp_pos = pos % len(line)

            if line[temp_pos] == '#':
                trees += 1

            pos += 3

    print(trees)
    

def p2():

    positions = [0]*5
    trees = [0]*5
    right = [1, 3, 5, 7, 1]
    down = [1, 1, 1, 1, 2]

    with open("Day03.txt", "r") as input_file:

        n_line = 0

        for line in input_file:
            line = line.rstrip('\n')

            for i in range(5):

                if n_line % down[i] != 0:
                    continue

                temp_pos = positions[i] % len(line)

                if line[temp_pos] == '#':
                    trees[i] += 1

                positions[i] += right[i]

            n_line += 1

    print(numpy.prod(trees))

p1()
p2()
