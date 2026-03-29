# Improvement - we could easily make function accept 2 parameters,
# second parameter would be how many times we want to duplicate list


def getConcatenation(list):

    how_many_times = 2
    ans = []

    for each in range(how_many_times):
        for each_element in list:
            ans.append(each_element)

    return ans


test_1_list = [1, 4, 1, 2]
result_test_1 = getConcatenation(test_1_list)

test_2_list = [22, 21, 20, 1]
result_test_2 = getConcatenation(test_2_list)

print(
    f"Result of test_1 should be [1, 4, 1, 2, 1, 4, 1, 2] and actual value is: {result_test_1}"
)
print(
    f"Result of test_2 should be [22, 21, 20, 1, 22, 21, 20, 1] and actual value is: {result_test_2}"
)
