# There is not very clear instructions for this task
# You are given an integer array nums(list) and an integer val(remove_val).
# Your task is to remove all occurrences of val from nums in-place.
# !! in-place meaning that you are not allowed to use another array and
# just move the elements that are not remove_val to new list and measure this new list


def removeElement(list, remove_val):

    element_counter = 0

    for each_element in list:
        if each_element == remove_val:
            element_counter += 1

    for each_count in range(0, element_counter):
        list.remove(remove_val)

    len_of_list = len(list)

    return len_of_list


test_1_list = [1, 1, 2, 3, 4]
test_1_val = 1
result_test_1 = removeElement(test_1_list, test_1_val)

test_2_list = [0, 1, 2, 2, 3, 0, 4, 2]
test_2_val = 2
result_test_2 = removeElement(test_2_list, test_2_val)

print(
    f"Result of test_1 should be [2, 3, 4] and length: 3 and actual value is: {result_test_1}"
)
print(
    f"Result of test_2 should be [0, 1, 3, 0, 4] and length: 5 and actual value is: {result_test_2}"
)
