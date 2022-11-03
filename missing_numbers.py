# Find the missing numbers

nums = [2, 3, 7, 9, 0, 12]


def missing_numbers(array):
    missing_nums = []

    for i in range(min(array), max(array)):
        if i not in array:
            missing_nums.append(i)
    return missing_nums


print(missing_numbers(nums))
