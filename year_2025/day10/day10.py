def read_input():
    import re
    with open("input.txt", 'r') as file:
        indicator_lights = []
        button_combinations = []
        for line in file.readlines():
            indicator_lights.append(re.findall("\[(.*?)\]",line)[0])
            button_combinations.append(re.findall("\((.*?)\)",line))
        return indicator_lights, button_combinations,

def check_if_indicator_light_matches(indicator_light, button_combination):
    indicator_light_map = {idx: int(char == "#") for idx, char in enumerate(indicator_light)}
    temp = {idx: 0 for idx in indicator_light_map.keys()}

    for button in button_combination:
        indices = list(map(int, button.split(",")))
        for index in indices:
            temp[index] = (temp.get(index, 0) + 1) % 2

    return indicator_light_map == temp


def generate_button_combinations(button_combinations):
    """Generate all possible combinations of button presses ordered by least combinations"""
    all_combinations = {}
    i = 1
    from itertools import combinations
    while i <= len(button_combinations):
        temp = combinations(button_combinations, i)
        all_combinations[i] = list(temp)
        i +=1
    return all_combinations


def get_minimum_button_presses(line, indicator_light):
    """get minimum button presses to match indicator light"""
    all_combinations = generate_button_combinations(line)
    for button_presses, combos in all_combinations.items():
        for combo in combos:
            if check_if_indicator_light_matches(indicator_light, combo):
                return button_presses

def main():
    indicator_lights, button_combinations,  = read_input()
    min_button_presses_part1,_ = 0, 0
    for idx, line in enumerate(button_combinations):
        min_button_presses_part1 += get_minimum_button_presses(line, indicator_lights[idx])
    return min_button_presses_part1, _


if __name__ == "__main__":
    res_part1, res_part2 = main()
    print(f"part1: {res_part1}")
    print(f"part2: {res_part2}")