# Instructions for this problem are again confusing
# We have array of numbers
# For each value we need to replace value with value
# that is biggest number from right side of array and last one change to -1
# [5, 10, 15, 20] -> [20, 20, 20, -1]
# [17, 18, 5, 4, 6, 1] -> [18, 6, 6, 6, 1, -1]
# Instructions are that we need to replace each element even if it is bigger than
# rest of the array to right


def replaceElements(list):

    index_of_arr = 1
    length_or_arr = len(list)

    for each_element in list:
        sub_arr = list[index_of_arr:]

        if len(sub_arr) == 0:
            continue
        else:
            max_value_sub_array = max(sub_arr)

        list[(index_of_arr - 1)] = max_value_sub_array
        index_of_arr += 1
    list[(length_or_arr - 1)] = -1

    return list


test_1 = [2, 4, 5, 3, 1, 2]
test_1_result = replaceElements(test_1)

test_2 = [3, 3]
test_2_result = replaceElements(test_2)

test_3 = [5, 10, 15, 20]
test_3_result = replaceElements(test_3)


print(
    f"Restult of test_1 should be: [5, 5, 3, 2, 2, -1] and actual restul is: {test_1_result}"
)
print(f"Restult of test_2 should be: [3, -1] and actual restul is: {test_2_result}")
print(
    f"Restult of test_3 should be: [20, 20, 20 -1] and actual restul is: {test_3_result}"
)
