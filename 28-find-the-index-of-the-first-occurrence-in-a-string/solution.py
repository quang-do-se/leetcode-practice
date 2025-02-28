class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        len_h = len(haystack)
        len_n = len(needle)
        hi = 0

        while hi <= len_h - len_n:
            i = 0
            while i < len_n:
                if haystack[hi + i] != needle[i]:
                    break
                i += 1

            if i == len_n:
                return hi

            hi += 1


        return -1


sol = Solution()
print(sol.strStr("adbutad", "sad"))