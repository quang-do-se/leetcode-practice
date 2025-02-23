class Solution {
    public int[] plusOne(int[] digits) {
        int carry = 1;
        for (int i = digits.length - 1; i > -1; i--) {
            int v = digits[i] + carry;
            if (v > 9) {
                carry = 1;
                v -= 10;
            } else {
                carry = 0;
            }
            digits[i] = v;
        }
        if (carry == 1) {
            int[] res = new int[digits.length + 1];
            res[0] = carry;
            for (int i = 1; i < res.length; i++) {
                res[i] = digits[i - 1];
            }
            return res;
        }
        return digits;
    }
}