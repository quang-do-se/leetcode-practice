
The symmetry of a row in Pascal's triangle allows us to get away with computing just half of each row.

### Pop Quiz: Are there any computational complexity benefits of doing this?

The worst case is still O(n) even if we only need to compute O(n/2).
However, there is a practical benefit by doing fewer multiplications and memory access, which can speed things up.

### Pop Quiz: Can you prove why these rows are symmetrical?

Mathematical Formula (Binomial Coefficient):
Each element in Pascal’s Triangle can be computed using: `C(n, k) = n! / (k! * (n - k)!)`

To prove symmetry, we need to show: `C(n, k) = C(n, n - k)`

`C(n, n - k) = n! / ((n - k)! * k!)`

`n! / (k! * (n - k)!) = n! / (k! * (n - k)!)`

`C(n, n - k) = C(n, k)`