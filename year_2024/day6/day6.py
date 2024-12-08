import time


def read_input():
	matrix = []
	blocker_indices = []
	position = {"^": None, "<": None, ">": None, "v": None}
	with open("input.txt") as f:
		for i, line in enumerate(f.readlines()):
			temp = []
			for j, c in enumerate(line.rstrip()):
				temp.append(c)
				if c in position:
					position[c] = (i, j)
				elif c == "#":
					blocker_indices.append((i, j))
			matrix.append(temp)
	curr_pos = {key: pos for key, pos in position.items() if pos}
	return matrix, curr_pos, blocker_indices
	

def is_end_of_grid(curr_pos):
	row_idx, col_idx = curr_pos
	if row_idx <= 0 or row_idx >= len(matrix)-1 or col_idx <= 0 or col_idx >= len(matrix)-1:
		return True
	return False


def update_row_matrix_up(start_row_idx, end_row_idx, col_idx):
	counter = 0
	while start_row_idx > end_row_idx:
		if matrix[start_row_idx][col_idx]:
			matrix[start_row_idx][col_idx] = False
			counter += 1
		start_row_idx -= 1
	return counter


def update_row_matrix_down(start_row_idx, end_row_idx, col_idx):
	counter = 0
	while start_row_idx < end_row_idx:
		if matrix[start_row_idx][col_idx]:
			matrix[start_row_idx][col_idx] = False
			counter += 1
		start_row_idx += 1
	return counter


def update_col_matrix_right(start_col_idx, end_col_idx, row_idx):
	counter = 0
	while start_col_idx < end_col_idx:
		if matrix[row_idx][start_col_idx]:
			matrix[row_idx][start_col_idx] = False
			counter += 1
		start_col_idx += 1
	return counter


def update_col_matrix_left(start_col_idx, end_col_idx, row_idx):
	counter = 0
	while start_col_idx > end_col_idx:
		if matrix[row_idx][start_col_idx]:
			matrix[row_idx][start_col_idx] = False
			counter += 1
		start_col_idx -= 1
	return counter


def move_up(curr_pos):
	row_idx, col_idx = curr_pos
	start_idx, end_idx = row_idx, max([x[0] for x in blocker_indices if x[1] == col_idx and x[0] < row_idx] or [0])
	return update_row_matrix_up(start_idx, end_idx, col_idx), ">", (end_idx+1, col_idx)


def move_down(curr_pos):
	row_idx, col_idx = curr_pos
	start_idx, end_idx = row_idx, min([x[0] for x in blocker_indices if x[1] == col_idx and x[0] > row_idx] or [len(matrix)])
	return update_row_matrix_down(start_idx, end_idx, col_idx), "<", (end_idx-1, col_idx)


def move_left(curr_pos):
	row_idx, col_idx = curr_pos
	start_idx, end_idx = col_idx, max([x[1] for x in blocker_indices if x[0] == row_idx and x[1] < col_idx] or [0])
	return update_col_matrix_left(start_idx, end_idx, row_idx), "^", (row_idx, end_idx+1)


def move_right(curr_pos):
	row_idx, col_idx = curr_pos
	start_idx, end_idx = col_idx, min([x[1] for x in blocker_indices if x[0] == row_idx and x[1] > col_idx] or [len(matrix)])
	return update_col_matrix_right(start_idx, end_idx, row_idx), "v", (row_idx, end_idx-1)


if __name__ == "__main__":
	matrix, init_pos, blocker_indices = read_input()
	pos_to_fn_map = {"^": move_up, "<": move_left, ">": move_right, "v": move_down}
	res_part1, res_part2 = 0, 0
	curr_pos = list(init_pos.values())[0]
	direction = list(init_pos.keys())[0]
	while not is_end_of_grid(curr_pos):
		res, direction, curr_pos = pos_to_fn_map[direction](curr_pos)
		res_part1 += res
	print(res_part1, res_part2, )
	
	
	
	
	

