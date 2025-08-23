class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        count = 0
        for i in range(len(s) - 1, -1, -1):
            if s[i] == ' ':
              if count > 0:
                break
              else:
                continue
            else:
               count += 1

        return count

s = Solution()
print(s.lengthOfLastWord("") == 0)
print(s.lengthOfLastWord("a "))
print(s.lengthOfLastWord("Hello World") == 5)
print(s.lengthOfLastWord("   fly me   to   the moon  ") == 4)
