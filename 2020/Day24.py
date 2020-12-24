import re
from itertools import permutations

def adj_black_tiles(pos):
    abt = 0
    for dr in drs:
        if tuple([sum(x) for x in zip(pos,dr)]) in tiles:
            abt += 1
    return abt

def move(pos, dr):
    if dr == 'e':
        pos[0] += 1
        pos[1] -= 1
    elif dr == 'se':
        pos[1] -= 1
        pos[2] += 1
    elif dr == 'sw':
        pos[0] -= 1
        pos[2] += 1
    elif dr == 'w':
        pos[0] -= 1
        pos[1] += 1
    elif dr == 'nw':
        pos[1] += 1
        pos[2] -= 1
    elif dr == 'ne':
        pos[0] += 1
        pos[2] -= 1
    return pos

tiles = set()
drs = list(permutations([0, 1, -1]))
days = 100

with open('Day24.txt') as file:
    lines = [line.strip() for line in file if line.strip()]

for line in lines:
    pos = [0, 0, 0]
    while line:
        dr = re.search('^(e|se|sw|w|nw|ne)', line).group(1)
        line = re.sub('^(e|se|sw|w|nw|ne)', '', line)
        pos = move(pos, dr)
    pos = tuple(pos)
    if pos not in tiles:
        tiles.add(pos)
    else:
        tiles.remove(pos)

for _ in range(days):
    checked = set()
    new_tiles = set(tiles)
    for tile in tiles:

        abt = adj_black_tiles(tile)
        if abt == 0 or abt > 2:
            new_tiles.remove(tile)

        for dr in drs:
            pos = tuple([sum(x) for x in zip(tile,dr)])
            if pos in checked:
                continue
            if adj_black_tiles(pos) == 2:
                new_tiles.add(pos)
            checked.add(pos)

    tiles = new_tiles

print(len(new_tiles))