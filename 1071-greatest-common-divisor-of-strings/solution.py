class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:

        len1, len2 = len(str1), len(str2)

        for i in range(min(len1, len2), 0, -1):
            if len1 % i or len2 % i:
                continue
            
            f1, f2 = len1 // i, len2 // i

            base = str1[:i]

            if base * f1 == str1 and base * f2 == str2:
                return base
        
        return ""  


sol = Solution()    
print(sol.gcdOfStrings("ABABAB", "AB"))