class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        sum  = 0
        for i in range(k):
            sum += nums[i]
        
        max = sum
        r = k
        l = 0
        size = len(nums)

        while r < size:
            sum += nums[r]
            sum -= nums[l] 
            if sum > max:
                max = sum
            r += 1
            l += 1

        return max / k
    
sol = Solution()
print(sol.findMaxAverage([1, 12, -5, -6, 50, 3], 4) == 12.75)
print(sol.findMaxAverage([5], 1) == 5.0)
print(sol.findMaxAverage([5, -6], 2) == -0.5)