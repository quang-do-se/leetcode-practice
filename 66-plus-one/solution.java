class Solution {
    public int[] plusOne(int[] digits) {
        int carry = 1;
        for (int i = digits.length - 1; i > -1; i--) {
            int v = digits[i] + carry;

            carry = 0;
            if (v > 9) {
                carry = 1;
                v -= 10;
            }
            digits[i] = v;

            if (carry == 0) {
                return digits;
            }
        }

        // cases: 9, 99, 999
        if (carry > 0) {
            digits = new int[digits.length + 1];
            digits[0] = 1;   // Since all digits to the right is 0, we don't need to copy the array
        }
        return digits;
    }
}