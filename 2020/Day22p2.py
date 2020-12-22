from collections import deque
import itertools

def game(d1, d2):

    rounds = set()
    while d1 and d2:

        t1 = d1.popleft()
        t2 = d2.popleft()

        if len(d1) >= t1 and len(d2) >= t2:

            s1 = deque(itertools.islice(d1, 0, t1))
            s2 = deque(itertools.islice(d2, 0, t2))
            winner, _ = game(s1, s2)

            if winner == 1:
                d1.append(t1)
                d1.append(t2)
            else:
                d2.append(t2)
                d2.append(t1)

        else:
            if t1 > t2:
                d1.append(t1)
                d1.append(t2)
            else:
                d2.append(t2)
                d2.append(t1)

        if (tuple(d1), tuple(d2)) in rounds:
            return 1, d1

        rounds.add((tuple(d1), tuple(d2)))

    if d1:
        return 1, d1
    else:
        return 2, d2


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

_, wd = game(d1, d2)

score = 0
for i, card in enumerate(wd):
    score += (len(wd)-i)*card
print(score)