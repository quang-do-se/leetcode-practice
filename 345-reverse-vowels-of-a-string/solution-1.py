class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set('aeiouAEIOU')

        l = 0
        r = len(s) - 1
        a = list(s)

        while l < r:
            if a[l] in vowels:
                while a[r] not in vowels:
                    r -= 1

                a[l], a[r] = a[r], a[l]
                r -= 1

            l += 1

        return ''.join(a)


sol = Solution()
print(sol.reverseVowels("All") == "All")
print(sol.reverseVowels("IceCreAm") == "AceCreIm")
print(sol.reverseVowels("leetcode") == "leotcede")
print(sol.reverseVowels("") == "")
print(sol.reverseVowels("a") == "a")
print(sol.reverseVowels("E") == "E")
print(sol.reverseVowels("C") == "C")