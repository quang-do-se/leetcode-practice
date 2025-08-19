# Binary Search
class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        current_digit = 0
        low = 0
        high = 2 ** (n - 1)

        while n > 1:
            current_mid = (high - low) // 2 + low

            expand_digit = "01" if current_digit == 0 else "10"

            if k <= current_mid:
                current_digit = int(expand_digit[0])
                high = current_mid
            else:
                current_digit = int(expand_digit[1])
                low = current_mid + 1

            n -= 1

        return int(current_digit)

    

sol = Solution()
print(sol.kthGrammar(1, 1) == 0)
print(sol.kthGrammar(2, 1) == 0)
print(sol.kthGrammar(2, 2) == 1)
print(sol.kthGrammar(5, 15) == 1)
print(sol.kthGrammar(4, 5) == 1)