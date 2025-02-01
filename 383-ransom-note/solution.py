class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine):
            return False

        map = {}
        for c in magazine:
            if c in map:
                map[c] += 1
            else:
                map[c] = 1

        for c in ransomNote:
            if c in map and map[c] > 0:
                map[c] -= 1
            else:
                return False
        return True


sol = Solution()
print(sol.canConstruct("a", "b") == False)
print(sol.canConstruct("aa", "ab") == False)
print(sol.canConstruct("aa", "aab") == True)