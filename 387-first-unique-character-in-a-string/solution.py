class Solution:
    def firstUniqChar(self, s: str) -> int:
        map = {}

        for e in s:
            map[e] = map.get(e, 0) + 1

        for i in range(len(s)):
            if map[s[i]] == 1:
                return i

        return -1

sol = Solution()
print(sol.firstUniqChar("leetcode") == 0)
print(sol.firstUniqChar("loveleetcode") == 2)
print(sol.firstUniqChar("aabb") == -1)