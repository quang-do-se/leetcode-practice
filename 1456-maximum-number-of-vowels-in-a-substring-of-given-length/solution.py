class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowel = set('aeiou')

        max = 0
        for i in range(len(s)):
            if i + k - 1 >= len(s):
                return max

            vowel_count = 0
            for j in range(i, i + k):
                if s[j] in vowel:
                    vowel_count += 1
            if vowel_count > max:
                max = vowel_count

                if max == k:
                    return max

        return max


sol = Solution()
print(sol.maxVowels("abciiidef", 3))
print(sol.maxVowels("aeiou", 2))
print(sol.maxVowels("leetcode", 3))
print(sol.maxVowels("l", 1))
print(sol.maxVowels("a", 1))
