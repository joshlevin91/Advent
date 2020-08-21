import hashlib

def main():
	with open('input.txt', 'r') as file:

		secret_key = file.read()
		num = 1

		while True:

			key_to_try = secret_key + str(num)
			hash = hashlib.md5(key_to_try.encode()).hexdigest()
			if hash[0:6] == '000000':
				break

			num += 1

	print(num)

main()