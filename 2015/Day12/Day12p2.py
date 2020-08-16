import json

def addSum(obj):
	if isinstance(obj, int):
		return obj

	elif isinstance(obj, dict):
		if "red" in obj.values():
			return 0
		else:
			return sum(addSum(elements) for elements in obj.values())

	elif isinstance(obj, list):
		return sum(addSum(elements) for elements in obj)

	return 0

def main():

	with open("input.txt", "r") as input_file:
		inputs = json.load(input_file)
		print(addSum(inputs))

main()