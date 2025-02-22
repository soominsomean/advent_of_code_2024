from typing import List
import re

def read_input():
    with open("day04_input.txt") as file:
        lines = file.readlines()

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


def part1(input:List[str]):
    XMAS_COUNTS = 0
    correct_order_list = []
    reverse_order_list = []
    for ex in example:
        correct_order = re.findall(pattern="XMAS", string=ex)
        reverse_order = re.findall(pattern="XMAS", string=ex[::-1])

        correct_order_count = len(correct_order)
        reverse_order_count = len(reverse_order)

        XMAS_COUNTS += correct_order_count
        XMAS_COUNTS += reverse_order_count

    print()

part1(input=example)