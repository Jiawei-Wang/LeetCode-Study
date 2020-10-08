// 做题思路：
// 1. 读题：题目是什么意思，给了什么输入，要求什么输出
// 2. 算法：获得一个初步的模糊解法
// 3. 优化：怎么样获得更佳算法，以及trade off
// 4. corner case
// 5. 选用什么数据结构
// 6. coding


// 读题：给一个array，返回一个int，该int是：把元素两两配对后，取对中较小值，让所有较小值总和最大
// 算法：给元素排序，然后取每两个元素中的第一个

class Solution {
    public int arrayPairSum(int[] nums) {
        Arrays.sort(nums);
        int result = 0;
        for (int i = 0; i < nums.length; i += 2) {
            result += nums[i];
        }
        return result;
    }
}
// 两个关注点：1. Array.sort()；2. i+=2
