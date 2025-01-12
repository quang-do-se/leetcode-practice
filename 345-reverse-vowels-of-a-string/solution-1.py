class Solution:
    def reverseVowels(self, s: str) -> str:
        # Two pointers approach
        vowels = set('aeiouAEIOU')

        left_pointer = 0
        right_pointer = len(s) - 1
        s_array = list(s)

        while left_pointer < right_pointer:
            if s_array[left_pointer] in vowels:
                while s_array[right_pointer] not in vowels:
                    right_pointer -= 1

                # Swap characters
                s_array[left_pointer], s_array[right_pointer] = s_array[right_pointer], s_array[left_pointer]
                right_pointer -= 1

            left_pointer += 1

        return ''.join(s_array)


sol = Solution()
print(sol.reverseVowels("All") == "All")
print(sol.reverseVowels("IceCreAm") == "AceCreIm")
print(sol.reverseVowels("leetcode") == "leotcede")
print(sol.reverseVowels("") == "")
print(sol.reverseVowels("a") == "a")
print(sol.reverseVowels("E") == "E")
print(sol.reverseVowels("C") == "C")