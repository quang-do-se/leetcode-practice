from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]

        for s in strs[1:]:
            new_prefix = []
            i = 0
            while i < len(s) and i < len(prefix):
                if prefix[i] == s[i]:
                    new_prefix.append(s[i])
                else:
                    break
                i += 1
            prefix = new_prefix

        return "".join(prefix)


sol = Solution()
print(sol.longestCommonPrefix(["flower","flow","flight"]))
print(sol.longestCommonPrefix(["cir","car"]))
print(sol.longestCommonPrefix(["dog","racecar","car"]))
