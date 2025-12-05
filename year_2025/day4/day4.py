def read_input():
    matrix = []
    with open("input.txt", 'r') as file:
        for line in file:
            # replace @ with 1, rest with 0 to simplify summation
            matrix.append([1 if x == "@" else 0 for x in line.strip()])
    return matrix

def main():
    _first_adjacent_node_count,_total_adjacent_node_count = 0, 0
    matrix = read_input()
    _adjacent_node_count, reset_indexes = get_adjacent_node_count(matrix)
    _first_adjacent_node_count, _total_adjacent_node_count = (_adjacent_node_count, _adjacent_node_count)
    matrix = update_matrix(matrix, reset_indexes)
    while _adjacent_node_count:
        _adjacent_node_count, reset_indexes = get_adjacent_node_count(matrix)
        _total_adjacent_node_count += _adjacent_node_count
        matrix = update_matrix(matrix, reset_indexes)
    return _first_adjacent_node_count, _total_adjacent_node_count

def check_left_right(matrix, i, j, is_up_down=False):
    """check adjacency in left and right direction
    is_up_down would be True when checking either 1 row above or below current row
    """
    try:
        if len(matrix[i]) == 1:
            return 0
        elif j <= 0:
            return matrix[i][j + 1] if not is_up_down else matrix[i][j]+matrix[i][j + 1]
        elif j == len(matrix[i]) - 1:
            return matrix[i][j - 1] if not is_up_down else matrix[i][j]+matrix[i][j - 1]
        else:
            return matrix[i][j-1]+matrix[i][j+1]  if not is_up_down else sum(matrix[i][j-1:j+2])
    except IndexError:
        print(matrix, i, j)

def check_up(matrix, i, j):
    """
    check adjacency in 1 row above current row
    """
    if i >= 1:
        return check_left_right(matrix, i-1, j, is_up_down=True)
    return 0

def check_down(matrix, i, j):
    """check adjacency in 1 row below current row"""
    if i < len(matrix)-1:
        return check_left_right(matrix, i+1, j, is_up_down=True)
    return 0

def update_matrix(matrix, reset_indexes):
    """reset nodes that have less than 4 adjacent nodes"""
    for i, j in reset_indexes:
        matrix[i][j] = 0
    return matrix

def get_adjacent_node_count(matrix):
    """get count and position of each node that have less than 4 adjacent nodes"""
    count = 0
    reset_indexes = []
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 1:
                res = check_up(matrix, i, j)+check_down(matrix, i, j)+check_left_right(matrix, i, j,is_up_down=False)
                if res < 4:
                    count += 1
                    reset_indexes.append((i, j))
    return count, reset_indexes


if __name__ == "__main__":
    res_part1, res_part2 = main()
    print(f"part1: {res_part1}")
    print(f"part2: {res_part2}")
