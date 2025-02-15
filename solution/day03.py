import re
from typing import List


def read_input():
    with open("day03_input.txt") as file:
        lines = file.readlines()

    return ["".join(lines)]

input = read_input()


def part1(input_list:List[str]):
    total_sum = 0
    for input in input_list:
        pattern_to_capture_mul_int = r"mul\(\d+,\d+\)"
        pattern_to_capture_int_only = r"mul\((\d+),(\d+)\)" # () extract things inside ()
        mul_matches = re.findall(pattern_to_capture_mul_int, input)
        # The map() function is used to apply a given function to every item of an iterable map(func, iterable)
        # By default map function returns map object (iterator)

        # QUESTION: Difference between map and for loop and applying function?
        int_only = [tuple(map(int, re.findall(pattern_to_capture_int_only, mul)[0])) for mul in mul_matches]

        result = sum(x * y for x, y in int_only)
        total_sum += result

    return total_sum


def part2(examples):
    total_sum = 0
    for example in examples:
        pattern = r"(don't|do)"
        splitted = re.split(pattern=pattern,string=example)
        do_index = [index for index, element in enumerate(splitted) if element == "do"]
        dont_index = [index for index, element in enumerate(splitted) if element == "don't"]

        merged_index_list = [(index, "do_index") for index in do_index] + [(index, "dont_index") for index in dont_index]
        sorted_merged_index_list = sorted(merged_index_list)
        need_to_apply_mul = []

        if dont_index:
            index_to_print = list(range(dont_index[0]))
            start_index = dont_index[0]
            write = False
        else:
            index_to_print=[]
            start_index = 0
            write = True

        # QUESTION: What is the smart way to do this? instead of double for loop, and set the condiion index==ind?
        for index in range(start_index, len(splitted)):
            if write and (index not in set([*do_index, *dont_index])):
                index_to_print.append(index)
            for ind, list_name in sorted_merged_index_list:
                if index == ind:
                    if list_name == "do_index":
                        write=True
                    else:
                        write=False


        contents_to_print = [splitted[idx] for idx in index_to_print]
        sum = part1(contents_to_print)
        print(sum)
        total_sum += sum

    print(f"total_sum equals {total_sum}")

example = ["xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"]
part1(example)
part1(input)

part2(["mul(6,7]don't()mul(3,9)"]) # 0
part2(["mul(6,7)don't()mul(3,9)"]) # 42
part2(["don'tmul(6,7]do()mul(3,9)"]) # 27
part2(["don'tmul(6,7]do()mul(3,9])"]) # 0
part2(input)
