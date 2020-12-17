import re
from itertools import combinations

def applyMaskVal(bval, mask):
    for i in range(len(mask)):
        op = mask[i]
        if op == '1':
            bval = bval[:i] + '1' + bval[i + 1:]
        elif op == '0':
            bval = bval[:i] + '0' + bval[i + 1:]
    return bval

def applyMaskMem(bmem, mask):
    floats = []
    for i in range(len(mask)):
        op = mask[i]
        if op == '1':
            bmem = bmem[:i] + '1' + bmem[i + 1:]
        elif op == 'X':
            bmem = bmem[:i] + '0' + bmem[i + 1:]
            floats.append(i)

    mems = [int(bmem, 2)]
    for k in range(1, len(floats)+1):
        for c in combinations(floats, k):
            temp = bmem[:]
            for i in c:
                temp = temp[:i] + '1' + temp[i + 1:]
            mems.append(int(temp, 2))

    return mems

with open('Day14.txt') as file:
    lines = file.read().splitlines()

#p1
vals = {}
for line in lines:
    if re.match('^mask', line):
        mask = re.search('= (.*)', line).group(1)
    else:
        mem = int(re.search('mem\[(.*?)\]', line).group(1))
        val = int(re.search('= (.*)', line).group(1))
        bval = applyMaskVal('{0:036b}'.format(val), mask)
        mval = int(bval, 2)
        vals[mem] = mval

print(sum(vals.values()))

#p2
vals = {}
for line in lines:
    if re.match('^mask', line):
        mask = re.search('= (.*)', line).group(1)
    else:
        mem = int(re.search('mem\[(.*?)\]', line).group(1))
        val = int(re.search('= (.*)', line).group(1))
        mems = applyMaskMem('{0:036b}'.format(mem), mask)
        for m in mems:
            vals[m] = val

print(sum(vals.values()))