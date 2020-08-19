// 改变至多 1 个元素的值，来使得array变成non-decreasing

// 解法1：brute force，改变每一个元素大小为前一个元素，查看array是否符合要求
class Solution {
    // 创建一个新的int array
    int[] newNums;

    // main
    public boolean checkPossibility(int[] nums) {
        // 对新的array进行初始化，复制nums的所有元素
        // 切记不要使用 a = b，因为这只是提供了一个新的指针
        newNums = nums.clone();
        // 使用下标遍历nums每个元素
        for (int i = 0; i < nums.length; i++) {
            // 使用变量保存当前下标
            int temp = nums[i];
            // 将newNums中对应的元素的值改为前一个元素的值，注意0号元素的corner case
            if ( i > 0) newNums[i] = newNums[i-1];
            if ( i == 0) newNums[i] = Integer.MIN_VALUE;
            // call helper
            if (helper(newNums)) return true;
            // 将元素的值修改回去
            newNums[i] = temp;
        }
        return false;
    }

    // helper
    private boolean helper(int[] newNums) {
        // 遍历每个元素，如果其小于前一个元素，返回false
        for (int i = 1; i < newNums.length; i++) {
            if (newNums[i] < newNums[i-1]) return false;
        }
        return true;
    }
}
