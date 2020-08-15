import re

# Increment password
def increment(password):
	for i in reversed(range(len(password))):
		next_char = chr(ord(password[i])+1)
		if next_char == '{':
			password[i] = 'a'
		else:
			password[i] = next_char
			break
	return password

# Return True if password includes one increasing straight of at least three letters
def increasing_straight(password):
	straight_length = 1
	for i in range(len(password)):
		password[i] = ord(password[i])
		if i >= 1 and password[i] == password[i-1] + 1:
			straight_length += 1
			if straight_length == 3:
				return True
		else:
			straight_length = 1
	return False

# Return True if password does not contain any of: i, o, or l
def no_bad_letters(password):
	if 'i' in password or 'o' in password or 'l' in password:
		return False
	else:
		return True

# Return True if password contains at least two different non-overlapping pairs of letters
def pairs(password):
	password = "".join(password)
	matches = re.findall("(.)\\1", password)
	if len(matches) >= 2:
		return True
	else:
		return False

# Find next password
def main():
	password = list("hxbxwxba")

	i = 0
	while True:
		password = increment(password)
		if increasing_straight(password[:]) and no_bad_letters(password) and pairs(password):
			i += 1
			if i == 2:
				break

	print("".join(password))

main()