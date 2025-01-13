class Solution:
    def reverseWords(self, s: str) -> str:
        # Python built-in solution
        return ' '.join(s.split()[::-1])


sol = Solution()
print(sol.reverseWords("the sky is blue") == "blue is sky the")
print(sol.reverseWords("   hello   world ") == "world hello")
print(sol.reverseWords("a good   example") == "example good a")
print(sol.reverseWords("a good   example 123 456") == "456 123 example good a")
