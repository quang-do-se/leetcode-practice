class Solution:
    def isHappy(self, n: int) -> bool:
        current = n
        seen = set()

        while True:
            sum = 0
            while current > 0:
                digit = current % 10
                sum += digit ** 2
                current //= 10

            if sum == 1:
                return True

            if sum in seen:
                return False
            
            seen.add(sum)
            current = sum


sol = Solution()
print(sol.isHappy(2))