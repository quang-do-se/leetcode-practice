class Solution:
    # Brute Force - Time Limit Exceeded
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        s_len = len(s)
        sub_len = len(s)

        start = 0
        while sub_len > 0:

            while start + sub_len <= s_len:
                i = 0
                dup = set()
                while i < sub_len:
                    c = s[start + i]
                    #print(c, end="")

                    if c in dup:
                        break
                    else:
                        dup.add(c)

                    i += 1 

                #print()

                if i == sub_len:
                    return sub_len

                start += 1

            sub_len -= 1
            start = 0

        return res


sol = Solution()
print(sol.lengthOfLongestSubstring("") == 0)
print(sol.lengthOfLongestSubstring("abcde") == 5)
print(sol.lengthOfLongestSubstring("abcabcbb") == 3)
print(sol.lengthOfLongestSubstring("pwwkew") == 3)
print(sol.lengthOfLongestSubstring("bbbbb") == 1)