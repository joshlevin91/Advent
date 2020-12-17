numbers = {}
snumbers = [5,2,8,16,18,0,1]
stop = 30000000

k = 1
mn = 0
while k <= stop:
    n = mn
    if k <= len(snumbers):
        mn = snumbers[k-1]
    elif n in numbers:
        mn = k - numbers[n]
    else:
        mn = 0
    numbers[n] = k
    k += 1
print(mn)