class Solution:
    def addBinary(self, a: str, b: str) -> str:
        ai = len(a) - 1
        bi = len(b) - 1
        carry = 0
        res = []

        while True:
            va = int(a[ai]) if ai >= 0 else 0
            vb = int(b[bi]) if bi >= 0 else 0

            v = va + vb + carry

            carry = 0
            if v > 1:
                carry = 1
                v -= 2  # or v %= 2

            res.insert(0, str(v))
            ai -= 1
            bi -= 1

            if ai < 0 and bi < 0 and carry == 0:
                return ''.join(res)


sol = Solution()
print(sol.addBinary("11", "1") == "100")
print(sol.addBinary("1010", "1011") == "10101")
print(sol.addBinary("11", "11") == "110")
print(sol.addBinary("101", "11") == "1000")
print(sol.addBinary("111", "11") == "1010")