class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        slow = fast = 0

        while slow < len(s) and fast < len(t):
            if s[slow] == t[fast]:
                slow += 1
            fast += 1

        return slow == len(s)


sol = Solution()

print(sol.isSubsequence("", "ahbgdcea"))     # True
print(sol.isSubsequence("abc", "ahbgdcea"))  # True
print(sol.isSubsequence("abec", "ahbgdcea")) # False