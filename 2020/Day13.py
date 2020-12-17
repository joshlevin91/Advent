def findNum(n, div):  
    rem = (n + div) % div;  
    if (rem == 0):  
        return n 
    else: 
        return (n + div - rem)  

with open('Day13.txt') as file:
    lines = file.read().splitlines() 

t = int(lines[0])
busses = {idx: [int(ID), int(ID)] for idx, ID in enumerate(lines[1].split(',')) if ID != 'x'}

#p1
n = 1
while True:
    feasible = [n*ID for idx, [ID, m] in busses.items() if n*ID >= t]
    if feasible:
        earliest = min(feasible)
        print(earliest//n*(earliest - t))
        break
    n += 1

#p2
n = 1
b = 1
max_k = 0
while True:
    k = 0
    for idx, [ID, m] in busses.items():
        if idx == 0:
            busses[idx][1] = n*ID
        else:
            busses[idx][1] = findNum(prev_m, ID)
            if busses[idx][1] - prev_m != idx - prev_idx:
                break
            else:
                k += 1
                if k > max_k:
                    b *= busses[idx][0]
                    max_k = k
        prev_m = busses[idx][1]
        prev_idx = idx

    if k == len(busses)-1:
        print(busses[0][1])
        break

    n += b