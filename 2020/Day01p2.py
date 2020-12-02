def main():

    sum = 2020

    numbers = []
    with open("Day01.txt", "r") as input_file:
        for line in input_file:
            numbers.append(int(line))

    done = False
    for i in range(len(numbers)):
        for j in range(1, len(numbers)):
            for k in range(2, len(numbers)):
                if numbers[i] + numbers[j] + numbers[k] == sum:
                    print(numbers[i] * numbers[j] * numbers[k])
                    done = True
                    break
            if done:
                break
        if done:
            break

main()