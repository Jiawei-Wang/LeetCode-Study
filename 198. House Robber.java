// 解法1：pure recursion
class Solution {
    // 两个method拥有相同的名字被称为overload

    // 主函数调用helper并传递相应参数
    public int rob(int[] nums) {
        return rob(nums, nums.length - 1);
    }

    // helper做两件事：1.base case，2.recursion form
    private int rob(int[] nums, int index) {
        if (index < 0) return 0;
        return Math.max(rob(nums, index - 2) + nums[index], rob(nums, index - 1));
    }
}

/*
对于这个程序的理解：
1. 给一个array，返回一个int
2. 状态转换方程：i的收益是 （i-2的收益+i；i-1的收益） 两者间的较大者
3. 注意base case
4. 使用一个method完成recursion，使用另外一个返回答案
*/


// 解法2：Recursive + memo (top-down)
class Solution {
    // 解法2在解法1的基础上improve: https://weibeld.net/algorithms/recursion.html

    // 不能在method里申明变量，另一个method无法使用
    int[] memo;

    // 主函数做两件事：1.初始化存储结构，2.调用helper
    public int rob(int[] nums) {
        memo = new int[nums.length];
        // 先给默认值
        Arrays.fill(memo, -1);
        return rob(nums, nums.length - 1);
    }

    // helper的任务：1.base case，2.如果存储结构中已经有该答案，返回，3.如果没有，计算并存入
    private int rob(int[] nums, int i) {
        if (i < 0) return 0;
        if (memo[i] != -1) return memo[i];
        return memo[i] = Math.max(rob(nums, i - 2) + nums[i], rob(nums, i - 1));
    }
}


// 解法3：Iterative + memo (bottom-up)
class Solution {
    public int rob(int[] nums) {
        if (nums.length == 0) return 0;
        // 这里使用比nums长1位的memo可以防止index越界
        int[] memo = new int[nums.length+1];
        memo[0] = 0;
        memo[1] = nums[0];
        for (int i = 1; i < nums.length; i++) {
            int val = nums[i];
            memo[i+1] = Math.max(memo[i], memo[i-1] + val);
        }
        return memo[nums.length];
    }
}


// Iterative + 2 variables (bottom-up)
class Solution {
    public int rob(int[] nums) {
        if (nums.length == 0) return 0;
        int prev1 = 0;
        int prev2 = 0;
        for (int num : nums) {
            int tmp = prev1;
            prev1 = Math.max(prev2 + num, prev1);
            prev2 = tmp;
        }
        return prev1;
    }
}
