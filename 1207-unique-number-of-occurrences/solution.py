from typing import List


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        count = {}
        for n in arr:
            if n in count:
                count[n] += 1
            else:
                count[n] = 1

        unique = {}
        for k in count:
            if count[k] in unique:
                return False
            else:
                unique[count[k]] = 1

        return True


sol = Solution()
print(sol.uniqueOccurrences([1,2,2,1,1,3]) == True)
print(sol.uniqueOccurrences([1,2]) == False)