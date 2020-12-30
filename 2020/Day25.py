ck = 10604480
dk = 4126658
sn = 7

v = 1
n = 1
while True:
    v *= sn
    v = v % 20201227
    if v == ck:
        cl = n
    if v == dk:
        dl = n
        break
    n += 1

sn = ck
v = 1
n = 1
while n <= dl:
    v *= sn
    v = v % 20201227
    n += 1

print(v)