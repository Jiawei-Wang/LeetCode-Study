import java.math.BigInteger;

public class Solution {
    
    /**
     * Determines whether a String num representing at least 3 distinct
     * integers is additive.
     * 
     * Ex. "112" is additive, since 1 + 1 = 2
     * Ex. "12358" is additive, since:
     *      1 + 2 = 3, 2 + 3 = 5, and 3 + 5 = 8
     * Ex. "011" is additive, since 0 + 1 = 1
     * 
     * Ex. "1203" is NOT additive, since although 1 + 2 = 3,
     * 3 has a leading zero, which is not allowed.
     * 
     * @param num the given number
     * @return {@code true} if the given number is additive,
     *         {@code false} otherwise.
     */
    public boolean isAdditiveNumber(String num) {
        int n = num.length();
        
        /**
         * Iterate over possible first numbers.
         * 
         * The first number is defined as num.substring(0, i),
         * inclusive of 0, and exclusive of i.
         * 
         * Note that the first number, when added to a second number of any
         * length, must produce a sum that is at least the length of the first
         * number.
         * 
         * Accordingly, the first number cannot be more than half the length
         * of the given String num.
         * 
         * Accordingly, we can stop iterating when i reaches (n / 2) + 1.
         * 
         * Note also that when num.length < 2, this loop exits, thus handling
         * some of the invalid-length inputs.
         */
        for (int i = 1; i <= n / 2; i++) {
            
            /**
             * Iterate over possible second numbers.
             * 
             * The second number is defined as num.substring(i, i + j),
             * inclusive of i, and exclusive of i + j.
             * 
             * Note that the second number, when added to a first number of any
             * length, must produce a sum whose length is at least
             * the maximum of either i or j.
             * 
             * Accordingly, if n is the length of the given num, and i of those
             * digits belong to the first number, and j of those digits belong
             * to the second number, then (n - i - j) digits are left for the
             * sum.
             * 
             * Since the length of the sum is at least max(i, j), we can stop
             * iterating when max(i, j) exceeds n - i - j.
             * 
             * Note also that when num.length == 2, this loop exits, thus
             * handling the remaining invalid-length input case.
             */
            for (int j = 1; Math.max(i, j) <= n - i - j; j++) {
                if (isValid(i, j, num)) return true;
            }
        }
        return false;
    }
    
    /**
     * Is the given num additive?
     * 
     * @param i the length of the first number
     * @param j the length of the second number
     * @param num the given number
     * @return {@code true} if the given number is additive, where:
     *         the first number has a length of i,
     *         the second number has a length of j and begins at num[i],
     *         the first sum begins at num[i + j],
     *         {@code false} otherwise
     */
    private boolean isValid(int i, int j, String num) {
        
        /**
         * Check for leading zero in first number.
         * 
         * Note that the first number is allowed to be zero, but it's not
         * allowed to be more than one digit long with zero as the first digit.
         */
        if (num.charAt(0) == '0' && i > 1) return false;
        
        /**
         * Check for leading zero in second number.
         * 
         * Note that the second number is allowed to be zero, but it's not
         * allowed to be more than one digit long with zero as the first digit.
         */
        if (num.charAt(i) == '0' && j > 1) return false;
        
        // The sum of the first and second numbers
        String sum;
        
        // The first number
        BigInteger b1 = new BigInteger(num.substring(0, i));
        
        // The second number
        BigInteger b2 = new BigInteger(num.substring(i, i + j));
        
        /**
         * Check whether num obeys the Additive pattern described in the 
         * problem statement.
         * 
         * Specifically, given our first and second numbers:
         * (1) Compute their sum,
         * (2) Update the second number to be this sum (for the next iteration),
         * (3) Update the first number to be the previous second number,
         * (4) Check whether the next number in the given num is sum,
         * (5) Repeat until the start of the next sum exceeds the last index
         *     of the given num.
         * 
         * Note that offset below is our "offset" for where the next sum
         * comparison should occur in the given num.
         * 
         * Thus, offset initializes to the lengths of the first and second
         * numbers (due to zero-indexing, offset = 2 starts sum at the third
         * digit of num).
         * 
         * Note also that offset increments by the length of the previous sum,
         * which cleverly handles the sum's tendency to grow in length.
         */
        for (int offset = i + j; offset < num.length(); offset += sum.length()) {
            
            // The second number becomes the sum of the first and second numbers
            b2 = b2.add(b1);
            
            // The first number becomes the second number
            b1 = b2.subtract(b1);
            
            /**
             * Store the sum as a String for use with startsWith below, and
             * for incrementing the offset in this for loop
             */
            sum = b2.toString();
            
            // Check whether the next digits of num, at an offset of offset, are sum
            if (!num.startsWith(sum, offset)) return false;
        }
        return true;
    }
}