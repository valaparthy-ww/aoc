import timeit


def read_input():
	with open("input.txt") as f:
		return f.readlines()


def move_block(line):
	reverse_idx = len(line) - 1
	for idx, c in enumerate(line):
		if c != ".":
			dot_idx = line.index(".")
			if len(set(line[dot_idx:]))==1:
				return line
			while line[reverse_idx] == ".":
				reverse_idx -= 1
			# swap
			temp = line[reverse_idx]
			line[dot_idx] = temp
			line[reverse_idx] = "."
	return line


def get_checksum(line):
	res = 0
	for idx, c in enumerate(line):
		if c==".":
			return res
		res += idx * int(c)
	return res


def generate_file_map(line):
	res = []
	idx = 0
	block_idx = 0
	while idx < len(line):
		free_space = ""
		try:
			block = [str(idx)] * int(line[block_idx])
			free_space = int(line[block_idx + 1]) * ["."]
		except IndexError as ex:
			break
		res.extend(block)
		res.extend(free_space)
		block_idx += 2
		idx += 1
	res.extend(block)
	res.extend(free_space)
	return res

def main(line):
	file_map = generate_file_map(line)
	moved_block = move_block(file_map)
	assert len(file_map)==len(moved_block)
	res = get_checksum(moved_block)
	return res

if __name__=="__main__":
	start = timeit.default_timer()
	lines = read_input()
	res_part1 = 0
	for line in lines:
		res_part1 += main(line)
		
	print(f"The difference of time is : {timeit.default_timer() - start} seconds", )
	print(res_part1)
