import re

def check_side(rules, msg, i, keys):
    res = True
    too_deep = False
    for rule in keys:
        c, i, l = check(rules, rule, msg, i)
        if not l:
            side = [False, i, False]
            too_deep = True
            break
        if not c:
            res = False
    if not too_deep:
        side = [res, i, l]    
    return side

def check(rules, key, msg, i=0):

    if rules[key] == ['"a"']:
        if i >= len(msg):
            return False, i+1, False
        if msg[i] == 'a':
            return True, i+1, True
        else:
            return False, i+1, True

    if rules[key] == ['"b"']:
        if i >= len(msg):
            return False, i+1, False
        if msg[i] == 'b':
            return True, i+1, True
        else:
            return False, i+1, True

    if '|' in rules[key]:
        left_keys = [k for idx, k in enumerate(rules[key]) if idx < rules[key].index('|')]
        left = check_side(rules, msg, i, left_keys)

        right_keys = [k for idx, k in enumerate(rules[key]) if idx > rules[key].index('|')]
        right = check_side(rules, msg, i, right_keys)

        if left[0]:
            return left
        if right[0]:
            return right
        if left[2]:
            return left
        if right[2]:
            return right
        return False, i, False

    else:
        res = True
        for rule in rules[key]:
            c, i, l = check(rules, rule, msg, i)
            if not l:
                return False, i, False
            if not c:
                res = False
        return res, i, l

with open('Day19p2.txt') as file:
    lines = [line.strip() for line in file if line.strip()]

reached_messages = False
rules = {}
messages = []
for line in lines:
    if not reached_messages and re.match('^(a|b)', line):
        reached_messages = True
    if not reached_messages:
        key = re.search('(.*?):', line).group(1)
        value = re.search(': (.*)', line).group(1).split(' ')
        rules[key] = value
    else:
        messages.append(line)

total = 0
for msg in messages:
    res, length, _ = check(rules, '0', msg)
    if res and length == len(msg):
        total += 1
print(total)