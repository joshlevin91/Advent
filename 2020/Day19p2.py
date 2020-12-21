import re

def check(rules, key, msg, i=0):

    if rules[key] == ['"a"']:
        i += 1
        if i-1 < len(msg) and msg[i-1] == 'a':
            return True, i
        else:
            return False, i

    if rules[key] == ['"b"']:
        i += 1
        if i-1 < len(msg) and msg[i-1] == 'b':
            return True, i
        else:
            return False, i

    if '|' in rules[key] and len(rules[key]) == 6:
        new_keys = rules[key]
        c1, i1 = check(rules, new_keys[0], msg, i)
        c2, i2 = check(rules, new_keys[1], msg, i1)
        c3, i3 = check(rules, new_keys[3], msg, i)
        c4, i4 = check(rules, new_keys[4], msg, i3)
        c5, i5 = check(rules, new_keys[5], msg, i4)
        if c1 and c2:
            return True, i2
        if c3 and c4 and c5:
            return True, i5
        else:
            return False, i2

    elif '|' in rules[key] and len(rules[key]) == 5:
        new_keys = rules[key]
        c1, i1 = check(rules, new_keys[0], msg, i)
        c2, i2 = check(rules, new_keys[1], msg, i1)
        c3, i3 = check(rules, new_keys[3], msg, i)
        c4, i4 = check(rules, new_keys[4], msg, i1)
        if key == '42' and c1 and c2:
            print(msg[i:i2])
        if key == '42' and c3 and c4:
            print(msg[i:i4])
        return (c1 and c2) or (c3 and c4), i4

    elif '|' in rules[key] and len(rules[key]) == 4:
        new_keys = rules[key]
        c1, i1 = check(rules, new_keys[0], msg, i)
        c2, i2 = check(rules, new_keys[2], msg, i)
        c3, i3 = check(rules, new_keys[3], msg, i2)
        if c1:
            return True, i1
        if c2 and c3:
            return True, i3
        else:
            return False, i1

    elif '|' in rules[key]:
        new_keys = rules[key]
        c1, i1 = check(rules, new_keys[0], msg, i)
        c2, i2 = check(rules, new_keys[2], msg, i)
        return c1 or c2, i2

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