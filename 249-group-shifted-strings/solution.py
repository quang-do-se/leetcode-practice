from typing import List


class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        groups = {}
        for s in strings:
            key = [0] * (len(s) - 1)
            for i in range(1, len(s)):
                key.append((ord(s[i]) - ord(s[i - 1])) % 26)
            
            group_key = tuple(key)

            if group_key in groups:
                groups[group_key].append(s)
            else:
                groups[group_key] = [s]

        return list(groups.values())


sol = Solution()
print(sol.groupStrings(["abc","bcd","acef","xyz","az","ba","a","z"]))
print(sol.groupStrings(["abc","bcd","acef","xyz","az","ba","a","z", "gikm"]))
print(sol.groupStrings(["a"]))
