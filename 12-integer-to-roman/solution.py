class Solution:
    def intToRoman(self, num: int) -> str:
        latins = {
            1000: "M",
            900: "CM",
            500: "D",
            400: "CD",
            100: "C",
            90: "XC",
            50: "L",
            40: "XL",
            10: "X",
            9: "IX",            
            5: "V",
            4: "IV",
            1: "I",
        }

        res = ""
        unit = 1
        while num > 0:
            digit = num % 10
            
            latin_num = ""
            reg_num = digit * unit
            while reg_num > 0:            
                for key, val in latins.items():
                    if reg_num >= key:
                        latin_num += val
                        reg_num -= key
                        break
            res = latin_num + res

            unit *= 10
            num //= 10

        return res


sol = Solution()
print(sol.intToRoman(10))
print(sol.intToRoman(58))
print(sol.intToRoman(3749))