class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if s == "":
            return True

        slow = 0

        for c in t:
            if c == s[slow]:
                slow += 1
                if slow == len(s):
                    return True
        
        return False

    
sol = Solution()
print(sol.isSubsequence("b", "abc"))