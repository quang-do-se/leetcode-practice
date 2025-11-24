Because of how the pointers move, when the loop finishes you're _guaranteed_ that `right` is the floor of √x, while `left` has already stepped one past it.

### Key invariant

Throughout the search the code maintains this idea:
- everything **≤ right** is still a candidate whose square might be ≤ x
- everything **> right** is known to be too large (square > x)

More concretely:
- When `mid*mid < x`, `mid` is too small, so you do `left = mid + 1`.  
    That means **mid is valid**, but you move `left` _past_ it to look for a bigger valid number.
- When `mid*mid > x`, `mid` is too big, so you do `right = mid - 1`.  
    That means you shrink the upper side to the last potentially valid number.
    
So `left` always moves upward after finding something _valid_, and `right` always moves downward after finding something _invalid_.

### What happens at exit

The loop stops when `left > right`.  
At that moment:

- `right` is the **largest number such that right² ≤ x**
- `left` is the **smallest number such that left² > x**
    
That implies `right = left - 1`, and the integer square root (floor) is `right`.

### Tiny trace example: x = 8

√8 ≈ 2.82, answer should be `2`.

Start: `left=0, right=8`

1. `mid=4`, `16>8` ⇒ `right=3`    
2. `mid=1`, `1<8` ⇒ `left=2`    
3. `mid=2`, `4<8` ⇒ `left=3`    
4. `mid=3`, `9>8` ⇒ `right=2`
    
Now `left=3`, `right=2` ⇒ loop ends.  
`right=2` is the largest value with square ≤ 8, so return `2`.

If you returned `left`, you’d get `3`—too big.

---

So the short reason: **the algorithm is a "find last valid" binary search.**  
`left` overshoots to the first invalid value; `right` lands on the last valid value, which is exactly `⌊√x⌋`.