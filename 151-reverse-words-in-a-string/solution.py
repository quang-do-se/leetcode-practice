class Solution:
    def reverseWords(self, s: str) -> str:
        words = []

        in_word = False
        word = ""
        for c in s:
            if c.isalnum():
                in_word = True
                word += c
            elif c == ' ':
                if in_word:
                    words.append(word)
                word = ""
                in_word = False

        if in_word:
            words.append(word)

        words.reverse()

        return ' '.join(words)


sol = Solution()
print(sol.reverseWords("the sky is blue") == "blue is sky the")
print(sol.reverseWords("   hello   world ") == "world hello")
print(sol.reverseWords("a good   example") == "example good a")
print(sol.reverseWords("a good   example 123 456") == "456 123 example good a")
