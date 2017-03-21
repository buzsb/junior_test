def max_sum_sub_list(array):
    if array == []:
        raise ValueError

    temporary_sum = max_sum = array[0]
    i = 0
    start = finish = 0
    for j in range(1, len(array)):
        if array[j] > (temporary_sum + array[j]):
            temporary_sum = array[j]
            i = j
        else:
            temporary_sum += array[j]
        if temporary_sum > max_sum:
            max_sum = temporary_sum
            start = i
            finish = j

    return array[start:finish + 1]


print max_sum_sub_list([1, -2, 3, -1, 5, -6])
print max_sum_sub_list([-3, 2, 6, -4])
