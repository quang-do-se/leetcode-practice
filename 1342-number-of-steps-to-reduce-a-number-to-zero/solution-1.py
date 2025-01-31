class Solution:
    def numberOfSteps(self, num: int) -> int:
        if num == 0:
            return 0
        
        count = 0
        while num > 0:
            if num & 1:
                count += 2
            else: 
                count += 1
            num = num >> 1

        return count - 1


sol = Solution()
print(sol.numberOfSteps(14))
print(sol.numberOfSteps(0))