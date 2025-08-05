class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s_words = s.split()
        p_to_w = {}
        w_to_p = {}

        if len(pattern) != len(s_words):
            return False

        for i in range(len(pattern)):
            if pattern[i] in p_to_w:
                if p_to_w[pattern[i]] != s_words[i]:
                    return False
            else:
                if s_words[i] in w_to_p:
                    return False
                p_to_w[pattern[i]] = s_words[i]
                w_to_p[s_words[i]] = pattern[i]

        return True


sol = Solution()
print(sol.wordPattern("abba", "dog cat cat dog") == True)
print(sol.wordPattern("abba", "dog cat cat fish") == False)
print(sol.wordPattern("aaaa", "dog cat cat dog") == False)
print(sol.wordPattern("aaa", "aa aa aa aa") == False)