# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

def isBadVersion(n):
    if n >= 4:
        return True
    return False

class Solution:
    def firstBadVersion(self, n: int) -> int:
        l = 1
        h = n

        while l < h:
            m = l + (h - l) // 2
            if isBadVersion(m):
                h = m
            else:
                l = m + 1
        
        return l
    
sol = Solution()
print(sol.firstBadVersion(5))