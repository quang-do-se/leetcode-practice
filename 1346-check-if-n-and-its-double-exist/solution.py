from typing import List


class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        map = {}
        for e in arr:
            if e in map:
                map[e] += 1
            else:
                map[e] = 1

        for e in arr:
            de = e * 2
            if de in map:
                if e == 0 and map[e] == 1:
                    continue
                return True

        return False


sol = Solution()
print(sol.checkIfExist([10,2,5,3]) == True)
print(sol.checkIfExist([3,1,7,11]) == False)
print(sol.checkIfExist([-2,0,10,-19,4,6,-8]) == False)