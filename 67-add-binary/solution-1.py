class Solution:
    # No addition approach
    def addBinary(self, a: str, b: str) -> str:
        ai = len(a) - 1
        bi = len(b) - 1
        carry = 0
        res = []

        while ai >= 0 or bi >= 0 or carry:
            va = int(a[ai]) if ai >= 0 else 0
            vb = int(b[bi]) if bi >= 0 else 0

            v = va ^ vb ^ carry

            carry = (va & vb) | (va & carry) | (vb & carry)

            res.append(str(v))
            ai -= 1
            bi -= 1

        return ''.join(res[::-1])   # Reverse result


sol = Solution()
print(sol.addBinary("11", "1") == "100")
print(sol.addBinary("1010", "1011") == "10101")
print(sol.addBinary("11", "11") == "110")
print(sol.addBinary("101", "11") == "1000")
print(sol.addBinary("111", "11") == "1010")