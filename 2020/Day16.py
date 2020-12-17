import re

# Parse input
with open('Day16.txt') as file:
    lines = [line.strip() for line in file if line.strip()]

yours, nearby = False, False
nearby_tickets = []
ranges = []
for line in lines:
    if not yours and re.match('^your ticket:', line):
        yours = True
        continue
    elif not nearby and re.match('^nearby tickets:', line):
        nearby = True
        continue

    if nearby:
        nearby_tickets.append([int(n) for n in line.split(',')])
    elif yours:
        your_ticket = [int(n) for n in line.split(',')]
    else:
        l1 = int(re.search(': (\d*?)-', line).group(1))
        u1 = int(re.search('-(\d*?) or', line).group(1))
        l2 = int(re.search('or (\d*?)-', line).group(1))
        u2 = int(re.search('-(\d*?)$', line).group(1))
        ranges.append([l1, u1, l2, u2])

# Compute error rate and discard invalid tickets
error = 0
valid_tickets = [your_ticket]
for ticket in nearby_tickets:
    valid_ticket = True
    for n in ticket:
        valid_num = False
        for r in ranges:
            if r[0] <= n <= r[1] or r[2] <= n <= r[3]:
                valid_num = True
                continue
        if not valid_num:
            error += n
            valid_ticket = False
    if valid_ticket:
        valid_tickets.append(ticket)
print(error)

# Create dictionary where key -> field number, and value -> ticket positions that can't be associated with it
bad = {}
for ticket in valid_tickets:
    for it, n in enumerate(ticket):
        for ir, r in enumerate(ranges):
            if not (r[0] <= n <= r[1] or r[2] <= n <= r[3]):
                if ir not in bad:
                    bad[ir] = [it]
                elif it not in bad[ir]:
                    bad[ir].append(it)

# Create list of sublists where first element of sublist is range number and rest are ticket positions that 
# can be associated with it
good = []
for key in bad:
    l = [key] + [i for i in range(len(your_ticket)) if i not in bad[key]]
    good.append(l)
good.sort(key = len)

# Create association between range number and ticket position by process of elimination
used = set()
associations = {}
for g in good:
    sub = [i for i in g[1:] if i not in used]
    if len(sub) == 1:
        used.add(sub[0])
    associations[g[0]] = sub[0]

# Compute result
res = 1
for i in range(6):
    res *= your_ticket[associations[i]]
print(res)