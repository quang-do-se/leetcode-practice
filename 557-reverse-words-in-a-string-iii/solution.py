from collections import deque


class Solution:
    def reverseWords(self, s: str) -> str:
        words = deque([])
        word = []

        for i in range(len(s) - 1, -1, -1):
            if s[i] == ' ':
                if word:
                    words.appendleft(''.join(word))
                    word = []
            else:
                word.append(s[i])
        
        if word:
            words.appendleft(''.join(word))
            
        return ' '.join(words)


sol = Solution()
print(sol.reverseWords("ab cd ef"))