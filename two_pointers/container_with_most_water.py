"""
Container With Most Water
-------------------------

Problem:
    Given an array of heights, find two lines that together with
    the x-axis form a container that holds the maximum amount of water.

Example:
    Input:  [1,8,6,2,5,4,8,3,7]
    Output: 49

Algorithm (Two Pointers):
    1. Start with left = 0 and right = n - 1.
    2. Calculate area = min(height[left], height[right]) * (right - left).
    3. Update max_area if needed.
    4. Move the pointer at the shorter line inward.
    5. Repeat until left < right.

Time Complexity:
    O(n)  - each pointer moves at most n steps
Space Complexity:
    O(1)  - no extra data structures

Details:
1. What are we trying to measure?

    We’re trying to find the area of water that can be contained between two vertical lines (like walls of a container).
    Each element in height[] is a vertical line.
    Pick two lines at indices i and j (with i < j).
    The water is trapped between them, and its size depends on:
    The shorter line’s height (because water spills over if we try to count the taller one).
    The distance between the lines (width of the container).

2. Why min(height[i], height[j])?

    If one line is shorter than the other, water will overflow at the shorter line’s height.
    So the effective height of the container = the minimum height of the two.

"""

from typing import List


def max_area(height: List[int]) -> int:
    left, right = 0, len(height) - 1
    max_area_val = 0
    while left < right:
        area = min(height[left], height[right]) * (right - left)
        if area > max_area_val:
            max_area_val = area
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return max_area_val


if __name__ == "__main__":
    nums = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    print(f"Max water container area: {max_area(nums)}")
