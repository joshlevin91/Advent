def main():

    sum = 2020

    numbers = []
    with open("Day01.txt", "r") as input_file:
        for line in input_file:
            numbers.append(int(line))

    numset = set()
    for number in numbers:
        if (sum - number) in numset:
            print(number * (sum - number))
            break
        else:
            numset.add(number)

main()