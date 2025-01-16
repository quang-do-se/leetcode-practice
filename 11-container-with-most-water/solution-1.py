class Solution:
    def maxArea(self, height: list[int]) -> int:
        # Two-pointer greedy algorithm
        size = len(height)
        max = 0

        i = 0
        j = size - 1
        while i < j:
            area = min(height[i], height[j]) * (j - i)
            if area > max:
                max = area
            
            if height[j] < height[i]:
                j -= 1
            else:
                i += 1

        return max

sol = Solution()
print(sol.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49)
print(sol.maxArea([1,1]) == 1)
print(sol.maxArea([2,3]) == 2)