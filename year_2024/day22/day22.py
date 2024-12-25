import timeit
from collections import defaultdict


def read_input():
	with open("input.txt") as f:
		return f.readlines()


def do_mix(num, secret_num):
	return num ^ secret_num


def do_prune(num):
	return num % 16777216


def do(num):
	mul = num * 64
	secret_num = do_mix(mul, num)
	secret_num = do_prune(secret_num)
	secret_num = do_mix(secret_num // 32, secret_num)
	secret_num = do_prune(secret_num)
	secret_num = do_mix(secret_num * 2048, secret_num)
	secret_num = do_prune(secret_num)
	return secret_num


def main(secret_num):
	i = 0
	all_seqs = defaultdict(int)
	last_digit = secret_num % 10
	last_4_changes = []
	while i < max_limit:
		secret_num = do(secret_num)
		price_change = (secret_num % 10) - last_digit
		last_4_changes.append(price_change)
		last_4_changes.pop(0) if len(last_4_changes) > 4 else None
		last_digit = secret_num % 10
		if len(last_4_changes) == 4 and tuple(last_4_changes) not in all_seqs:
			all_seqs[tuple(last_4_changes)] = last_digit
		i += 1
	return secret_num, all_seqs


def find_max_val(seqs):
	seq_counter = defaultdict(int)
	for seq in seqs:
		for key, val in seq.items():
			seq_counter[key] += val
	return sorted([(v, k) for k, v in seq_counter.items()], reverse=True)[0]


if __name__ == "__main__":
	start = timeit.default_timer()
	res1, res2 = 0, 0
	max_limit = 2000
	all_sequences = []
	for line in read_input():
		secret_num = int(line.strip("\n"))
		temp = main(secret_num)
		res1 += temp[0]
		all_sequences.append(temp[1])
	res2 = find_max_val(all_sequences)
	print(f"The difference of time is : {timeit.default_timer() - start} seconds", )
	print(res1, res2)
