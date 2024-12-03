import re


def read_input():
	with open("input.txt") as f:
		return f.read()


def regex_find_matches(text, pattern):
	matching = re.finditer(pattern, text)
	return matching


def mul(match):
	temp = match.replace("mul(", "").replace(")", "").split(",")
	return int(temp[0]) * int(temp[1])


def is_enable(match):
	nearest_do = max([x for x in doindices if x <= match.start()] + [0])
	nearest_dont = max([x for x in donot_indices if x <= match.start()] + [-1])
	if nearest_do > nearest_dont:
		return True
	return False


if __name__ == "__main__":
	text = read_input()
	matches = regex_find_matches(text, "mul\([0-9]+,[0-9]+\)")
	donot_indices, doindices = [], []
	for i in regex_find_matches(text, "don't\(\)"):
		donot_indices.append(i.end())
	for i in regex_find_matches(text, "do\(\)"):
		doindices.append(i.end())
	res_part1 = 0
	res_part2 = 0
	for match in matches:
		res_part1 += mul(text[match.start(): match.end()])
		if is_enable(match):
			res_part2 += mul(text[match.start(): match.end()])
	print(res_part1, res_part2,)
