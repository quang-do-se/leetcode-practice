class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ['a', 'e', 'i', 'o', 'u']
        found_vowels = []

        for c in s:
            if c.lower() in vowels:
                found_vowels.append(c)

        new_string = ""
        reversed_index = len(found_vowels) - 1
        for c in s:
            if c.lower() in vowels:
                new_string += found_vowels[reversed_index]
                reversed_index -= 1
            else:
                new_string += c

        return new_string


sol = Solution()
print(sol.reverseVowels("IceCreAm") == "AceCreIm")
print(sol.reverseVowels("leetcode") == "leotcede")
print(sol.reverseVowels("") == "")
print(sol.reverseVowels("a") == "a")
print(sol.reverseVowels("E") == "E")
print(sol.reverseVowels("C") == "C")