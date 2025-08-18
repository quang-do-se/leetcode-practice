class Solution:
    map = {0: "01", 1: "10"}

    def kthGrammar(self, n: int, k: int) -> int:
        if n == 1:
            return 0
        
        previous_number = self.kthGrammar(n - 1, k // 2 + k % 2)

        expand_previous_number = self.map[previous_number]

        return int(expand_previous_number[k % 2 ^ 1])
    

sol = Solution()
print(sol.kthGrammar(5, 5))