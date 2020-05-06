class Solution {
    public int[] smallerNumbersThanCurrent(int[] nums) {
        // 题目条件：所有元素均在[0,100]范围内，一共101个可能性
        // 在括号内使用数字来初始化list的长度
        int[] count = new int[101];
        // 返回的list，每个位置上是nums中每个元素对应小于它的元素个数
        int[] res = new int[nums.length];

        // 对于nums内每个元素，记录其出现次数，存储在count中和这个元素值相等的index下
        // for循环：1.圆括号，2.三段式，3.分号
        for (int i =0; i < nums.length; i++) {
            // 使用下标访问元素的方法
            count[nums[i]]++;
        }

        // 将count内每个元素出现次数和比它小的元素的出现总次数相加(暂时先不管0)
        for (int i = 1 ; i <= 100; i++) {
            count[i] += count[i-1];
        }

        // 如果nums内有0元素，没有比它小的元素，所以它那个位置是0
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] == 0)
                res[i] = 0;
            else
                res[i] = count[nums[i] - 1];
        }

        return res;
    }
}
