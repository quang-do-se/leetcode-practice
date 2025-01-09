class Solution:
    def largestAltitude(self, gain: list[int]) -> int:
        max = sum = 0
        for i in gain:
            sum += i
            if sum > max:
                max = sum
        return max
    
sol = Solution()
print(sol.largestAltitude([-5,1,5,0,-7]) == 1)
print(sol.largestAltitude([0, 0]) == 0)
print(sol.largestAltitude([0, -1, 1]) == 0)
print(sol.largestAltitude([-4,-3,-2,-1,4,3,2]) == 0)