class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        s = ""
        if len(str1) < len(str2):
            s = str1
        else:
            s = str2

        l = len(s)
        len1, len2 = len(str1), len(str2)

        for i in range(l, 0, -1):
            if len1 % i or len2 % i:
                continue
            
            f1, f2 = len1 // i, len2 // i

            base = s[:i]

            if base * f1 == str1 and base * f2 == str2:
                return base
        
        return ""

sol = Solution()    
print(sol.gcdOfStrings("ABABAB", "AB"))