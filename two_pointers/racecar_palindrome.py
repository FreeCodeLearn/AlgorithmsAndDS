"""
Palindrome Check using Two Pointers
-----------------------------------

Problem:
    Given a string `s`, determine if it is a palindrome,
    considering only alphanumeric characters and ignoring cases.

    A palindrome is a string that reads the same backward as forward.

Example:
    Input: "racecar"
    Output: True

    Input: "hello"
    Output: False

Algorithm (Two Pointers):
    1. Initialize two pointers:
        - left starting at the beginning of the string
        - right starting at the end of the string
    2. While left < right:
        - Compare characters at `s[left]` and `s[right]`
        - If they differ → return False
        - Otherwise, move pointers inward (left++, right--)
    3. If the loop completes, the string is a palindrome → return True

Time Complexity:
    O(n)  - each character is checked at most once
Space Complexity:
    O(1)  - no extra data structures are used
"""


def is_palindrome(s: str) -> bool:
    """
    Check if the given string is a palindrome using the Two Pointers approach.

    :param s: Input string
    :return: True if palindrome, False otherwise
    """
    # Normalize string: keep only alphanumeric and lowercase
    s = "".join(ch.lower() for ch in s if ch.isalnum())

    left, right = 0, len(s) - 1

    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1

    return True


if __name__ == "__main__":
    # Example tests
    examples = ["racecar", "level", "hello", "A man, a plan, a canal: Panama"]

    for word in examples:
        print(f"'{word}' -> {is_palindrome(word)}")
