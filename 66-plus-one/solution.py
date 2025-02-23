from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        for i in range(len(digits) - 1, -1, -1):
            v = digits[i] + carry

            carry = 0
            if v > 9:
                carry = 1
                v -= 10
            digits[i] = v

            if not carry:
                return digits

        if carry:
            digits.insert(0, 1)

        return digits