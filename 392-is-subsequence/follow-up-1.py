import bisect

class Solution:
    def __init__(self, t: str):
        # Preprocess `t`
        self.char_map = {}
        for i, char in enumerate(t):
            if char not in self.char_map:
                self.char_map[char] = [i]
            else:
                self.char_map[char].append(i)

    def isSubsequence(self, s: str) -> bool:
        # Check if `s` is a subsequence of `t`
        current_position = -1
        for char in s:
            if char not in self.char_map:
                return False

            # Find the next occurrence of `char` in `t` using binary search
            index_list = self.char_map[char]
            next_position = bisect.bisect_right(index_list, current_position)

            # `bisect_right()` returns the right most index where `x` can be inserted to maintain the sorted order.
            # If `x` or `current_position` is not found, it returns an index equal to `len(list)`
            if next_position == len(index_list):
                return False

            current_position = index_list[next_position]

        return True


# Example usage
t = "ahbgdcea"
sol = Solution(t)

print(sol.isSubsequence(""))     # True
print(sol.isSubsequence("abc"))  # True
print(sol.isSubsequence("abec")) # False


"""
My note: This approach is to build a precomputed map.

{
  'a': [0, 7],
  'h': [1],
  'b': [2],
  ...
}

Reference: ChatGPT

Implementation Steps:

    1. Preprocessing:
       The preprocessing step creates a mapping of character positions in t. This allows us to quickly look up where each character appears.

    2. Checking Subsequence:
       For each `s`, the `isSubsequence` method uses binary search to find the next valid position of each character in `t`.
       This avoids rescanning `t` from the start.

Time Complexity:

    Preprocessing: O(n) where n is the length of `t`
    Checking each subsequence: O(m * logn) where m is the length of `s`

    For k elements of s, the time complexity is O(n + k * m * logn) or O(n + kmlogn)

Space Complexity:

    O(t) where the map contains all characters `c` in `t` and each character `c` contains a list of all `c` posiion in `t`
"""