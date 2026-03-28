def findMaxConsecutiveOnes(list):

    count_in_row = 0
    max_consecutive = 0

    for each_value in list:
        if each_value == 1:
            count_in_row += 1

        else:
            if count_in_row > max_consecutive:
                max_consecutive = count_in_row
            count_in_row = 0

    if count_in_row > max_consecutive:
        max_consecutive = count_in_row

    return max_consecutive


test_1 = [1, 1, 0, 1, 1, 1]
result_test_1 = findMaxConsecutiveOnes(test_1)

test_2 = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0]
result_test_2 = findMaxConsecutiveOnes(test_2)

print(f"Result of test_1 should equal to 3, and actual result is {result_test_1}")
print(f"Result of test_2 should equal to 1, and actual result is {result_test_2}")
