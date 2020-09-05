import itertools, copy, numpy

def split(nums, n, inner = False):

    for i in range(1, len(nums)):

        firsts = itertools.combinations(nums,i)
        small_firsts = []
        remainings = []

        for first in firsts:

            remaining = copy.copy(nums)      
            for weight in first:
                remaining.remove(weight)

            if sum(remaining) == (n-1)*sum(first):
                small_firsts.append(first)
                remainings.append(remaining)
                if inner:
                    break

        if small_firsts:

            if n == 2:
                return True

            elif split(remainings[0], n-1, True):
                return small_firsts

    return None

def main():

    nums = []
    with open("input.txt", "r") as input_file:
        for line in input_file:
            nums.append(int(line.rstrip('\n')))

    packages = split(nums, 4)

    ideal_qe = None
    for package in packages:
        result = numpy.prod(package)
        if ideal_qe == None or result < ideal_qe:
            ideal_qe = result

    print(ideal_qe)
    
main()