def read_input():
    with open("input.txt", 'r') as file:
        lines = file.readlines()
        operations = [x for x in lines[-1].split(" ") if x]
        values_with_position = []
        for line in lines[:-1]:
            values_with_position.append(line.strip().split(" "))
        return values_with_position, operations

def remove_spaces_convert_numeric(values):
    return [int(x) for x in values if x]

def transpose_values(values):
    """transpose matrix excluding blank values"""
    return [value  for value in zip(*values) if any(value)]


def apply_operation(values, operation):
    import math
    return sum(values) if operation == "+" else math.prod(values)


def main():
    total_value = 0
    values, operations = read_input()
    transposed_values = transpose_values(values)
    for idx, op in enumerate(operations):
        transposed_value = remove_spaces_convert_numeric(transposed_values[idx])
        total_value += apply_operation(transposed_value, op)

    return total_value, 0



if __name__ == "__main__":
    res_part1, res_part2 = main()
    print(f"part1: {res_part1}")
    print(f"part2: {res_part2}")
