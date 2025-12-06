def read_input():
    fresh_range = []
    available_values = []
    with open("input.txt", 'r') as file:
        for line in file:
            if len(line.split("-")) == 2:
                low, high = int(line.split('-')[0]), int(line.split('-')[1].strip())
                fresh_range.append((low, high))
            elif line.strip().isdecimal():
                available_values.append(int(line.strip()))
            else:
                continue
    return fresh_range, available_values

def merge_overlap_ranges(ranges):
    """merge ranges that overlap"""
    latest = sorted(ranges,key=lambda x:x[0])[0]
    temp = [latest]
    for start, end in sorted(ranges,key=lambda x:x[0]):
        if min(latest) <= start <= max(latest) or min(latest) <= end <= max(latest):
            latest = (min(min(latest), start), max(max(latest), end))
            temp.pop()
            temp.append(latest)
        else:
            latest = (start, end)
            temp.append(latest)
    return temp


def main():
    _available_fresh_ingredient_count, _fresh_ingredient_count = 0, 0
    fresh_range, available_values = read_input()
    merged_fresh_range = merge_overlap_ranges(fresh_range)
    _fresh_ingredient_count += sum([high - low + 1 for low, high in merged_fresh_range])
    for value in available_values:
        _available_fresh_ingredient_count += check_value_is_fresh(merged_fresh_range, (value, value))
    return _available_fresh_ingredient_count, _fresh_ingredient_count


def check_value_is_fresh(merged_fresh_range, available_range):
    """Check if available value overlaps with existing merged range"""
    merged_range = merged_fresh_range+[available_range]
    return len(merge_overlap_ranges(merged_range)) == len(merged_fresh_range)


if __name__ == "__main__":
    res_part1, res_part2 = main()
    print(f"part1: {res_part1}")
    print(f"part2: {res_part2}")
