class Solution:
    def maxArea(self, height: list[int]) -> int:
        # Brute force n^2
        i = 0
        size = len(height)
        max = 0

        while i < size:
            j = i + 1
            while j < size:
                area = min(height[i], height[j]) * (j - i)
                if area > max:
                    max = area
                j += 1
            i += 1

        return max

sol = Solution()
print(sol.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49)
print(sol.maxArea([1,1]) == 1)
print(sol.maxArea([2,3]) == 2)