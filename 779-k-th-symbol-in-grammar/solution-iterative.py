# Binary Search
class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        current_digit = 0
        low = 0
        high = 2 ** (n - 1)

        while n > 1:
            current_mid = (high - low) // 2 + low

            if k <= current_mid:
                current_digit = 0 if current_digit == 0 else 1
                high = current_mid
            else:
                current_digit = 1 if current_digit == 0 else 0
                low = current_mid + 1

            n -= 1

        return current_digit


sol = Solution()
print(sol.kthGrammar(1, 1) == 0)
print(sol.kthGrammar(2, 1) == 0)
print(sol.kthGrammar(2, 2) == 1)
print(sol.kthGrammar(5, 15) == 1)
print(sol.kthGrammar(4, 5) == 1)
