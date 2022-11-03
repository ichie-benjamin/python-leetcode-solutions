# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.


def contains_duplicate(nums) -> bool:
    """
    :type nums: List[int]
    :rtype: bool
    """
    lists = []
    for i in nums:
        if i in lists:
            return True
        lists.append(i)

    return False


def contains_duplicate_2(nums):
    # using set
    hashset = set(nums)
    return not (len(hashset) == len(nums))


numbers = {1, 3, 5, 7, 2}
print(contains_duplicate(numbers))
print(contains_duplicate_2(numbers))
