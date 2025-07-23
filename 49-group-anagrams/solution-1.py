from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = {}
        for s in strs:
            char_count = [0] * 26
            for c in s:
                char_count[ord(c) - ord('a')] += 1

            new_key = tuple(char_count)

            if new_key in group:
                group[new_key].append(s)
            else:
                group[new_key] = [s]

        return list(group.values())
    

sol = Solution()
print(sol.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]) == [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']])
print(sol.groupAnagrams(["", ""]) == [["", ""]])