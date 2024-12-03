def read_input():
	left_list = []
	right_list = []
	left_dict = {}
	right_dict = {}
	with open("input.txt") as f:
		lines = f.readlines()
		for line in lines:
			left, right = map(int, line.split("   "))
			left_list.append(left)
			right_list.append(right)
			left_dict[left] = left_dict.get(left, 0) + 1
			right_dict[right] = right_dict.get(right, 0) + 1
	return left_list, right_list, left_dict, right_dict


def find_distance(left_list, right_list):
	left_lst = sorted(left_list)
	right_lst = sorted(right_list)
	diff = 0
	for i in range(0, len(left_lst)):
		diff += abs(int(left_lst[i]) - int(right_lst[i]))
	return diff


def find_similarity(left_dict, right_dict):
	diff = 0
	for k in left_dict.keys():
		diff += k * right_dict.get(k, 0)
	return diff


if __name__ == "__main__":
	left_list, right_list, left_dict, right_dict = read_input()
	# part 1
	print(find_distance(left_list, right_list))
	# part 2
	print(find_similarity(left_dict, right_dict))
