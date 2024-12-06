from collections import defaultdict
def read_input():
	rules = defaultdict(list)
	updates = []
	with open("input.txt") as f:
		for line in f.readlines():
			pipe_split = line.split("|")
			comma_split = line.split(",")
			if len(pipe_split) > 1:
				rules[int(pipe_split[0])].append(int(pipe_split[1]))
			elif len(comma_split) > 1:
				updates.append(list(map(int, comma_split)))
	return rules, updates


def is_valid_order(update):
	"""check if the line is ordered"""
	for idx, num in enumerate(update[:-1]):
		for jdx, _ in enumerate(update, idx+1):
			try:
				if not (update[idx] in rules and update[jdx] in rules[num]):
					return False
			except IndexError as ex:
				pass
	return True


def fix_ordering(update):
	"""recursive brute force approach to re-order one at a time by swapping"""
	fixed_order = update.copy()
	for idx, num in enumerate(update[:-1]):
		for jdx, _ in enumerate(update, idx+1):
			try:
				if not (update[idx] in rules and update[jdx] in rules[num]):
					temp = fixed_order[jdx]
					fixed_order[jdx] = fixed_order[idx]
					fixed_order[idx] = temp
			except IndexError as ex:
				pass
	while not is_valid_order(fixed_order):
		return fix_ordering(fixed_order)
	return fixed_order


if __name__ == "__main__":
	rules, updates = read_input()
	res_part1, res_part2 = 0, 0
	for update in updates:
		if is_valid_order(update):
			res_part1 += update[len(update)//2]
		else:
			fixed_order = fix_ordering(update)
			res_part2 += fixed_order[len(fixed_order)//2]
	print(res_part1, res_part2)
	
