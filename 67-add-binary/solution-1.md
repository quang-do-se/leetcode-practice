https://leetcode.com/problems/add-binary/solutions/6474614/pure-bit-manipulation-no-addition-no-int-kid7/

# Intuition
Adding the numbers bit by bit in their original binary format with bit-wise operators.

# Approach
This approach is similar to the Bit-by-Bit Computation in the Editorial Solution, but with one key difference: we avoid using addition entirely.

To calculate the sum at each bit without the carry, we can simply use XOR operation:
`va ^ vb`
Where:
- `va` is the bit value at the current position in `a`.
- `vb` is the bit value at the current position in `b`.
- `va` and `vb` can each be either `0` or `1`

The XOR operation gives us the correct sum for each bit:
`1 ^ 0` = `1`
`0 ^ 1` = `1`
`1 ^ 1` = `0`
`0 ^ 0` = `0`

### Incorporating the Carry
To obtain the final sum, we need to include the carry from the previous bit calculation:
`sum = (va ^ vb) ^ carry`

There are three scenarios when adding carry:
1. There is no carry, the sum remains the same:
`(1 ^ 0) ^ 0` = `1`
`(0 ^ 1) ^ 0` = `1`
`(1 ^ 1) ^ 0` = `0`
`(0 ^ 0) ^ 0` = `0`

2. Sum of `va` and `vb` is `0`, but there is a carry:
`(1 ^ 1) ^ 1` = `1`
`(0 ^ 0) ^ 1` = `1`

3. Sum of `va` and `vb` is `1`, with a carry present:
`(1 ^ 0) ^ 1` = `0`
`(0 ^ 1) ^ 1` = `0`

As observed, this correctly computes the sum at each bit.

### Computing the Carry
The tricky part is determining the new carry value. There are three scenarios:

1. Both `va` and `vb` are `0`, there will be no carry, regardless of the previous carry.
2. Both `va` and `vb` are `1`, there will be a carry.
3. One of `va` and `vb` is `1`, there will be a carry if there is a previous carry.

We can compute the carry as follows:
- Scenario 1 and 2 can be solved with `va & vb`, which captures the case where both bits are `1`.
- Scenario 3 can be solved with XOR and AND. `(va ^ vb) & carry` captures the case where one bit is `1` and there's an existing carry.

### Final Formula

Combining both parts, we derive:
``` python
sum = va ^ vb ^ carry
carry = (va & vb) | ((va ^ vb) & carry)
```
This ensures the correct sum and carry computation at each bit.

# Complexity
- Time complexity: O(max(N,M))

- Space complexity: O(max(N,M)) for output

# Code
```python3 []
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        ai = len(a) - 1
        bi = len(b) - 1
        carry = 0
        res = []

        while ai >= 0 or bi >= 0 or carry:
            va = int(a[ai]) if ai >= 0 else 0
            vb = int(b[bi]) if bi >= 0 else 0

            sum_without_carry = va ^ vb

            sum = sum_without_carry ^ carry

            carry = (va & vb) | (sum_without_carry & carry)

            res.append(str(sum))
            ai -= 1
            bi -= 1

        return ''.join(res[::-1])   # Reverse result
```