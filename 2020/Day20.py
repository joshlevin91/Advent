import re

with open('Day20.txt') as file:
    lines = [line.strip() for line in file if line.strip()]

tiles = {}
for line in lines:
    if re.match('^Tile', line):
        ID = re.search('Tile (.*?):', line).group(1)
        image = []
        x = 0
    else:
        row = []
        for pixel in line:
            row.append(pixel)
        image.append(row)
        tiles[ID] = image

borders = {}
for ID, image in tiles.items():
    b1 = [pixel for pixel in image[0]]
    b2 = [row[0] for row in image]
    b3 = [pixel for pixel in image[-1]]
    b4 = [row[-1] for row in image]
    borders[ID] = [b1, b2, b3, b4]

ans = 1
for ID, border in borders.items():
    count = 0
    for sID, sborder in borders.items():
        if ID == sID:
            continue
        for b in border:
            for sb in sborder:
                if sb == b or sb == list(reversed(b)):
                    count += 1
    if count == 2:
        ans *= int(ID)
print(ans)