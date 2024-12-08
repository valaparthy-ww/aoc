import timeit
from collections import defaultdict


def read_input():
    input = []
    with open("input.txt") as f:
        for i, line in enumerate(f.readlines()):
            test_value, nums_string = line.split(": ")
            input.append([int(test_value), nums_string.strip("\n").split(" ")])
    return input


def permute_without_reorder(nums):
    out = []
    if len(nums) == 1:
        out = [nums]
    else:
        for i, c in enumerate(nums):
            if i > 0:
                return out
            for res in permute_without_reorder(nums[i + 1 :]):
                for op in operators:
                    temp = [[c] + [op] + res]
                    out += temp
    return out


def apply_op(stack):
    if len(stack) == 3:
        if stack[1] == "*":
            return int(stack[0]) * int(stack[2])
        elif stack[1] == "+":
            return int(stack[0]) + int(stack[2])
        elif stack[1] == "|":
            return int(stack[0] + stack[2])
    return 0


def eval_left_to_right(expression):
    res = 0
    stack = []
    for c in expression:
        temp = apply_op(stack)
        if temp > 0:
            stack.clear()
            res += temp
            stack.append(str(res))
            res = 0
        stack.append(c)
    if stack:
        assert len(stack) == 3
    return res + apply_op(stack)


def main(cache_test_results):
    res = 0
    for test_result, nums in inp:
        if test_result in cache_test_results and nums in cache_test_results.get(
            test_result
        ):
            res += test_result
            continue
        for expr in permute_without_reorder(nums):
            actual_val = eval_left_to_right(expr)
            assert (
                len(expr) == len(nums) + len(nums) - 1
            ), f"{len(expr)} != {len(nums) + len(nums) - 1}"
            if test_result == actual_val:
                res += test_result
                cache_test_results[test_result].append(nums)
                break
    return res, cache_test_results


if __name__ == "__main__":
    start = timeit.default_timer()
    inp = read_input()
    # part 1
    operators = ["+", "*"]
    cache_test_results = defaultdict(list)
    res_part1, cache_test_results = main(cache_test_results)
    # part 2
    operators = operators + ["|"]
    res_part2, _ = main(cache_test_results)
    print(f"The difference of time is : {timeit.default_timer() - start} seconds",)
    print(res_part1, res_part2)
