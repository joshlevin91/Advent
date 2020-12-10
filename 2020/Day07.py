import re
import collections

def contains(bags, outer, inner):
    if bags[outer] == ['no other bags']:
        return False
    elif True in [inner in bag for n, bag in bags[outer]]:
        return True
    else:
        for n, bag in bags[outer]:
            if contains(bags, bag, inner):
                return True
        return False

def count(bags, outer, n):
    total = n
    if bags[outer] != ['no other bags']:
        for nn, bag in bags[outer]:
            total += n*count(bags, bag, nn)
    return total

bags = collections.defaultdict(list)
lines = open('Day07.txt', 'r').readlines()
for line in lines:
    outer = re.search('^(.*?) bags', line).group(1)
    inners = [i[1].split(' ', 1) for i in re.findall('(, |contain )(.*?) (bags|bag)', line)]
    if ['no', 'other'] not in inners:
        for inner in inners:
            n = int(inner[0])
            color = inner[1]
            bags[outer].append((n, color))
    else:
        bags[outer].append('no other bags')

n = 0
for bag in bags.keys():
    if contains(bags, bag, 'shiny gold'):
        n += 1
                                
print(n, count(bags, 'shiny gold', 1) - 1)