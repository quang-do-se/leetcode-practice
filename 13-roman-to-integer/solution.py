class Solution:
    def romanToInt(self, s: str) -> int:
        map = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

        sum = 0
        previous = float("inf")

        for char in s:
            current_number = map[char]

            if current_number <= previous:
                sum += current_number
            else:
                sum += -previous + current_number - previous

            previous = current_number

        return sum


sol = Solution()
print(sol.romanToInt("I") == 1)
print(sol.romanToInt("V") == 5)
print(sol.romanToInt("IV") == 4)
print(sol.romanToInt("III") == 3)
print(sol.romanToInt("LVIII") == 58)
print(sol.romanToInt("MCMXCIV") == 1994)