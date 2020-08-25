import math

from functools import reduce

def factors(n):    
    return set(reduce(list.__add__, 
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

def binary_search(lower, upper, goal):
    while lower <= upper:
        mid = (lower + upper) // 2
        guess = robins_inequality(mid)
        if guess < goal:
            lower = mid + 1
        elif guess > goal:
            upper = mid - 1
        else:
            return mid
    return upper

def robins_inequality(n):
    return 1.781072418*n*math.log(math.log(n))

def main():

    goal = 34000000
    m = 11
    
    r_goal = goal // m
    n = binary_search(5040, r_goal, r_goal)

    i = 1
    while True:
        #f = factors(i) # part one
        f = [item for item in factors(i) if item*50 >= i] # part two
        if sum(f)*m >= goal:
            break
        i += 1

    print(i)

main()