"""
Remove Duplicates from Sorted Array
-----------------------------------

Problem:
    Given a sorted array nums, remove duplicates in-place
    such that each unique element appears only once.
    Return the number of unique elements.

Example:
    Input:  [0,0,1,1,1,2,2,3,3,4]
    Output: 5
    Array after modification: [0,1,2,3,4,_,_,_,_,_]

Algorithm (Two Pointers):
    1. Use two pointers: `slow` and `fast`.
    2. `slow` points to the position of the last unique element.
    3. Iterate with `fast`:
        - If nums[fast] != nums[slow],
          increment slow and copy nums[fast] to nums[slow].
    4. Return slow + 1 as the length of the unique array.

Time Complexity:
    O(n)  - each element visited once
Space Complexity:
    O(1)  - in-place modification
"""

from typing import List


def remove_duplicates(nums: List[int]) -> int:
    if not nums:
        return 0

    slow = 0

    for fast in range(1, len(nums)):
        if nums[fast] != nums[slow]:
            slow += 1
            nums[slow] = nums[fast]

    return slow + 1


if __name__ == "__main__":
    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    k = remove_duplicates(nums)
    print(f"Unique count: {k}")
    print(f"Array after modification: {nums[:k]}")
