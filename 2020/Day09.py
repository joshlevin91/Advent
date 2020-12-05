def sum_exists(nums, target):
	unique_nums = set()
	for n in nums:
		if (target - n) in unique_nums:
			return True
		else:
			unique_nums.add(n)
	return False

text = open("Day09.txt", 'r').read().split('\n')
nums = [int(i) for i in text]

n = 25
prev_nums = [nums[i] for i in range(n)]
while n < len(nums):
	invalid_num = nums[n]
	if not sum_exists(prev_nums, invalid_num):
		break
	prev_nums.pop(0)
	prev_nums.append(invalid_num)
	n += 1

end = 0
contiguous = [nums[end]]
while sum(contiguous) != invalid_num:
	end += 1
	contiguous.append(nums[end])
	while sum(contiguous) > invalid_num:
		contiguous.pop(0)

print(min(contiguous) + max(contiguous))