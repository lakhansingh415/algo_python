# contains duplicate in a list Brute force
def contains_duplicate_using_list(nums):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] == nums[j]:
                return True
    return False

def contains_duplicate_using_set(nums):
    unique_set = set()
    for i in nums:
        if i in unique_set:
            return True
        unique_set.add(i)
    return False

if __name__ == '__main__':
    nums1 = [1, 2, 3, 4]
    print(contains_duplicate_using_list(nums1)) # Expected output: False

    nums2 = [1, 2, 3, 1]
    print(contains_duplicate_using_set(nums2)) # Expected output: True

    nums3 = []
    print(contains_duplicate_using_list(nums3)) # Expected output: False

    nums4 = [1, 1, 1, 1]
    print(contains_duplicate_using_set(nums4)) # Expected output: True

