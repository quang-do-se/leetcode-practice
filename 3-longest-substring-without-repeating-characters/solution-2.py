class Solution:
    # Sliding Window - accepted
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        s_len = len(s)
        left = 0
        right = 0
        
        c_dict = {}

        while right < s_len:
            dup = False
            c_dict[s[right]] = c_dict.get(s[right], 0) + 1

            if c_dict[s[right]] > 1:
                dup = True

            while dup and left < right:
                c_dict[s[left]] -= 1
                if c_dict[s[left]] < 0:
                    c_dict[s[left]] = 0

                left += 1

                if c_dict[s[right]] == 1:
                    dup = False

            res = max(res, right - left + 1)
            right += 1

        return res


sol = Solution()
print(sol.lengthOfLongestSubstring("") == 0)
print(sol.lengthOfLongestSubstring("abcde") == 5)
print(sol.lengthOfLongestSubstring("abcabcbb") == 3)
print(sol.lengthOfLongestSubstring("pwwkew") == 3)
print(sol.lengthOfLongestSubstring("bbbbb") == 1)
print(sol.lengthOfLongestSubstring("dvdf") == 3)
print(sol.lengthOfLongestSubstring("tmmzuxt") == 5)