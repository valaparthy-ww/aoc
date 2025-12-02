
CURRENT_POSITION = 50

def read_input():
	with open("input.txt") as f:
		lines = f.readlines()
		for line in lines:
			yield line.strip()[0], int(line.strip()[1:])

def main():
	global CURRENT_POSITION
	_zero_last_position_count = 0
	_zero_crossover_count = 0
	for direction, distance in read_input():
		CURRENT_POSITION, temp = (find_distance(CURRENT_POSITION, direction, distance),
								  zero_crossover_count(CURRENT_POSITION, direction, distance))
		_zero_crossover_count += temp
		if CURRENT_POSITION == 0:
			_zero_last_position_count += 1
	return _zero_last_position_count, _zero_last_position_count+_zero_crossover_count

def get_zero_count(low, high):
	"""count number of zeros crossed in range"""
	cnt = 0
	for i in range(low, high):
		if i % 100 == 0:
			cnt += 1
	return cnt

def zero_crossover_count(current, direction, distance):
	"""count number of zeros crossed between previous and current position"""
	if distance > 0:
		if direction == "R":
			return get_zero_count(current+1, current + distance)
		elif direction == "L":
			return get_zero_count(current - distance+1 , current)
		raise ValueError(f"Invalid direction: {direction}!!")
	raise ValueError(f"Invalid distance: {distance}!!")

def find_distance(current, direction, distance):
	"""find new position after moving distance in given direction"""
	if distance > 0:
		if direction == "R":
			return (current + distance) % 100
		elif direction == "L":
			return (current - distance) % 100
		raise ValueError(f"Invalid direction: {direction}!!")
	raise ValueError(f"Invalid distance: {distance}!!")

if __name__ == "__main__":
	res_part1, res_part2 = main()
	print(f"part1: {res_part1}")
	print(f"part2: {res_part2}")
