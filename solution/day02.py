from typing import List


def read_input():
    with open("day02_input.txt") as file:
        lines = file.readlines()
    all_reports = []

    for report in lines:
        processed_report = report.split()
        all_reports.append(processed_report)

    print(len(all_reports))
    return all_reports

def part1(input_list:List[List[str]]):
    pos = [1, 2, 3]
    neg = [-1, -2, -3]

    correct_count = 0

    for report in input_list:
        diffs = []

        for i in range(len(report) - 1):
            diff = int(report[i+1]) - int(report[i])
            diffs.append(diff)

        all_in_pos = all(diff in pos for diff in diffs)
        all_in_neg = all(diff in neg for diff in diffs)

        if all_in_pos or all_in_neg:
            correct_count += 1

    print(correct_count)
    return correct_count


def part2(input_list:List[List[str]]):
    pos = [1, 2, 3]
    neg = [-1, -2, -3]

    correct_count = 0

    for report in input_list:
        diffs = []

        for i in range(len(report) - 1):
            diff = int(report[i+1]) - int(report[i])
            diffs.append(diff)

        all_in_pos = all(diff in pos for diff in diffs)
        all_in_neg = all(diff in neg for diff in diffs)

        if all_in_pos or all_in_neg:
            correct_count += 1

        else:
            correct = False
            for i in range(len(report)):
                report_copy = report.copy()
                report_copy.pop(i)
                diffs = []
                for i in range(len(report_copy) - 1):
                    diff = int(report_copy[i + 1]) - int(report_copy[i])
                    diffs.append(diff)

                all_in_pos = all(diff in pos for diff in diffs)
                all_in_neg = all(diff in neg for diff in diffs)

                if all_in_pos or all_in_neg:
                    correct=True
            if correct:
                correct_count +=1

    print(correct_count)
    return correct_count

example = [
    [7, 6, 4, 2, 1,],
    [1, 2, 7, 8, 9,],
    [9, 7, 6, 2, 1,],
    [1, 3, 2, 4, 5,],
    [8, 6, 4, 4, 1,],
    [1, 3, 6, 7, 9,]
]
part1(example)
part2(example)

input_list = read_input()

part1(input_list)
part2(input_list)