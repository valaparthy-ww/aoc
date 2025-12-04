def read_input():
    with open("input.txt") as f:
        lines = f.readlines()
        for line in lines:
            yield line.strip()


def main():
    _joltage_sum_exactly_twice,_part2 = 0, 0
    for line in read_input():
        _joltage_sum_exactly_twice += get_top_2_digits(line)
    return _joltage_sum_exactly_twice, _part2

def get_top_2_digits(line):
    top_digits = [0, 0]
    top_digit_idx = 0
    for i, c in enumerate(line):
        if int(c) > int(top_digits[0]) and i < len(line)-1:
            top_digits[0] = c
            top_digit_idx = i
        elif i > 0:
            top_digits[1] = max(line[top_digit_idx+1:] or top_digits[1:])
    return int("".join(top_digits))



if __name__ == "__main__":
    res_part1, res_part2 = main()
    print(f"part1: {res_part1}")
    print(f"part2: {res_part2}")
