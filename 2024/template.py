FILENAME = "input.txt"

from copy import deepcopy


# retrieves the input file and elaborates it
def parse_puzzle():
    file = open(FILENAME, "r", encoding="utf-8")

    for line in file:
        pass


def solve_part_one(puzzle):
    pass


# *************************************
#              part 2
# *************************************


def solve_part_two(puzzle):
    pass


if __name__ == "__main__":
    puzzle = parse_puzzle()

    result1 = solve_part_one(deepcopy(puzzle))
    print(f"result1: {result1}")

    result2 = solve_part_two(deepcopy(puzzle))
    print(f"result2: {result2}")
