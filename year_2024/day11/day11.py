import timeit


def read_input():
	with open("input.txt") as f:
		return f.readline()


def replace_zero(num):
	return 1 if num == 0 else None


def mul_by_2024(num):
	return num * 2024


def split_even_num(num):
	num_string = str(num)
	if len(num_string) % 2==0:
		return [int(num_string[: len(num_string) // 2]), int(num_string[len(num_string) // 2:])]

def apply_rules(num):
	return replace_zero(num) or split_even_num(num) or mul_by_2024(num)


def main(line, max_blinks):
	blink = 0
	cache = {}
	while blink < max_blinks:
		temp_line = []
		for i, num in enumerate(line):
			if num not in cache:
				res = apply_rules(num)
				cache[num] = res
			else:
				res = cache[num]
			if isinstance(res, int):
				temp_line.append(res)
			else:
				temp_line.extend(res)

		blink += 1
		line = temp_line.copy()
	return line
	

if __name__=="__main__":
	start = timeit.default_timer()
	line = list(map(int, read_input().split(" ")))
	res_part1 = main(line, 25)

	print(f"The difference of time is : {timeit.default_timer() - start} seconds", )
	print(len(res_part1))
