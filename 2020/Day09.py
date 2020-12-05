def sum_exists(nums, target):
	unique_nums = set()
	for n in nums:
		if (target - n) in unique_nums:
			return True
		else:
			unique_nums.add(n)
	return False

lines = [int(i) for i in open("Day09.txt", 'r').read().split('\n')]

n = 25
prev_nums = [lines[i] for i in range(n)]
while n < len(lines):
	invalid_num = lines[n]
	if not sum_exists(prev_nums, invalid_num):
		break
	prev_nums.pop(0)
	prev_nums.append(invalid_num)
	n += 1

end = 0
nums = [lines[end]]
while sum(nums) != invalid_num:
	end += 1
	nums.append(lines[end])
	while sum(nums) > invalid_num:
		nums.pop(0)

print(min(nums) + max(nums))