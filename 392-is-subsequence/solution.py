class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if s == "":
            return True

        slow = 0
        count_match = 0

        for c in t:
            if c == s[slow]:
                slow += 1
                count_match +=1
                if count_match == len(s):
                    return True
        
        return False
    
sol = Solution()
print(sol.isSubsequence("b", "abc"))