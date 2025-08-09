from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        if len(s) <= 1:
            return
        
        self.reverseStringHelper(s, 0, len(s) - 1)
        
    def reverseStringHelper(self, s: List[str], start: int, end: int) -> None:
        if start >= end:
            return
        
        s[start], s[end] = s[end], s[start]

        self.reverseStringHelper(s, start + 1, end - 1)


sol = Solution()

s = ["h","e","l","l","o"]
sol.reverseString(s)
print(s)

s = ["H","a","n","n","a","h"]
sol.reverseString(s)
print(s)        