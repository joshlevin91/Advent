import copy

def occupied(cubes, new_cubes, pos, add):
    occ = 0
    move = [-1, 0, 1]
    neighbors = [(pos[0]+dx, pos[1]+dy, pos[2]+dz) for dx in move for dy in move for dz in move if (dx != 0 or dy != 0 or dz != 0)]
    for npos in neighbors:
        if add and npos not in cubes:
            if occupied(cubes, new_cubes, npos, False) == 3:
                new_cubes[npos] = '#'
            else:
                new_cubes[npos] = '.'
        elif cubes.get(npos) == '#':
            occ += 1
    return occ

def occupied2(cubes, new_cubes, pos, add):
    occ = 0
    move = [-1, 0, 1]
    neighbors = [(pos[0]+dw, pos[1]+dx, pos[2]+dy, pos[3]+dz) for dw in move for dx in move for dy in move for dz in move if (dw != 0 or dx != 0 or dy != 0 or dz != 0)]
    for npos in neighbors:
        if add and npos not in cubes:
            if occupied2(cubes, new_cubes, npos, False) == 3:
                new_cubes[npos] = '#'
            else:
                new_cubes[npos] = '.'
        elif cubes.get(npos) == '#':
            occ += 1
    return occ

def round(cubes):
    new_cubes = copy.deepcopy(cubes)
    for pos in cubes:
        # occ = occupied(cubes, new_cubes, pos, True) #p1
        occ = occupied2(cubes, new_cubes, pos, True) #p2
        if cubes[pos] == '#' and occ != 2 and occ != 3:
            new_cubes[pos] = '.'
        elif cubes[pos] == '.' and occ == 3:
            new_cubes[pos] = '#'
    return new_cubes

cubes = {}
with open('Day17.txt') as file:
    lines = file.read().splitlines()
    for i, row in enumerate(lines):
        for j, value in enumerate(row):
            # cubes[(i, j, 0)] = value #p1
            cubes[(0, i, j, 0)] = value #p2

cycles = 6
for _ in range(cycles):
    cubes = round(cubes)

print(sum(state == '#' for state in cubes.values()))