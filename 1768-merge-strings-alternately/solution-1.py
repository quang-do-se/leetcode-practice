class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        minLen = min(len(word1), len(word2))
        s = ''

        for i in range(minLen):
            s += word1[i] + word2[i]

        return s + word1[minLen:] + word2[minLen:]
    
sol = Solution()
print(sol.mergeAlternately("abc", "pqr"))
