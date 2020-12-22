from collections import deque

with open('Day22.txt') as file:
    lines = [line.strip() for line in file if line.strip()]

d1 = deque()
d2 = deque()
player2 = False
for line in lines:
    if line == 'Player 1:':
        continue
    if line == 'Player 2:':
        player2 = True
        continue
    if player2:
        d2.append(int(line))
    else:
        d1.append(int(line))

while d1 and d2:
    t1 = d1.popleft()
    t2 = d2.popleft()

    if t1 > t2:
        d1.append(t1)
        d1.append(t2)
    else:
        d2.append(t2)
        d2.append(t1)

if d1:
    wd = d1
else:
    wd = d2

score = 0
for i, card in enumerate(wd):
    score += (len(wd)-i)*card
print(score)
