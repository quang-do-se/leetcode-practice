class Solution:
    def tribonacci(self, n: int) -> int:
        first = 0
        second = 1
        third = 1

        for i in range(n):
            temp = first + second + third
            first = second
            second = third
            third = temp
            
        return first
    
sol = Solution()
print(sol.tribonacci(0) == 0)
print(sol.tribonacci(1) == 1)
print(sol.tribonacci(2) == 1)
print(sol.tribonacci(4) == 4)
print(sol.tribonacci(25) == 1389537)