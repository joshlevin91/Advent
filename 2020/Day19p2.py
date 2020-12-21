import re

def check(rules, key, msg, i=0):

    if rules[key] == ['"a"']:
        i += 1
        if i-1 >= len(msg):
            return False, i, False
        if msg[i-1] == 'a':
            return True, i, True
        else:
            return False, i, True

    if rules[key] == ['"b"']:
        i += 1
        if i-1 >= len(msg):
            return False, i, False
        if msg[i-1] == 'b':
            return True, i, True
        else:
            return False, i, True


    if '|' in rules[key] and len(rules[key]) == 6:
        new_keys = rules[key]
        c2, c4, c5 = False, False, False
        c1, i1, long1 = check(rules, new_keys[0], msg, i)
        if long1:
            c2, i2, long2 = check(rules, new_keys[1], msg, i1)

        c3, i3, long3 = check(rules, new_keys[3], msg, i)
        if long3:
            c4, i4, long4 = check(rules, new_keys[4], msg, i3)
            if long4:
                c5, i5, long5 = check(rules, new_keys[5], msg, i4)
        if c1 and c2:
            return True, i2, True
        if c3 and c4 and c5:
            return True, i5, True
        else:
            return False, i2, False

    elif '|' in rules[key] and len(rules[key]) == 5:
        i2 = i
        c2, c4 = False, False
        new_keys = rules[key]
        c1, i1, long1 = check(rules, new_keys[0], msg, i)
        if long1:
            c2, i2, long2 = check(rules, new_keys[1], msg, i1)
        c3, i3, long3 = check(rules, new_keys[3], msg, i)
        if long3:
            c4, i4, long4 = check(rules, new_keys[4], msg, i1)
        # if key == '42' and c1 and c2:
        #     print(msg[i:i2])
        # if key == '42' and c3 and c4:
        #     print(msg[i:i4])
        return (c1 and c2) or (c3 and c4), i2, True

    elif '|' in rules[key] and len(rules[key]) == 4:
        new_keys = rules[key]
        c3 = False
        c1, i1, long1 = check(rules, new_keys[0], msg, i)
        c2, i2, long2 = check(rules, new_keys[2], msg, i)
        if long2:
            c3, i3 = check(rules, new_keys[3], msg, i2)
        if c1:
            return True, i1, True
        if c2 and c3:
            return True, i3, True
        else:
            return False, i1, False

    elif '|' in rules[key]:
        new_keys = rules[key]
        c1, i1, long1 = check(rules, new_keys[0], msg, i)
        c2, i2, long2 = check(rules, new_keys[2], msg, i)
        return c1 or c2, i2, True

    else:
        res = True
        leng = True
        for rule in rules[key]:
            c, i, l = check(rules, rule, msg, i)
            if not c:
                res = False
            if not l:
                leng = False
        return res, i, leng

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
    res, length, l= check(rules, '0', msg)
    if res and length == len(msg):
        total += 1
print(total)