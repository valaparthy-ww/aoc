import re


def read_input():
	with open("input.txt") as f:
		return f.readlines()


def find_horizontally(line, search_term="XMAS"):
	return len(re.findall(search_term, line))


def find_backwards(line):
	return find_horizontally(line, search_term[::-1])


def find_vertical(line):
	"""after transposing columns to rows"""
	return find_horizontally(line,) + find_backwards(line, )


def find_diagonals(matrix):
	"""
	assuming this will be a square matrix
	for each iteration, we need to traverse top->bottom, left->right, 4 directions
	
	"""
	diagonals_count = 0
	i, j = 0, 0
	while i < len(matrix):
		j = 0
		while j < len(matrix[i]):
			# top->bottom, left->right, example: ((0,0),(1,1),(2,2),(3,3))
			try:
				tblt = matrix[i][j] + matrix[i + 1][j + 1] + matrix[i + 2][j + 2] + matrix[i + 3][j + 3]
				if tblt == search_term:
					diagonals_count += 1
					# print((i, j), (i + 1, j + 1), (i + 2, j + 2), (i + 3, j + 3))
			except IndexError as ex:
				pass
			# bottom->top, left->right, example: ((3,0),(2,1),(1,2),(0,3))
			try:
				btlr = matrix[i + 3][j] + matrix[i + 2][j + 1] + matrix[i + 1][j + 2] + matrix[i][j + 3]
				if btlr == search_term:
					diagonals_count += 1
					# print((i+3, j), (i + 2, j + 1), (i + 1, j + 2), (i, j + 3))
			except IndexError as ex:
				pass
			# top->bottom, right->left, example: ((0,3),(1,2),(2,1),(3,0))
			try:
				tbrl = matrix[i][j + 3] + matrix[i + 1][j + 2] + matrix[i + 2][j + 1] + matrix[i + 3][j]
				if tbrl == search_term:
					diagonals_count += 1
					# print((i, j+3), (i + 1, j + 2), (i + 2, j + 1), (i+3, j))
			except IndexError as ex:
				pass
			# bottom->top, right->left, example: ((3,3),(2,2),(1,1),(0,0))
			try:
				btrl = matrix[i + 3][j + 3] + matrix[i + 2][j + 2] + matrix[i + 1][j + 1] + matrix[i][j]
				if btrl == search_term:
					diagonals_count += 1
					# print((i+3, j + 3), (i + 2, j + 2), (i + 1, j + 1), (i, j))
			except IndexError as ex:
				pass
			j += 1
		i += 1
	return diagonals_count


def find_one_nearest_neighbor(matrix):
	"""
	
	for part 2, central element is "A", we inspect the first nearest neighbors around it and see if they're either MAS or SAM
	note that we only need to look either top-bottom or bottom-top
	example:
	
	M . S
	. A .
	M . S
	
	top to bottom: left diagonal is MAS, right diagonal is SAM, when this is found, increment counter
	"""
	diagonals_count = 0
	i, j = 0, 0
	while i < len(matrix):
		j = 0
		while j < len(matrix[i]):
			if matrix[i][j] == "A":
				try:
					if matrix[i-1][j-1]+matrix[i][j]+matrix[i+1][j+1] in ("MAS", "SAM") and matrix[i-1][j+1]+matrix[i][j]+matrix[i+1][j-1] in ("MAS", "SAM"):
						diagonals_count += 1
				except IndexError as ex:
					pass
			j += 1
		i += 1
	return diagonals_count
	
	
if __name__ == "__main__":
	lines = read_input()
	search_term = "XMAS"
	res_part1 = 0
	for idx, line in enumerate(lines):
		#  part 1
		res_part1 += find_horizontally(line) + find_backwards(line) + find_vertical("".join(list(zip(*lines))[idx]))
	lines_array = [list(line.rstrip("\n")) for line in lines]
	res_part1 += find_diagonals(lines_array)
	# part 2
	res_part2 = find_one_nearest_neighbor(lines_array)
	print(res_part1, res_part2)
