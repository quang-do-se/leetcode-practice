class Solution:
    def __init__(self, t: str):
        self.next = self.preprocess(t)

    def preprocess(self, t: str):
        next = [[-1] * 26 for _ in range(len(t))]

        for i in range(len(t) - 1, -1, -1):
            for c in range(26):
                if i < len(t) - 1:
                    next[i][c] = next[i + 1][c]

                if ord(t[i]) - ord('a') == c:
                    next[i][c] = i

        return next

    def isSubsequence(self, s: str):
        j = 0

        for c in s:
            j = self.next[j][ord(c) - ord('a')]

            if j == -1:
                return False

        return True


# Example usage:
t = "ahbgdcea"
sol = Solution(t)

print(sol.isSubsequence(""))     # True
print(sol.isSubsequence("abc"))  # True
print(sol.isSubsequence("abec")) # False


"""
My note: This approach is quite similar to build a precomputed trie.

Reference: Google AI

To optimize the code when checking if a large number of strings (s1, s2, ..., sk) are subsequences of t, where k is very large (>= 10^9), you should pre-process the string `t` to create a data structure that allows for fast lookups of character positions, such as a hashmap or a dedicated "next" array, which would significantly reduce the time complexity of checking each new string `s` against `t`.
Key idea: Instead of iterating through `t` for every `s` to find the next occurrence of a character, pre-process `t` to store the next position of each character, allowing you to jump directly to the relevant position when checking a new string `s`.

Implementation Steps:

    1. Preprocessing:
        Create a 2D array next of size (length of t, number of unique characters c) where next[i][c] stores the index of the next occurrence of character `c` in `t` after position `i`.
        If a character `c` does not appear after position `i`, set next[i][c] to -1.

    2. Checking Subsequence:
        For each string `s`:
            Initialize a pointer j to 0 (current position in `t`).
            Iterate through each character `c` in `s`:
                If j < 0: return False (since we couldn't find the previous character in `t`)
                Update j = next[j][c] (jump to the next occurrence of `c` in `t`)
        If we reach the end of `s` while j is still a valid index, return True (s is a subsequence of t).

Time Complexity:

    Preprocessing: O(n) where n is the length of `t`
    Checking each subsequence: O(m) where m is the length of `s`

    For k elements of s, the time complexity is O(n + km)

Space Complexity:

    O(t * alphabet_size) due to the `next` array, where alphabet_size is the number of unique characters in the alphabet.
"""