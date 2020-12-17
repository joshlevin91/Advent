import copy

def occupied(seats, row, col):
    occ = 0
    adj_rows = [row-1, row, row+1]
    adj_cols = [col-1, col, col+1]
    adj = [(r, c) for r in adj_rows for c in adj_cols if (r != row or c != col) and 0 <= r < len(seats) and 0 <= c < len(seats[0])]
    for r, c in adj:
        if seats[r][c] == '#':
            occ += 1
    return occ

def occupied2(seats, row, col):
    occ = 0
    move = [-1, 0, 1]
    dirs = [(dr, dc) for dr in move for dc in move if (dr != 0 or dc != 0)]
    for dr, dc in dirs:
        n = 1
        while True:
            r = row + n*dr
            c = col + n*dc
            if r < 0 or r >= len(seats) or c < 0 or c >= len(seats[0]) or seats[r][c] == 'L':
                break
            elif seats[r][c] == '#':
                occ += 1
                break
            n += 1
    return occ

def round(seats):
    new_seats = copy.deepcopy(seats)
    for i, row in enumerate(seats):
        for j, seat in enumerate(row):
            if seat == 'L' and occupied(seats, i, j) == 0:
                new_seats[i][j] = '#'
            if seat == '#' and occupied(seats, i, j) >= 4:
                new_seats[i][j] = 'L'
    return new_seats

def round2(seats):
    new_seats = copy.deepcopy(seats)
    for i, row in enumerate(seats):
        for j, seat in enumerate(row):
            if seat == 'L' and occupied2(seats, i, j) == 0:
                new_seats[i][j] = '#'
            if seat == '#' and occupied2(seats, i, j) >= 5:
                new_seats[i][j] = 'L'
    return new_seats

with open('Day11.txt') as file:
    seats = [list(seat) for seat in file.read().splitlines()]

while True:
    # new_seats = round(seats) #p1
    new_seats = round2(seats) #p2
    if new_seats == seats:
        break
    seats = new_seats

print(sum(row.count('#') for row in seats))