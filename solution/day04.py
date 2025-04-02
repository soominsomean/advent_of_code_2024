from typing import List
import re

def read_input():
    with open("day04_input.txt") as file:
        lines = [line.strip() for line in file.readlines()]

    return lines

example = [
    "MMMSXXMASM",
    "MSAMXMSMSA",
    "AMXSXMAAMM",
    "MSAMASMSMX",
    "XMASAMXAMM",
    "XXAMMXXAMA",
    "SMSMSASXSS",
    "SAXAMASAAA",
    "MAMMMXMMMM",
    "MXMXAXMASX",
]

# row wise:
    # 정방향 3
    # 역방향 2

# col wise:
    # 정방향 1
    # 역방향 2

# diagonal
    # 왼오 아래 1
    # 왼오 위 4
    # 오왼 아래 1
    # 오아래 왼 4


def xmas_correct_reverse_order_count(input:List[str]):
    XMAS_COUNTS = 0
    correct_order_list = []
    reverse_order_list = []
    for ex in input:
        reverse_ex = ex[::-1]

        correct_order = re.findall(pattern="XMAS", string=ex)
        reverse_order = re.findall(pattern="XMAS", string=reverse_ex)

        correct_order_count = len(correct_order)
        reverse_order_count = len(reverse_order)

        XMAS_COUNTS += correct_order_count
        XMAS_COUNTS += reverse_order_count
        print(XMAS_COUNTS)
    return XMAS_COUNTS


def part1(input:List[str]):

    column_wise = []
    for j in range(len(input[0])):
        new_element = ''
        for element in input:
            new_element = new_element + element[j]
        column_wise.append(new_element)

    input_reversed = [element[::-1] for element in input]
    input_reversed_reversed = input_reversed[::-1]

    left_upper = get_diagonals(input)
    left_lower = get_diagonals(input_reversed_reversed)
    left_lower = left_lower[:(len(left_lower)-1)]
    left_diagonal_wise = list(set([*left_upper, *left_lower]))


    right_upper = get_diagonals(input_reversed)
    right_lower = get_diagonals(input[::-1])
    right_lower = right_lower[:(len(right_lower) -1)]
    right_diagonal_wise = list(set([*right_upper, *right_lower]))


    row_count = xmas_correct_reverse_order_count(input)
    column_count = xmas_correct_reverse_order_count(column_wise)
    left_diagonal_count = xmas_correct_reverse_order_count(left_diagonal_wise)
    right_diagonal_count = xmas_correct_reverse_order_count(right_diagonal_wise)

    print(f"{input=}")
    print(f"{column_wise=}")
    print(f"{left_diagonal_wise=}")
    print(f"{right_diagonal_wise=}")

    total_count = row_count + column_count + left_diagonal_count + right_diagonal_count
    print(f"{row_count=}")
    print(f"{column_count=}")
    print(f"{left_diagonal_count=}")
    print(f"{left_diagonal_count=}")
    print(f"{total_count=}")

    return total_count

def get_diagonals(input:List[str]):
    left_diagonal_wise = []

    for loc in range(len(input[0])):
        new_element = ''
        for i in range(loc + 1):
            second_element = loc - i
            new_element = new_element + input[i][second_element]
        left_diagonal_wise.append(new_element)


    return left_diagonal_wise

# part1(input=example)

part1(input=read_input())
