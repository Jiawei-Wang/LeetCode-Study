// new array + double loop
class Solution {
    public int[] shuffle(int[] nums, int n) {
        int[] ans = new int[nums.length];

        int j = 0;
        for (int i = 0; i < nums.length; i += 2) {
            ans[i] = nums[j];
            j ++;
        }
        for (int k = 1; k < nums.length; k += 2) {
            ans[k] = nums[j];
            j++;
        }
        return ans;

    }
}


// new array + simgle loop
class Solution {
    public int[] shuffle(int[] nums, int n) {
        int[] ans = new int[2 * n];
        for(int i = 0; i < nums.length; i++)
            // 对前一个解法进行了改良：学习这个表达式
            ans[i] = i % 2 == 0 ? nums[i/2] : nums[n + i/2];
        return ans;
    }
}
