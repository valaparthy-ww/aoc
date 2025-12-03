def read_input():
    with open("input.txt") as f:
        data = f.read()
        for id_range in data.split(","):
            yield id_range.strip().split("-")


def main():
    _invalid_id_count_exact,_invalid_id_count_atleast = 0, 0
    for low, high in read_input():
        _invalid_id_count_exact += get_substring_repeated_n_times(int(low), int(high)+1, repetition_count=2)
        _invalid_id_count_atleast += get_substring_repeated_n_times(int(low), int(high) + 1,)
    return _invalid_id_count_exact, _invalid_id_count_atleast



def get_substring_repeated_n_times(low, high, repetition_count=None):
    """sum of numbers in the range that are made of a substring repeated"""
    res = 0
    for i in range(low, high):
        string_i = str(i)
        for n in range(1, (len(string_i)//2)+1):
            repetitions = repetition_count or len(string_i)//n
            if string_i == string_i[0:n] * repetitions:
                res += i
                break
    return res


if __name__ == "__main__":
    res_part1, res_part2 = main()
    print(f"part1: {res_part1}")
    print(f"part2: {res_part2}")
