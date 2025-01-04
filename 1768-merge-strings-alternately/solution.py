class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        len1, len2 = len(word1), len(word2)
        minLen = min(len1, len2)
        s = []
        i = 0
        
        while i < minLen:
            s.append(word1[i])
            s.append(word2[i])
            i += 1

        while i < len1:
            s.append(word1[i])
            i += 1

        while i < len2:
            s.append(word2[i])
            i += 1

        return ''.join(s)
    
sol = Solution()
print(sol.mergeAlternately("abc", "pqr"))
