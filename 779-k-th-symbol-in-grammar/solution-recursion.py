class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if n == 1:
            return 0

        previous_number = self.kthGrammar(n - 1, k // 2 + k % 2)

        """
        If the next number is the first digit of the expanded number, it will be the same as the previous number
        If the next number is the second digit, it will be flipped

        Obserse this, notice the first digit is the same as previous number
        0 -> 01
        1 -> 10
        """

        return previous_number ^ (k % 2 ^ 1)


sol = Solution()
print(sol.kthGrammar(1, 1) == 0)
print(sol.kthGrammar(2, 1) == 0)
print(sol.kthGrammar(2, 2) == 1)
print(sol.kthGrammar(5, 15) == 1)
print(sol.kthGrammar(4, 5) == 1)