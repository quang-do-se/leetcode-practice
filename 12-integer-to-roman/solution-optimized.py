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

        roman_digits = []

        for value, symbol in latins.items():
            if num == 0:
                break

            count, num = divmod(num, value)
            roman_digits.append(symbol * count)

        return "".join(roman_digits)


sol = Solution()
print(sol.intToRoman(10))
print(sol.intToRoman(58))
print(sol.intToRoman(3749))
