// 题意：寻找array中是否有三个元素大小符合 1 3 2

// 解法1：暴力解
// 列出所有三元组，查看是否符合要求
// n^3

// 解法2：针对解法1的改进
// 逻辑如下：遍历nums，让每个元素轮流成为 3，让当前最小元素成为 1，那么如果在 3 后面找不到满足要求的 2，
// 无论如何更改 1 也无法满足要求
// n^2
class Solution {
    public boolean find132pattern(int[] nums) {
        // 一个技巧：每次让 j 向后挪一位，然后看看 i 有没有变得更小的可能性，min_i的值被从前一次循环中带进下一次循环
        int min_i = Integer.MAX_VALUE;
        for (int j = 0; j < nums.length - 1; j++) {
            min_i = Math.min(min_i, nums[j]);
            for (int k = j + 1; k < nums.length; k++) {
                if (nums[k] < nums[j] && min_i < nums[k])
                    return true;
            }
        }
        return false;
        
    }
}
