import timeit
from collections import defaultdict


class Rule:
	def __init__(self, key, op1, op, op2):
		self.key = key
		self.op1 = op1
		self.op = op
		self.op2 = op2
	
	def process(self):
		if self.op=="AND":
			res = init_values[self.op1] & init_values[self.op2]
		elif self.op=="OR":
			res = init_values[self.op1] | init_values[self.op2]
		elif self.op=="XOR":
			res = init_values[self.op1] ^ init_values[self.op2]
		else:
			raise BaseException(f"Unknown operation {self.op}!!")
		update_init_values(self.key, res)


def read_input():
	rules = defaultdict(Rule)
	init_values = defaultdict(int)
	with open("input.txt") as f:
		for line in f.readlines():
			line = line.rstrip("\n")
			if ":" in line:
				temp = line.split(":")
				init_values[temp[0].strip(" ")] = int(temp[1].strip(" "))
			elif "->" in line:
				temp = line.split("->")
				rules[temp[1].strip(" ")] = Rule(temp[1].strip(" "), *temp[0].split(" ")[:3])
	return rules, init_values


def has_init_value(op):
	return init_values.get(op, None)


def update_init_values(key, val):
	init_values[key] = val


def get_values_start_with_z():
	temp = sorted([(k, v) for k, v in init_values.items() if k.startswith("z")], reverse=True)
	res = ""
	for k, v in temp:
		res += str(v)
	return int(str.format(res, "b"), 2)


def process_rule(rule):
	if rule.key in init_values:
		return 0
	elif has_init_value(rule.op1) is not None and has_init_value(rule.op2) is not None:
		return rule.process()
	elif has_init_value(rule.op2) is None:
		process_rule(rules[rule.op2])
		return process_rule(rule)
	elif has_init_value(rule.op1) is None:
		process_rule(rules[rule.op1])
		return process_rule(rule)


if __name__ == "__main__":
	start = timeit.default_timer()
	rules, init_values = read_input()
	res1, res2 = 0, 0
	for key, rule in rules.items():
		process_rule(rule)
	res1 = get_values_start_with_z()
	print(f"The difference of time is : {timeit.default_timer() - start} seconds", )
	print(res1, res2)
