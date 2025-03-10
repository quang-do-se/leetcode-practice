class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        map = {}
        seen = {}
        for i in range(len(s)):
            if s[i] in map:
                if t[i] != map[s[i]]:
                    return False
            else:
                map[s[i]] = t[i]

        return True


sol = Solution()
print(sol.isIsomorphic("egg", "add"))
print(sol.isIsomorphic("foo", "bar"))
print(sol.isIsomorphic("paper", "title"))