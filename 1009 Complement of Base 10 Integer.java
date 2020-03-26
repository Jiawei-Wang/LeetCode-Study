class Solution {
    public int bitwiseComplement(int N) {

        if (N == 0) {
            return 1;
        }

        int total = 0;
        int digit = 0;

        while (total < N) {
            total += Math.pow(2, digit);
            digit += 1;
        }
        return total - N;
    }
}
