class Solution:
    def reverseWords(self, s: str) -> str:
        words = []
        word = []

        for c in s:
            if c.isalnum():
                word += c
            elif c == ' ':
                if len(word) > 0:
                    words.append(''.join(word))
                word = []

        if len(word) > 0:
            words.append(''.join(word))

        words.reverse()

        return ' '.join(words)


sol = Solution()
print(sol.reverseWords("the sky is blue") == "blue is sky the")
print(sol.reverseWords("   hello   world ") == "world hello")
print(sol.reverseWords("a good   example") == "example good a")
print(sol.reverseWords("a good   example 123 456") == "456 123 example good a")
