def parse_to_list(s, i=0):
    result = []
    while i < len(s):
        if s[i] == '(':
            i, r = parse_to_list(s, i+1)
            result.append(r)
        elif s[i] == ')':
            return i+1, result
        else:
            result.append(s[i])
            i += 1
    return i, result

def helper(l):
    if type(l) is not list:
        return l
    for i, item in enumerate(l):
        l[i] = helper(item)
    return parentheses_around_addition(l)

def parentheses_around_addition(l):
    while True:
        try:
            i = l.index('+')
            l = l[:i-1] + [[l[i-1], l[i], parentheses_around_addition(l[i+1])]] + l[i+2:]
        except ValueError:
            break
    return l

def evaluate(eq):
    if len(eq) == 1:
        if type(eq) is str:
            return int(eq)
        else:
            return evaluate(eq[0])
    res = evaluate(eq[0])
    for i, term in enumerate(eq):
        if term == '+':
            res = res + evaluate(eq[i+1])
        elif term == '*':
            res = res * evaluate(eq[i+1])
    return res

with open('Day18.txt') as file:
    lines = [line.replace(' ', '') for line in file.read().splitlines()]

total = 0
for line in lines:
    _, eq = parse_to_list(line)
    eq = helper(eq) #p2
    total += evaluate(eq)
print(total)