import re

def check(rules, key, msg, i=0):

    if rules[key] == ['"a"']:
        i += 1
        if msg[i-1] == 'a':
            return True, i
        else:
            return False, i

    if rules[key] == ['"b"']:
        i += 1
        if msg[i-1] == 'b':
            return True, i
        else:
            return False, i

    if '|' in rules[key]:
        left_keys = [k for idx, k in enumerate(rules[key]) if idx < rules[key].index('|')]
        right_keys = [k for idx, k in enumerate(rules[key]) if idx > rules[key].index('|')]

        res = True
        ix = i
        for rule in left_keys:
            cx, ix = check(rules, rule, msg, ix)
            if not cx:
                res = False
        left = [res, ix]

        res = True
        ix = i
        for rule in right_keys:
            cx, ix = check(rules, rule, msg, ix)
            if not cx:
                res = False
        right = [res, ix]

        return left[0] or right[0], ix

    else:
        res = True
        for rule in rules[key]:
            c, i = check(rules, rule, msg, i)
            if not c:
                res = False
        return res, i

with open('Day19.txt') as file:
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
    res, length = check(rules, '0', msg)
    if res and length == len(msg):
        total += 1
print(total)