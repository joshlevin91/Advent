import re

def main():

    valid_passwords_p1 = 0
    valid_passwords_p2 = 0

    with open("Day02.txt", "r") as input_file:

        for line in input_file:

            data = re.split(': |-| ', line.rstrip('\n'))
            n1 = int(data[0])
            n2 = int(data[1])
            letter = data[2]
            password = data[3]

            occurences = password.count(letter)

            if occurences >= n1 and occurences <= n2:
                valid_passwords_p1 += 1

            found = 0
            
            if password[n1-1] == letter:
                found += 1
            if password[n2-1] == letter:
                found += 1

            if found == 1:
                valid_passwords_p2 += 1

    print("Part 1:", valid_passwords_p1)
    print("Part 2:", valid_passwords_p2)

main()