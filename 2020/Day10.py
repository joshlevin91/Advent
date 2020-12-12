solved = {}

def paths(n):
    if n in solved:
        return solved[n]
    if n == 0:
        return 1
    res = 0
    for i in range(1,4):
        if n-i >= 0 and adapters[n] - adapters[n-i] <= 3:
            res += paths(n-i)
        else:
            break
    solved[n] = res
    return res

lines = open('Day10.txt', 'r').readlines()
adapters = [int(line) for line in lines]
adapters.append(0)
adapters.sort()
adapters.append(adapters[-1]+3)

n_one, n_three = 0, 0
jolts = 0
for adapter in adapters:
    if adapter - jolts == 1:
        n_one += 1
    elif adapter - jolts == 3:
        n_three += 1
    jolts = adapter

print(n_one*n_three)
print(paths(len(adapters)-1))