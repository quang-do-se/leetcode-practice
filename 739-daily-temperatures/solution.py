from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0] * n
        stack = []

        for i in range(n):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                res[stack[-1]] = i - stack[-1]
                stack.pop()

            stack.append(i)

        return res


sol = Solution()
print(
    sol.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]) == [1, 1, 4, 2, 1, 1, 0, 0]
)
print(sol.dailyTemperatures([30, 40, 50, 60]) == [1, 1, 1, 0])
print(sol.dailyTemperatures([30, 60, 90]) == [1, 1, 0])
print(sol.dailyTemperatures([60, 60, 60]) == [0, 0, 0])
print(sol.dailyTemperatures([60, 50, 40]) == [0, 0, 0])
