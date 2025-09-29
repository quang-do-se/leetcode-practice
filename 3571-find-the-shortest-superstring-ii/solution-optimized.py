class Solution:
    def shortestSuperstring(self, s1: str, s2: str) -> str:
        n, m = len(s1), len(s2)

        if n > m:
            s1, s2, n = s2, s1, m

        if s1 in s2: return s2

        for i in range(1, n):
            if s1[i:] == s2[:n-i]:
                return s1[:i] + s2
            if s2[-n+i:] == s1[:-i]:
                return s2 + s1[n-i:]

        return s1 + s2
    

sol = Solution()

print(sol.shortestSuperstring("abc", "bcda") == "abcda")
print(sol.shortestSuperstring("bcda", "abc")  == "abcda")
print(sol.shortestSuperstring("gwb", "slfg") == "slfgwb")
print(sol.shortestSuperstring("kbcdefg", "defghijk") == "kbcdefghijk")
print(sol.shortestSuperstring("abcd", "cdea") == "abcdea")
print(sol.shortestSuperstring("m", "azmvzfh") == "azmvzfh")