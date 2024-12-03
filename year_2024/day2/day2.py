def read_input():
	reports = []
	with open("input.txt") as f:
		lines = f.readlines()
		for line in lines:
			reports.append(list(map(int, line.split(" "))))
	return reports


def get_safe_count(nums):
	prev = nums[0]
	increasing = None
	for num in nums[1:]:
		if increasing is not None and increasing!=(num > prev):
			return 0
		if num > prev and 1 <= num - prev <= 3:
			increasing = True
		elif num < prev and 1 <= prev - num <= 3:
			increasing = False
		else:
			return 0
		prev = num
	return 1


def get_safe_count_loose(nums):
	res = get_safe_count(nums)
	i = 0
	while res == 0 and i < len(nums):
		res = get_safe_count(nums[:i] + nums[i + 1:])
		i += 1
	return res


if __name__ == "__main__":
	reports = read_input()
	safe_count, safe_count_loose = 0, 0
	for report in reports:
		#  part 1
		safe_count += get_safe_count(report)
		# part 2
		safe_count_loose += get_safe_count_loose(report)
	print(safe_count, safe_count_loose)
