def read_input():
    with open("input.txt", 'r') as file:
        matrix = []
        for idx, line in enumerate(file.readlines()):
            matrix.append(tuple(int(x) for x in line.strip().split(",")))
        return matrix

def calculate_area(corner1, corner2):
    length = max(abs(corner1[0] - corner2[0])+1,1)
    width = max(abs(corner1[1] - corner2[1])+1,1)
    return length * width


def get_max_rectangle_area(locations):
    max_area = 0
    for idx, loc in enumerate(locations):
        for next_loc in locations[idx+1:]:
            max_area = max(max_area, calculate_area(loc, next_loc))
    return max_area


def main():
    locations = read_input()
    max_area = get_max_rectangle_area(locations)
    return max_area, 0


if __name__ == "__main__":
    res_part1, res_part2 = main()
    print(f"part1: {res_part1}")
    print(f"part2: {res_part2}")