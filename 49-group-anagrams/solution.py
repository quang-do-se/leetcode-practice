from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        map = {}
        for s in strs:
            sorted_s = tuple(sorted(s))
            if sorted_s in map:
                map[sorted_s].append(s)
            else:
                map[sorted_s] = [s]

        res = list()
        for e in map:
            res.append(map[e])

        return res
    

sol = Solution()
print(sol.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]) == [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']])
print(sol.groupAnagrams(["", ""]) == [["", ""]])