// 这是一道数学题，但是可以用来复习array的操作方法:
// 1. sum of array; 2. min element of array; 3. length of array
class Solution {
    public int minMoves(int[] nums) {
        int sum = 0;
        int min = nums[0];

        for (int i : nums) {
            min = Math.min(min, i);
            sum += i;
        }

        return sum - min * nums.length;
    }
}
