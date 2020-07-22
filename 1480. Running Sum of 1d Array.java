// 做题思路：
// 1. 读题：题目是什么意思，给了什么输入，要求什么输出
// 2. 算法：获得一个初步的模糊解法
// 3. 优化：怎么样获得更佳算法，以及trade off
// 4. corner case
// 5. 选用什么数据结构
// 6. coding


// 读题：给了一个array，返回一个array
// 算法：遍历，n
// 优化：因为输出一个新的array，所以时间复杂度肯定不会小于n，重点在于如何更快获得每个元素
//       暴力解法：每个元素都重新遍历array，时间复杂度为 n^2
//       优化解法：使用一个额外的变量记录当前的sum，这样每个新元素的添加时间为常量，时间复杂度为 n
// corner case: 如果nums中不存在元素，如何操作
// 数据结构：array

class Solution {
    public int[] runningSum(int[] nums) {
        // 创建一个新的array
        int[] ans = new int[nums.length];
        // 记录当前sum的变量
        int sum = 0;
        // 遍历nums
        for (int i = 0; i < nums.length; i++) {
            sum += nums[i];
            ans[i] = sum;
        }
        // 输出
        return ans;
    }
}
