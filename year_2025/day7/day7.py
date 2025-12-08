SPLITTER_POSITION = set()
EXISTING_BEAMS = set()
class Beam:
    def __init__(self, position):
        if position in EXISTING_BEAMS:
            return
        EXISTING_BEAMS.add(position)
        self.current_position = position
        self.traverse_down()

    def found_splitter(self):
        if MATRIX[self.current_position[0]][self.current_position[1]] == "^":
            SPLITTER_POSITION.add((self.current_position[0], self.current_position[1]))
        return MATRIX[self.current_position[0]][self.current_position[1]] == "^"


    def split(self):
        if self.current_position[0] < len(MATRIX):
            left_beam = Beam((self.current_position[0], self.current_position[1] - 1))
            right_beam = Beam((self.current_position[0], self.current_position[1] + 1))


    def traverse_down(self):
        while self.current_position[0] < len(MATRIX) and not self.found_splitter():
            self.current_position = self.current_position[0] + 1, self.current_position[1]
        self.split()


MATRIX = []

def read_input():
    with open("input.txt", 'r') as file:
        global MATRIX
        for idx, line in enumerate(file.readlines()):
            MATRIX.append(line)
            if "S" in line:
                position = idx ,line.index("S")
        return MATRIX[position[0]:], position


def main():
    matrix, position = read_input()
    # initial beam
    Beam(position)
    return len(SPLITTER_POSITION), 0



if __name__ == "__main__":
    res_part1, res_part2 = main()
    print(f"part1: {res_part1}")
    print(f"part2: {res_part2}")
