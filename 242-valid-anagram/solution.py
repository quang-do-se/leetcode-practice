class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        map = {}

        for c in s:
            map[c] = map.get(c, 0) + 1

        for c in t:
            map[c] = map.get(c, 0) - 1

            # We only need to check `t` since if `s` and `t` are the same length and they have different characters, some count will become negative
            if map[c] < 0:
                return False

        return True


sol = Solution()
print(sol.isAnagram("anagram", "nagaram") == True)
print(sol.isAnagram("rat", "car") == False)
print(sol.isAnagram("abc", "ab") == False)
print(sol.isAnagram("ab", "abc") == False)
print(sol.isAnagram("abc", "abc") == True)
