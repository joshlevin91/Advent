import re

def main():

	passport_fields = {"byr": False, "iyr": False, "eyr": False, "hgt": False, "hcl": False, "ecl": False, "pid": False}
	valid_passports = 0

	with open("Day04.txt", "r") as input_file:
		for line in input_file:
			line = line.strip("\n")

			if not line: 

				# If all fields are present
				if all(field_present == True for field_present in passport_fields.values()):
					valid_passports += 1

				# Reset all fields to not present
				passport_fields = dict.fromkeys(passport_fields, False)

				continue

			for field in passport_fields.keys():

				if field in line:

					pos = line.find(field) + 4
					value = line[pos:].split(' ')[0]

					if field == "byr":
						byr = int(value)
						if byr >= 1920 and byr <= 2002:
							passport_fields[field] = True
							# print(byr)

					elif field == "iyr":
						iyr = int(value)
						if iyr >= 2010 and iyr <= 2020:
							passport_fields[field] = True		
							# print(iyr)

					elif field == "eyr":
						eyr = int(value)
						if eyr >= 2020 and eyr <= 2030:
							passport_fields[field] = True		
							# print(eyr)

					elif field == "hgt":

						if "cm" in value:
							result = re.search('(.*)cm', value)
							num = int(result.group(1))
							if num >= 150 and num <= 193:
								passport_fields[field] = True	
								# print(num)

						elif "in" in value:
							result = re.search('(.*)in', value)
							num = int(result.group(1))
							if num >= 59 and num <= 76:
								passport_fields[field] = True	
								# print(num)

					elif field == "hcl":
						result = re.match("\A#[0-9a-f][0-9a-f][0-9a-f][0-9a-f][0-9a-f][0-9a-f]", value)
						if result is not None:
							passport_fields[field] = True	
							# print(result.group(0))

					elif field == "ecl":
						result = re.match("amb|blu|brn|gry|grn|hzl|oth", value)
						if result is not None:
							passport_fields[field] = True	
							# print(result.group(0))

					elif field == "pid":
						result = re.match("\d{9}", value)
						if result is not None:
							passport_fields[field] = True	
							# print(result.group(0))
					
	print(valid_passports)


main()