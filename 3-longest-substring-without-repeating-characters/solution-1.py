class Solution:
    # Sliding Window - bad
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        s_len = len(s)
        sub_len = len(s)

        while sub_len > 0:
            start = 0
            end = start + sub_len - 1

            c_dict = {}
            dup = set()
            for i in range(start, end + 1):
                if s[i] in c_dict:
                    dup.add(s[i])
                    c_dict[s[i]] += 1
                else:
                    c_dict[s[i]] = 1
            
            if len(dup) == 0:
                return sub_len
            
            while end < s_len - 1:
                if s[start] in c_dict and c_dict[s[start]] > 0:
                    c_dict[s[start]] -= 1

                    if c_dict[s[start]] == 1:
                        dup.remove(s[start])

                c_dict[s[end + 1]] = c_dict.get(s[end + 1], 0) + 1

                if c_dict[s[end + 1]] > 1:
                    dup.add(s[end + 1])

                if len(dup) == 0:
                    return sub_len
                
                start += 1
                end += 1
            

            sub_len -= 1

        return res


sol = Solution()
print(sol.lengthOfLongestSubstring("") == 0)
print(sol.lengthOfLongestSubstring("abcde") == 5)
print(sol.lengthOfLongestSubstring("abcabcbb") == 3)
print(sol.lengthOfLongestSubstring("pwwkew") == 3)
print(sol.lengthOfLongestSubstring("bbbbb") == 1)