class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        min_len = min(len(word1), len(word2))
        s = ''

        for i in range(min_len):
            s += word1[i] + word2[i]

        return s + word1[min_len:] + word2[min_len:]


sol = Solution()
print(sol.mergeAlternately("abc", "pqr") == "apbqcr")