from typing import List
import numpy as np

def read_input():
    with open("day01_input.txt") as file:
        lines = file.readlines()
    list1 = []
    list2 = []

    for i in range(len(lines)):
        list1.append(int(lines[i].split('   ')[0]))
        list2.append(int(lines[i].split('   ')[1]))

    return list1, list2

# PART 1
def calculate_distance_between_two_lists(list1:List, list2:List):
    sorted_list1 = sorted(list1)
    sorted_list2 = sorted(list2)

    distances = 0
    for i, j in zip(sorted_list1, sorted_list2):
        distance = abs(i-j)
        distances += distance

    print(distances)

    return distances

def test_calculate_distance_between_two_lists():
    list1 = [3, 4, 2, 1, 3, 3]
    list2 = [4, 3, 5, 3, 9, 3]

    actual_result = calculate_distance_between_two_lists(list1, list2)
    expected_result = 11

    print(f"{actual_result==expected_result}")


list1, list2 = read_input()
test_calculate_distance_between_two_lists()
calculate_distance_between_two_lists(list1,list2)

# PART 2
def calculate_similarity_score(list1:List, list2:List):
    total_similarity_score = 0

    for i in list1:
        np_list2 = np.array(list2)
        deducted_list2 = np_list2 - i
        count_same_num = int((deducted_list2==0).sum())
        sim_score = i * count_same_num
        total_similarity_score += sim_score

    print(total_similarity_score)
    return total_similarity_score

def test_calculate_similarity_score():
    list1 = [3, 4, 2, 1, 3, 3]
    list2 = [4, 3, 5, 3, 9, 3]

    actual_result = calculate_similarity_score(list1, list2)
    expected_result = 31

    print(f"{actual_result==expected_result}")


test_calculate_similarity_score()
calculate_similarity_score(list1=list1, list2=list2)